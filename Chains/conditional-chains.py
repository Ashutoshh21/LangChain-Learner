from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()



model = ChatGroq(model = 'openai/gpt-oss-20b')



class Feedback(BaseModel):
    sentiment : Literal['Positive', 'Negetive'] = Field(description='Return the sentiment, whether Positive or Negetive, for the given feedback')

parser = PydanticOutputParser(pydantic_object=Feedback)

strparser = StrOutputParser()

prompt1 = PromptTemplate(
    template='classify the sentiment of this given feedback into positive or negetive : {feedback} \n Do as per the format : {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions' : parser.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template = 'Generate an appropriate response for this positive feedbac: {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = 'Generate an appropriate response to this negetive feedback: {feedback} ',
    input_variables=['feedback']
)


classifier_Chain = prompt1 | model | parser

conditional_chain = RunnableBranch(
    (lambda x: x.sentiment == 'Positive' , prompt2 | model | strparser),
    (lambda x : x.sentiment == 'Negetive' , prompt3 | model | strparser),
    RunnableLambda(lambda x : 'Sentiment could not be resolved')
)

final_chain = classifier_Chain | conditional_chain

res = final_chain.invoke({'feedback', 'This Phone is terrible, do not buy it' })

print(res)