from langchain_openai import OpeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-small", dimenstions = 512)  
#context capturing more at more dim, but also increase bill
#you can find those openai embed models here -> https://developers.openai.com/api/docs/guides/embeddings

result = embedding.embed_query('I love eating apples')

#of if you wanna generate for a whole doc with seperate vector for each sentence
document = [        #make a list of sentences / queries
    "I love to eat apple", "my whole family loves apple" , "my family loves me",
    "I am apple", "I love eating myself"
]
result_doc = embedding.embed_document(document)

print(str(result)) # just using string to print for readability