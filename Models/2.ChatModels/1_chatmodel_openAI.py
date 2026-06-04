from langchain_groq import ChatGroq #from langchain_openai import ChatOpenAI
                                    #from lanchain_anthropic import ChatAnthropic
                                    #from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# 1. Load the API key from your hidden .env file into temporary memory
load_dotenv()

# 2. Initialize the free cloud model
model = ChatGroq(model = 'openai/gpt-oss-20b', temperature = 1.5, max_tokens = 200) #ChatOpenAI(model = 'their model', temp.., max_completion_tokens = ..) for ChatOpenAI

# 3. Format your query using standard LangChain message blocks
messages = [
    HumanMessage(content = "write a poem on chess")
]

# 4. Send the prompt over the cloud and print the live response
result = model.invoke(messages) 
print(result.content) #only printing result will show many metadata

