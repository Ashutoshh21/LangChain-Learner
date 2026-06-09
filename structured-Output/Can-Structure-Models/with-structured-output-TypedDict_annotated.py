from langchain_groq import ChatGroq
from dotenv import load_dotenv

from typing import TypedDict, Literal, Optional, Annotated #annotation is done to even further specify the tasks, Like here to tell LLM what exactly we mean by summary and what sentiments? i.e. classify into positive and negetive, This is done because sometimes the LLMs are not smart enough or able to capture the task to be done with the help of keys

load_dotenv()

model = ChatGroq(model='llama-3.3-70b-versatile')

#defining the schema for output data format
class review(TypedDict):
    summary : Annotated[str, "Return a summary of the user review "]
    sentiment : Annotated[Literal['pos','neg'], "The overall sentiment of the review i.e. positive or negetive "] # To specify if we want the key to be a particular name, else we can do basic like -> Anootated[str, "return the overall senti..."]
    topics : Annotated[Optional[list[str]], "Return the key components mentioned in the review"] #optinal means the key can be empty if no relevent thing found in material matching it

structured_model = model.with_structured_output(review)

result = structured_model.invoke("The hair dryer's looks is okayish but the battery drains too fast and the plastic body heats which might make it faulty sooner. Won't recommend for this price range. ")

print(result)