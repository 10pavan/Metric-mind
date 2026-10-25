# ui.py
import streamlit as st
import sys
import os

# Path setup
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from agent.orchestrator import MetricMindAgent

# Page configuration
st.set_page_config(page_title="MetricMind BI", page_icon="📊", layout="centered")

st.title("📊 MetricMind: Agentic Semantic BI Engine")
st.markdown("Ask financial and sales questions powered by a governed enterprise semantic layer.")

# Initialize agent
@st.cache_resource
def load_agent():
    return MetricMindAgent()

agent = load_agent()

# Chat input from user
user_query = st.text_input("Enter your question (e.g., Why did European margins drop in Q2?):")

if st.button("Analyze"):
    if user_query.strip():
        with st.spinner("Agent is analyzing semantic layers..."):
            response = agent.run(user_query)
        
        st.success("Analysis Complete!")
        st.markdown(f"### **Response:**")
        st.write(response)
    else:
        st.warning("Please enter a valid question.")