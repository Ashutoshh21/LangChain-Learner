from langchain_groq import ChatGroq
from dotenv import load_dotenv

from typing import TypedDict

load_dotenv()

model = ChatGroq(model='llama-3.3-70b-versatile')

#defining the schema for output data format
class review(TypedDict):
    summary : str
    sentiment : str 


#Both works fine , doesn't throw error since no data validation applied, only type suggestions
"""
dict1 = {'summary' : "i know nothing don't ask me", 'sentiment' : 23}
dict2 = {'summary' : "I know everything ask me please", 'sentiment' : 'Positive'}

new_review1 = review(**dict1)
new_review2 = review(**dict2)

"""


structured_model = model.with_structured_output(review)

result = structured_model.invoke("The hair dryer's looks is okayish but the battery drains too fast and the body heats which might make it faulty sooner. Won't recommend for this price range. ")

print(type(result))
print(result)

