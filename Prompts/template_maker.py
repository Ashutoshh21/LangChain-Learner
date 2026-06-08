from langchain_core.prompts import PromptTemplate
import json
from langchain_core.load import dumps 


template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)


# 1. Convert the prompt object into a standardized JSON string
prompt_json_string = dumps(template, pretty=True)

# 2. Use standard Python tools to write it to your file
with open("template.json", "w") as file:
    file.write(prompt_json_string)

"""
An old legacy way to do it

template.save('template.json') 

"""
