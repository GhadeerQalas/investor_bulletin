""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_model import Alerts
from colorama import init, Fore

init(autoreset=True)

def create_rule(symbols: AlertCreate, session):
    for symbol in symbols:
        alert = Alerts(symbol=symbol)
        existing_alert = session.query(Alerts).filter_by(symbol=symbol).first()
        if existing_alert is None:
            session.add(alert)
        else:
            print(f"{Fore.YELLOW} [!] Alert for {symbol} already exists")

    session.commit()

def get_all_alerts(session):
    return session.query(Alerts).all()
