
from fastapi import FastAPI
from pydantic import BaseModel
from scraper import scraper
from indexer import load_index, INDEX_FILE
from chatbot import query_index, ask_openai
import os

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

if not os.path.exists(INDEX_FILE):
    scraper()
index = load_index()

@app.post("/query")
def query_docs(query: QueryRequest):
    results = query_index(index, query.query)
    response = ask_openai(results)
    return {"response": response}
