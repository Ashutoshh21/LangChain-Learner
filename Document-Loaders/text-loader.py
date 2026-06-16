from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader #not necessary here though 

"""
since the langchain_community has been sunsetted completely, thus TextLoader has been removed and PyPDF resides in 'langchain_pdf.document_loaders'
Best way to use .txt file is via standard file reader and converting into Document object explicitly
"""
with open('poem.txt', 'r', encoding='utf-8') as f:
    text = f.read()

doc = Document(page_content=text, metadata = {"source" : 'poem.txt'})

print(doc)
