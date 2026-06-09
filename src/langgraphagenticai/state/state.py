from typing import List

from pydantic import BaseModel
from sqlalchemy.sql.annotation import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represent the structure of the statue used in the graph.
    """
    messages:Annotated[List, add_messages]
