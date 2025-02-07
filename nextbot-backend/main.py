
from fastapi import FastAPI
from pydantic import BaseModel
from scraper import scraper
from indexer import create_index
from chatbot import query_index, ask_openai

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

docs_content = scraper()
index = create_index(docs_content)

@app.post("/query")
def query_docs(query: QueryRequest):
    results = query_index(index, query.query)
    response = ask_openai(results)
    return {"response": response}


"""
FastAPI is a package/module that makes it easy to build with APIs. It's primarily a tool for building APIs with Python.
Pydantic is a package/module that makes it easy to work with data in Python. Mainly used for working with data in Python.
scraper, indexer, and chatbot are my own modules that import all the functions I will be using in the main.py file where 
it brings the backend of the app together.

First, declare the FastAPI function and assign it a variable "app". We use it repeatedly throughout the file.
Then, a QueryRequest class is created/defined with Pydantic by using "BaseModel" as an argument. 
"BaseModel" is a class from Pydantic that is used to create a new model.
 - within the QueryRequest class is a "query" variable (or attribute) that is a string (str) type

 The docs_content variable is assigned to the scraper() function, which is a function that scrapes the Next.js documentation.
T
he index variable is assigned to the create_index function, which is a function that creates an index of the docs_content.

All of this comes together in the @app.post("/query") decorator, which is attached to the FastAPI function (app) that takes a QueryRequest object as an argument.
Everything under the decorator (@app) is appended to everything that's contained in the .post method (with the argument of "/query").
.post handles the HTTP POST requests and sends them to the "/query" endpoint, at which the URL will look like: http://localhoast:8000/query
The function defined after the decorator (query_docs) will handle the POST requests sent to the ("/query") endpoint.
-- This is where the backend connects to the frontend from the backend

The query_docs function takes the QueryRequest class/object as an argument
-- the results variable is assigned to the query_index function from the chatbox module, which is a function.
-- The query_index function takes in "index" argument (which is the index of the results from docs_content) 
and the "query" argument (which is the query from the frontend)
that searches the indexed docs for data related to the query that was obtained from the frontend (the user's question).
-- the response variable contains the ask_openai function from the chatbot module, which is a function that feeds the question to OpenAI
-- The return statement ({"response": response}) is formatted in JSON so that the frontend can read it and display the response to the user.
It allows the client-side to display the generated response to the user.
 """