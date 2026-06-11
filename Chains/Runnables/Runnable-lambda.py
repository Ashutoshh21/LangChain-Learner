from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)
joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(lambda x: len(x.split()))
}) #outputs a dict with keywords joke, word_count -> their output, can access like result['joke']

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)
result = final_chain.invoke({'topic' : 'Naruto'})

print(result)