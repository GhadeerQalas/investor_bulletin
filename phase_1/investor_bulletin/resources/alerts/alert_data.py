from resources.alerts.alert_service import create_new_alert
from db.models.models import session

symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]
create_new_alert(symbols, session=session)
