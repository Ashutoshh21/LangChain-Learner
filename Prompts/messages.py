from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')

messages = [
    SystemMessage(content='You are the former President of United States of America Harry S. Truman, Now kindly answer based on what you know. '),
    HumanMessage(content = 'What happened to the Alien UFO recovered from the debris in roswell incident? Why did the Military retract its original message? ')
]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))

print(result.content)