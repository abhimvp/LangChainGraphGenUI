"""this is file where we implement langgraph chain."""

from typing import List, Optional, TypedDict
from langchain_core.messages import HumanMessage
from langgraph.graph.graph import CompiledGraph
from langgraph.graph import StateGraph


class GenerativeUIState(TypedDict, total=False):
    """
    input : HumanMessages are messages that are passed in from a human to the model.
    """

    input: HumanMessage
    result: Optional[str]
    """Plain text response if no tool was used."""
    tool_calls: Optional[List[dict]]
    """A list of parsed tool calls."""
    tool_result: Optional[dict]
    """The result of a tool call."""


def create_graph() -> CompiledGraph:
    """gives us an idea about different nodes and the flow our graph is going to take"""
    workflow = StateGraph(GenerativeUIState)

    workflow.add_node("invoke_model", invoke_model)  # type: ignore
    workflow.add_node("invoke_tools", invoke_tools)
    workflow.add_conditional_edges("invoke_model", invoke_tools_or_return)
    workflow.set_entry_point("invoke_model")
    workflow.set_finish_point("invoke_tools")

    graph = workflow.compile()
    return graph
