import streamlit as st


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message


    def display_result_on_ui(self):
        """
        Displays the result in the Streamlit app.

        """
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message
        print(f"Displaying results for use case: {usecase} with user message: {user_message}")
        if usecase=="Basic Chatbot":
            messages={'messages':[("user",user_message)]}
            print(f"Streaming graph with messages: {messages}")
            config = {"configurable": {"thread_id": "loopless_session_888"}}
            events= graph.stream(messages)
            print(f"Received events: {events}")
            for event in events:
                print(f"Processing event: {event}")
                for value in event.values():
                    print(f"value is {value}")
                    if "messages" in value and value["messages"]:
                        # Get the last message object in the list
                        last_msg = value["messages"][-1]
                        with st.chat_message("assistant"):
                            st.write(last_msg)
