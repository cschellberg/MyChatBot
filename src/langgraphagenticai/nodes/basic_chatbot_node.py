from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """

    """
    def __init__(self, model):
        self.llm = model

    def process(self, state:State):
        """
        Process the input from the: user and generate a response using the LLM.
        """
        result=self.llm.invoke(state['messages'])
        print(f"BasicChatbotNode process result: {result}")
        print(f"State messages: {state['messages']}")
        return {"messages":[result.content]}