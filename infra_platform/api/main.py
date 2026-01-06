from fastapi import FastAPI, HTTPException
from infra_platform.core.decision_engine import get_decision

app = FastAPI(title="EKS Decision Engine API")


@app.get("/decision/{profile_name}")
def get_decision_by_profile(profile_name: str):
    try:
        return {
            "profile": profile_name,
            "decision": get_decision(profile_name),
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

