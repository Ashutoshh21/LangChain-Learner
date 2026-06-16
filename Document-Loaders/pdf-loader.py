from langchain_core.documents import Document
from pypdf import PdfReader

"""
Install the lightweight, standard PDF parsing library via terminal.
Use pypdf to extract the text and wrap it directly into a standard LangChain Document object
"""


reader = PdfReader('example.pdf')
documents = []

for page_num, page in enumerate(reader.pages, start= 1):
    text = page.extract_text()

    #skip empty pages
    if text.strip():
        doc = Document(page_content=text, metadata = {'source' : 'example.pdf', 'page' : page_num})
        documents.append(doc)


print(documents[0].page_content)
print(len(documents)) #No of pages