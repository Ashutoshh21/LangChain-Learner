
from langchain_core.documents import Document
from pathlib import Path
from pypdf import PdfReader

pdf_dir = Path("targ_directory") #or ./"targ_directory"

#The yield is the key word here which does all the magic, making a custom function and 
# 'yield' instead of 'return' makes it the returned value streamable object

def lazy_load(pdf_dir):
    for file_path in pdf_dir.glob("*.pdf"):
        try:
            reader = PdfReader(file_path)
            
            for page_num , page in enumerate(reader.pages, start = 1):
                text = page.extract_text()
                if text.strip():
                    yield Document(page_content=text, metadata = {'soruce':str(file_path.name), 'page' : page_num})

        except Exception as e:  
            print(f"Skipping broken file {file_path.name}: {e}")


streamm = lazy_load(pdf_dir) #or directly pass the func in iterable loop below

for document in streamm:
    print(document.page_content)