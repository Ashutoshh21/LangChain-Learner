from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a Report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'summarize the text: {text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1, model, parser)

conditional_chain = RunnableBranch(
    (lambda x : len(x.split()) > 300 , RunnableSequence(prompt2,model, parser)), #x automatically captures output from chain-1
    (RunnablePassthrough())
)

final_chain = RunnableSequence(report_gen_chain , conditional_chain)
result = final_chain.invoke({'topic' : 'Adani AI Data Center in Vishakhapatnam'})

print(result)