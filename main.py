
from fastapi import FastAPI, Request # Imports FastAPI class from fastapi module
from pydantic import BaseModel # Imports BaseModel class from pydantic module
from scraper import scraper # Imports scraper function from scraper module
from indexer import load_index, INDEX_FILE # Imports load_index function and INDEX_FILE (variable for str 'index.pkl' which is storage for index) from indexer module
from chatbot import LlamaIndexAgent 
import os # Imports os module

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

if not os.path.exists(INDEX_FILE):
    scraper()
index = load_index()

agent = LlamaIndexAgent(index)

@app.post("/query")
def query_docs(query_request: QueryRequest):
    response = agent.handle_query(query_request.query)
    return {"response": response}
