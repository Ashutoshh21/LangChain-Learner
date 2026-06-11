from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Tell me a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain this joke, {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic' : 'Chess'}))