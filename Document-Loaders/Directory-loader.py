from langchain_core.documents import Document
from pathlib import Path
from pypdf import PdfReader

pdf_dir = Path("targ_directory") #or ./"targ_directory"

documents = []

for file_path in pdf_dir.glob("*.pdf"):
    try:
        reader = PdfReader(file_path)
        
        for page_num , page in enumerate(reader.pages, start = 1):
            text = page.extract_text()
            if text.strip():
                doc = Document(page_content=text, metadata = {'soruce':str(file_path.name), 'page' : page_num})
                documents.append(doc)

    except Exception as e:  
        print(f"Skipping broken file {file_path.name}: {e}")     

print(len(documents))