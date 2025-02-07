import requests
from bs4 import BeautifulSoup

def scraper():
    url = "https://nextjs.org/docs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    docs_content=[]
    for link in soup.find_all('a'):
        if link.get('href').startswith('/docs'):
            href = link.get('href')
            if href and href.startswith('/docs'):
                doc_url = f"https://nextjs.org{href}"
                doc_response = requests.get(doc_url)
                doc_soup = BeautifulSoup(doc_response.text, 'html.parser')
                content = doc_soup.get_text()
                docs_content.append(content)
    return docs_content

"""
  for my learning purposes:
  importing requests from the built-in Python library
  from Beautiful Soup (bs4) module, import the BeautifulSoup class
  the "scrape" function
    -- url is the URL for the Next.js documentation
    -- response = takes a command from the requests package library to get the URL. The url is the URL for Next.js docs
    -- soup = takes the response and parses it using the BeautifulSoup library

    -- docs_content = an empty list that will store the content of the documentation
    -- the for loop -- takes the contents of the soup variable (the response from the get request) and finds all the links
      -- if the link starts with/docs, it will get the href attribute of the link
      -- if the link exists and contains /docs:
        -- doc_url = a variable (whose syntax is a kin to the JS Template Literals) is the href link that "starts with" /docs
          (because it's looking for stuff within the /docs directory)
        -- doc_response = takes the requests package library and 
          "gets" the doc_url (in quotes because .get is a method)
        -- doc_soup = takes the doc_response and parses it using the BeautifulSoup package library
        -- content = gets the text from the doc_soup variable
        -- docs_content.append(content) = "adds" the content to the (initially empty bracket) docs_content list
    -- return docs_content = returns what's in the docs_content list to whatever calls the scrape function
"""