# app.py
import sys
import os

# Root directory ko explicitly Python path mein sabse upar add kar rahe hain
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from agent.orchestrator import MetricMindAgent
from governance.validator import validate_metric_request

def main():
    print("==================================================")
    print("🚀 Initializing MetricMind: Agentic Semantic BI Engine")
    print("==================================================")
    
    # 1. Test Governance Validation
    try:
        validate_metric_request("margin")
        print(" [Governance Check] Metric 'margin' is approved.")
    except Exception as e:
        print(f" [Governance Check Failed] {e}")

    # 2. Initialize Agent
    agent = MetricMindAgent()
    
    # 3. Run Sample Query
    sample_query = "Why did our European margins drop in Q2?"
    print(f"\n User Query: '{sample_query}'")
    print("-" * 50)
    
    response = agent.run(sample_query)
    print("\n MetricMind Response:")
    print(response)
    print("==================================================")

if __name__ == "__main__":
    main()