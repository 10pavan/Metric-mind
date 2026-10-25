# semantic/metrics.py
import pandas as pd
import os

def load_data():
    # Load mock sales data safely relative to this file's location
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'mock_sales.csv')
    return pd.read_csv(data_path)

def get_regional_margin(region_name: str, target_quarter: str):
    """
    Calculates the exact margin for a region in a specific quarter.
    Formula: (Revenue - Cost) / Revenue
    """
    df = load_data()
    filtered = df[(df['region'].str.lower() == region_name.lower()) & 
                  (df['quarter'].str.lower() == target_quarter.lower())]
    
    if filtered.empty:
        return None, "No data found for this region/quarter combination."
    
    total_revenue = filtered['revenue'].sum()
    total_cost = filtered['cost'].sum()
    
    if total_revenue == 0:
        return 0.0, "Revenue is zero, cannot compute margin."
        
    margin = (total_revenue - total_cost) / total_revenue
    return round(margin * 100, 2), None