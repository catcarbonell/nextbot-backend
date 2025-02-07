from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex
import os
import pickle

INDEX_FILE = 'index.pkl'

def create_index():
    reader = SimpleDirectoryReader('docs')
    documents = reader.load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    
    # Store the index to a file
    with open(INDEX_FILE, 'wb') as f:
        pickle.dump(index, f)
    
    return index

def load_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'rb') as f:
            index = pickle.load(f)
        return index
    else:
        return create_index()