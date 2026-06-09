from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core import output_parsers
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= 'meta-llama/Llama-3.1-8B-Instruct',
    task = 'text-generation'
)

model = ChatHuggingFace(llm = llm)

parser = output_parsers.JsonOutputParser()

template= PromptTemplate(
    template = 'Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables= [],
    partial_variables= {'format_instruction' : parser.get_format_instructions()}
)


#Either manually
"""
prompt = template.invoke({}) #since in our template we already defined everything and no input var is given hence nothing passed in () here

res = model.invoke(prompt)

final_res = parser.parse(res.content) #parse is a low level func for parser, just like format() is for temp, both have an invoke() func that handles all
                                      #so parse expect res.content (raw strings) & not whole res
"""
#or via chains
chain = template | model | parser
final_res = chain.invoke({})


print(type(final_res)) 
print(final_res) #this isn't a str but a dict, so we can fetch like: ->  print(final_res['name'] ) 