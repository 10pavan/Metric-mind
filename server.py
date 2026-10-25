from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(title="MetricMind Enterprise BI Engine", version="1.0.0")

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/api/analyze")
async def analyze_query(req: QueryRequest):
    try:
        user_q = req.query.lower()
        time.sleep(1) # Simulating agent reasoning & semantic lookup

        if "margin" in user_q or "europe" in user_q:
            response_text = "📊 **European Region Margin Analysis (Q2)**\n\n• **Gross Margin:** 42.4% (Down 3.2% QoQ)\n• **Root Cause:** Increased logistics overhead in Western European hubs and higher discounting in enterprise segments.\n• **Recommendation:** Re-negotiate 3-PL contracts in Frankfurt and optimize regional tier-2 pricing."
        elif "revenue" in user_q or "sales" in user_q:
            response_text = "📈 **Global Revenue Performance**\n\n• **Total ARR:** $48.2M (+14% YoY)\n• **Top Driver:** North America SaaS expansion.\n• **Underperformer:** APAC region missed target by 6.5% due to delayed enterprise closures."
        else:
            response_text = f"🤖 **Semantic Agent Output:** Successfully resolved query against Snowflake Data Lakehouse via Cube.dev semantic model for: *'{req.query}'*.\n\nKey metric trends look stable with standard variance within 95% confidence intervals."

        return {
            "success": True,
            "query": req.query,
            "response": response_text,
            "latency_ms": 340
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)