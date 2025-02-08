import os
import time
from cachetools import TTLCache
from llama_index.core import VectorStoreIndex
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

cache = TTLCache(maxsize=100, ttl=3600)
last_request_time = 0

def query_index(index, query):
    retriever = index.as_retriever()
    results = retriever.retrieve(query)
    return results

def ask_openai(prompt):
    global last_request_time

    prompt_key = str(prompt)

    # Check the cache first
    if prompt_key in cache:
        return cache[prompt_key]

    # Rate limiting: ensure at least 1 second between requests
    current_time = time.time()
    if current_time - last_request_time < 1:
        time.sleep(1 - (current_time - last_request_time))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt_key}
            ]
    )
    
    last_request_time = current_time

    # Cache the response and return its
    answer = response.choices[0].message.content
    cache[prompt_key] = answer
    return answer
class LlamaIndexAgent:
    def __init__(self, index: VectorStoreIndex):
        self.index = index

    def handle_query(self, query: str):
        # Query the index for relevant documents
        results = query_index(self.index, query)
        # Formulate a response using the results
        response = ask_openai(results)
        return response