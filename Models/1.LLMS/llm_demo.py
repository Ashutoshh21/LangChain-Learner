#This notebook is just for reference, I don't have OpenAI API keys

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = ' gpt-3.5-turbo-instruct')

result = llm.invoke("what is the capital of Siberia?") # <- notice raw string input

print(result)

