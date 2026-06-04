from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct', # we can access these from their pages, in modelssection, some are paid (Inference endpoints) some are free for api use ( serverless / inference providers) but all are free to download
    task = 'text-generation'  
)

model = ChatHuggingFace(llm= llm) #only difference from closed source is this extra parameter

result = model.invoke("What is the Capital of India ? ")

print(result.content)