import streamlit as st

from src.langgraphagenticai.LLM.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI Streamlit application. This function initializes the UI components and starts the Streamlit app.
    """
    ui_loader = LoadStreamlitUI()
    user_input = ui_loader.load_streamlit_ui()

    if not user_input:
        st.error("Error loading user input. Please check the UI configuration.")
        return

    user_message = st.text_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()
            if not model:
                st.error("LLM model could not be initialized. Please check your API key and model selection.")
                return
            usecase=user_input.get('selected_usecase')
            if not usecase:
                st.error("Use case not selected. Please select a use case from the sidebar.")
                return
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error building the graph: {e}")
                return
        except Exception as e:
            st.error(f"An error occurred while processing your message: {e}")
            return

