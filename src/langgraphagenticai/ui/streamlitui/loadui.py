import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}


    def load_streamlit_ui(self):
        st.set_page_config(page_title="xx "+self.config.get_page_title(), layout="wide")
        st.header("Schellberg's "+self.config.get_page_title())
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)
            if self.user_controls['selected_llm'] == "Groq":
                model_options= self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", model_options)
                self.user_controls['API_KEY'] = st.text_input("API Key", type="password")
                if not self.user_controls["API_KEY"]:
                    st.warning("Please enter your Groq API Key to use Groq LLM.")

            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", usecase_options)
            print(f"User controls: {self.user_controls}")
        return self.user_controls