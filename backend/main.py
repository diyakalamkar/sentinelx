from fastapi import FastAPI, Request
from database import supabase
from models import LogEntry

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SentinelX Backend Running"}

@app.post("/log")
async def log_event(request: Request, entry: LogEntry):
    ip = request.headers.get('x-forwarded-for') or request.client.host
    payload = {
        "ip": ip,
        "agent": entry.agent,
        "action": entry.action,
        "details": entry.details,
    }
    supabase.table("logs").insert(payload).execute()
    return {"status": "logged"}
