from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
]) #simple modern way, as the SystemMessage(content = ..) way for this is a mess and a drawback for as-it-is input variable stored in template


prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)