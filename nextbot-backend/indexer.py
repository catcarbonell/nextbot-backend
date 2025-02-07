from llama_index import LlamaIndex

def create_index(docs_content):
  index = LlamaIndex()
  for doc in docs_content:
    index.add_document(doc)
    return index
  
  """
  from the llama_index package/module import the LlamaIndex class
  create_index function that takes docs_content as an argument
  index = a variable that is an instance of the LlamaIndex class
  for loop that takes the doc in the docs_content list
    -- index.add_document(doc) = adds the doc to the index
      - the add_document method is a method of the LlamaIndex class
    -- return index = returns the index to whatever calls the create_index function
  """