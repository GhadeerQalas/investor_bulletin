""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_dal import create_rule, get_all_alerts

def create_new_alert(rule: AlertCreate, session ):
     return create_rule(symbols=rule, session=session)

def get_alerts(session):
    return get_all_alerts(session=session)
