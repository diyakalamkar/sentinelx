from pydantic import BaseModel

class LogEntry(BaseModel):
    agent: str      # "red" or "blue"
    action: str     # e.g., "scan", "exploit", "patch"
    details: str    # any notes or explanation
