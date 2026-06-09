from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.state.state import State


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder =StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph with the following structure:
        User -> LLM -> Response
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot",END)
        return self.graph_builder

    def setup_graph(self, use_case):
        """
        Set up the graph based on the selected use case. Currently, only a basic chatbot use case is implemented.
        """
        memory=MemorySaver()
        if use_case == "Basic Chatbot":
            return self.basic_chatbot_build_graph().compile()
        else:
            raise ValueError(f"Use case '{use_case}' is not implemented.")

