import csv
from langchain_core.documents import Document

documents = [] #since each row in csv will be a seperate doc object, so list of doc objects stored

with open("netflix_titles_sample.csv", mode = "r" , encoding='utf-8') as f:
    reader = csv.DictReader(f) #returns an iterator 'reader' which gives one row at a time as a dict, with {key = col1_name , val = corresponding_val_in_row, col2_name : corresponding_val_in_row ... 
    #since it's fetching one at a time, not storing in RAM memory, thus file needs to be open throughout

    for row_idx, row in enumerate(reader, start = 1):
        text = " , ".join(f"{k} : {v}" for k,v in row.items())
        doc = Document(page_content=text, metadata = {'source' : "netflix_titles_sample.csv", "row": row_idx})
        documents.append(doc)

    print(documents[0].page_content)