import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        print(f"Initializing GroqLLM with user controls: {self.user_controls_input}")

    def get_llm_model(self):
        try:
            groq_api_key= self.user_controls_input["API_KEY"]
            selected_groq_model= self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' :
                st.error("Please enter the Groq API KEY")
                return None
            else:
                print(f"groq_api_key {groq_api_key}")
                llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)
                return llm
        except Exception as e:
            print(f"Error initializing Groq LLM: {e}")
            raise ValueError(f"Error initializing Groq LLM: {e}")
