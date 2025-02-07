import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def query_index(index, query):
  results = index.search(query)
  return results

def ask_openai(query):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=query,
    max_tokens=150
  )
  return response.choices[0].text.strip()