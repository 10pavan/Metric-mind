# governance/validator.py

ALLOWED_METRICS = ["margin", "revenue", "cost", "churn_rate"]

def validate_metric_request(metric_name: str) -> bool:
    """
    Validates if the requested metric is approved by corporate governance.
    Prevents unauthorized or hallucinated metrics.
    """
    if not metric_name or metric_name.lower() not in ALLOWED_METRICS:
        raise ValueError(f"Governance Error: Metric '{metric_name}' is not authorized or doesn't exist.")
    return True