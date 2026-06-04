from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

result = embedding.embed_query("Hi I am Mr Vanilla") #this whole thing is converted into a fixed dim vector, not per word, but for whole sentence
#Here we unlike openai , cannot set dimensions= 128 or something manually
#Here also, we can use embed_documents() func for whole docs

print(result[:10])