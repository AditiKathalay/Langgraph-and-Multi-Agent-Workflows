import sys
import os
import streamlit as st
from langchain_core.messages import HumanMessage
from app.langgraph_config import build_graph

from dotenv import load_dotenv
load_dotenv()

react_graph = build_graph()

st.title("🧳 AI Travel Planner")

user_input = st.text_input("Enter your travel plan (e.g., I'm going to Delhi from July 1 to July 3):")

if user_input:
    with st.spinner("Planning your trip..."):
        result = react_graph.invoke({"messages": [HumanMessage(user_input)]})
        outputs = [msg.content for msg in result["messages"] if msg.type == "ai"]
        st.markdown(outputs[-1])