from fastapi import APIRouter, HTTPException
from db.models.models import session
from resources.alert_rules.alert_rule_service import create_new_rule, update_rule, delete_rule, get_all_rule
from resources.alerts.alert_service import get_all_alerts
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from fastapi.encoders import jsonable_encoder

router = APIRouter()



@router.post("/alert-rules")
def create_alert_rule(alert_rule: AlertRuleCreate):
    try:
        create_new_rule(alert_rule, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Alert rule created successfully"}

@router.patch("/alert-rules/{id}")
def update_alert_rule(id: int, alert_rule: AlertRuleUpdate):
    try:
        if not any(alert_rule):
            return HTTPException(status_code=400, detail="At least one field must be provided")
        update_rule(id, alert_rule, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Alert rule updated successfully"}

@router.delete("/alert-rules/{id}")
def delete_alert_rule(id: int):
    try:
        delete_rule(id, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Alert rule deleted successfully"}

@router.get("/alert-rules")
def get_alerts_rules():
    try:
        all_rules = get_all_rule(session=session)
        return {"message": jsonable_encoder(all_rules)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/alerts")
def alerts():
    try:
        all_rules = get_all_alerts(session=session)
        return {"message": all_rules}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
