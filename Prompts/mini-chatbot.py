from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

chat_history = [
    SystemMessage('You are a helpful AI assistant. ')
]

while True:
    user_input = input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print(f'AI : {result.content}')

print("\n\n", chat_history)