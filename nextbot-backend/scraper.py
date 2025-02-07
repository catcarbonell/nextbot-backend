import os
import requests
from bs4 import BeautifulSoup

def scraper():
    url = "https://nextjs.org/docs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    docs_dir = "docs"
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/docs'):
            doc_url = f"https://nextjs.org{href}"
            doc_response = requests.get(doc_url)
            doc_soup = BeautifulSoup(doc_response.text, 'html.parser')
            content = doc_soup.get_text()
            
            # Save content to a file
            filename = href.replace('/docs', '').replace('/', '_') + '.txt'
            with open(os.path.join(docs_dir, filename), 'w', encoding='utf-8') as f:
                f.write(content)