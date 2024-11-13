from fastapi import APIRouter, Depends, Header, HTTPException

router = APIRouter()

@router.get("/active_alerts", tags=["alerts", "active alerts", "active"])
async def get_active_alerts(user_id:str):

    return []