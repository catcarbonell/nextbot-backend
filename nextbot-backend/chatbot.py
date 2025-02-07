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

"""
from the openai package/module, import the openai class
from the dotenv package/module, import the load_dotenv function
from the os package/module, import the os module 
  (which is a built-in Python module) that allows you to interact
  with the operating system, in this case it's using a tool that accesses
  the.env file, specifically the API key for OpenAI

First step is to initiate load_dotenv() to load the .env file
Then, use the openai.api_key method to access the API key from 
the .env file with the "key word" OPENAI_API_KEY

First function is query_index, which takes two arguments: index and query
  -- a results variable stores the results of the index.search method 
  (that has the query as an argument)
  -- return results = returns the results of the index.search method to 
  whatever calls the query_index function

Second function is ask_openai, which takes one argument: query
  -- it is for asking OpenAI a question
  -- a response variable stores the response from the openai.Completion.create method
  where the "engine" is "text-davinci-003", the prompt is the query, and the max_tokens is 150
  
return response.choices[0].text.strip() = returns the response to whatever calls 
the ask_openai function
  -- breaking it down: 
    - response = the variable created above that sets up what engine to use, 
   prompt, and how many tokens it should use 
    - choices[0] = a method from openai.Completion.create() that takes the first choice in the response with zero being the index
    - .text = taking the text of the response
    - .strip() = a method removes any whitespace from the text

"""











