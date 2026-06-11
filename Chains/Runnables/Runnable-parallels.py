from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a short twitter post on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'write a short linkedin post on, {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'twitter' : RunnableSequence(prompt1, model, parser),
    'linkedin' : RunnableSequence(prompt2, model, parser)
}) #outputs a dict with keywords same, values -> their output, can access like result['linkedin']

print(parallel_chain.invoke({'topic' : 'RAG'}))