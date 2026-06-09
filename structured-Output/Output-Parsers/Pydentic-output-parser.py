from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= 'meta-llama/Llama-3.1-8B-Instruct',
    task= 'text-generation',
    temperature=0.1
)

model = ChatHuggingFace(llm=llm)

#define the schema pydantic object class
class person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(gt = 18, description='age of the person')
    city : str = Field(description='city the person belongs to')


parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template= 'Generate the name, age and city of a fictional {place} person {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke({'place' : 'Indian'})

print(result)