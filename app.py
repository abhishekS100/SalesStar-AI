from fastapi import FastAPI
from models.lead import Lead
from services.dynamodb import save_lead, get_all_leads
from agent.agent import SalesAgent

app = FastAPI()
agent = SalesAgent()

@app.post("/lead")
def create_lead(lead: Lead):
    saved = save_lead(lead.dict())
    return saved

@app.get("/leads")
def list_leads():
    return get_all_leads()

@app.post("/run-agent/{lead_id}")
def run_agent(lead_id: str):
    leads = get_all_leads()
    lead = next(l for l in leads if l["id"] == lead_id)

    result = agent.run(lead)
    return result