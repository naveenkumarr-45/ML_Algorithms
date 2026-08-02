from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
st.title("Naveen's ChatBot")
input_txt=st.text_input("Enter your question here:")
prompt=ChatPromptTemplate.from_messages(
    [("system","you are a helpful AI assistant,your name is Naveen's Assistant"),
     ("user",'question: {query}')]
)
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain= prompt|llm|output_parser
if input_txt:
    st.write(chain.invoke({"query":input_txt})) 
