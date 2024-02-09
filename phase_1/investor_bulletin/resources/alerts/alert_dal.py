""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_model import Alerts

def create_rule(symbols: AlertCreate, session):
    symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]

    for symbol in symbols:
        alert = Alerts(symbol=symbol)
        session.add(alert)

    session.commit()

def get_all_alerts(session):
    return session.query(Alerts).all()
