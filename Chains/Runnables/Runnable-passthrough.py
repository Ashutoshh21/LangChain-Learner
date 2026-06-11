from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain about the joke: {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser)
}) #outputs a dict with keywords joke, explanation -> their output, can access like result['joke']

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)
result = final_chain.invoke({'topic' : 'Naruto'})

print(result['joke'])