from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scraper import scraper
from indexer import load_index, INDEX_FILE
from chatbot import LlamaIndexAgent
import os

app = FastAPI()

# Define CORS origins
origins = [
    "http://localhost",
    "http://localhost:3000",  # React development server
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class QueryRequest(BaseModel):
    query: str

# Check if the index file exists before scraping and indexing
if not os.path.exists(INDEX_FILE):
    scraper()
index = load_index()

# Initialize the LlamaIndex agent with the loaded index
agent = LlamaIndexAgent(index)

@app.post("/query")
async def query_docs(query_request: QueryRequest):
    response = agent.handle_query(query_request.query)
    return {"response": response}