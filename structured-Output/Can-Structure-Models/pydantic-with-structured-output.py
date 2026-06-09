from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional


load_dotenv()

model = ChatGroq(model='llama-3.3-70b-versatile')

#defining the schema for output data format
class review(BaseModel):
    key_themes : list[str] = Field(description='List of key components or key themes mentioned in the review')
    summary : str = Field(description='A short summary of the whole review ')
    sentiment : Literal['pos','neg'] = Field(description='Overall sentiment of the review either positive or Negetive') 
    email : Optional[EmailStr] = Field(default = None, description='Email of the reviewer in case it is given')


structured_model = model.with_structured_output(review)

result = structured_model.invoke("The hair dryer's looks is okayish but the battery drains too fast and the body heats which might make it faulty sooner. Won't recommend for this price range. ")

print(type(result))
print(result)
