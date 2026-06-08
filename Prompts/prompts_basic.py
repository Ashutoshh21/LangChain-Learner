from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.load import loads

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')
st.header('Research Summary Tool')

ppr_input = st.selectbox("Choose from the Research papers", [
    'Attention is all you Need',
     "BERT: Pre-training of Deep Bidirectional Transformers", 
    "GPT-3: Language Models are Few-Shot Learners", 
    "Diffusion Models Beat GANs on Image Synthesis"
])
len_input = st.selectbox('Select the length of summary', [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)"
] )

style_input = st.selectbox("Select Explaination Style ", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

with open('template.json', 'r') as file:
    prompt_json_string = file.read()

template = loads(prompt_json_string)


if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        'paper_input' : ppr_input,
        'style_input' : style_input,
        'length_input' : len_input 
    })
    st.write(result.content)
