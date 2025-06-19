from langgraph.graph import StateGraph, END, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from .summarizer import summarize_trip
from .tools import get_attractions_and_activities, get_hotels_and_transport, get_weather_forecast, generate_itinerary

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
tools = [get_attractions_and_activities, get_weather_forecast, get_hotels_and_transport, generate_itinerary, summarize_trip,  web_search]  # Add others if needed
llm_with_tools = llm.bind_tools(tools)

def llm_decision_node(state):
    user_question = state["messages"]
    return {"messages": [llm_with_tools.invoke(user_question)]}

def build_graph():
    builder = StateGraph(MessagesState)
    builder.add_node("llm_decision_step", llm_decision_node)
    builder.add_node("tools", ToolNode(tools))
    builder.set_entry_point("llm_decision_step")
    builder.add_edge("llm_decision_step", "tools")
    builder.add_edge("tools", "llm_decision_step")
    builder.set_finish_point("llm_decision_step")
    return builder.compile()