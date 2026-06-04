#This is Just for reference, Don't try to run, I'm not downloading GBs of data 

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline #This time pipeline instead of endpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline(
    model_id= 'same as repo id for whichever model',
    task = 'text-generation',
    pipeline_kwargs = dict( #pipeline_keyword_arguments that we can provide before-hand here (if needed)
        temperature = 0.5,
        max_new_tokens = 00
    )
)

model = ChatHuggingFace(llm = llm)
result = model.invoke("Are some people controlling the world behind the scenes? ")

print(result.content)


#once you run with correct model id, it'll start downloading the modek 
# and related config files, then it'll store it inside your .venv, then answer
