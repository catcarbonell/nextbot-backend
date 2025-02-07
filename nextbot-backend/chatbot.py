import openai
from dotenv import load_dotenv
import os
import time
from cachetools import TTLCache

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Create a cache with a TTL of 1 hour and a max size of 100 entries
cache = TTLCache(maxsize=100, ttl=3600)
last_request_time = 0

def query_index(index, query):
    results = index.search(query)
    return results

def ask_openai(query):
    global last_request_time
    
    # Check the cache first
    if query in cache:
        return cache[query]
    
    # Rate limiting: ensure at least 1 second between requests
    current_time = time.time()
    if current_time - last_request_time < 1:
        time.sleep(1 - (current_time - last_request_time))
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=150
    )
    last_request_time = current_time
    
    # Cache the response and return it
    answer = response.choices[0].text.strip()
    cache[query] = answer
    return answer