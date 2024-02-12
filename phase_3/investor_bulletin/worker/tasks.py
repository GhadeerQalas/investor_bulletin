from resources.market.market_service import MarketService
from resources.alert_rules.alert_rule_service import get_all_rule
from db.models.models import session
from core.messaging import send_message
from worker.app import app
import json
@app.task
def fetch_data_and_check_rules():
    try:
        user_rules = get_all_rule(session)
        for rule in user_rules:
            print(f'Fetching data for {rule.symbol}...')
            print(f'rule.threshold_price: {rule.threshold_price}')
            market_data = MarketService().get_market_data([rule.symbol])
            if market_data[0]["symbol"] == rule.symbol and market_data[0]["price"] is not None and market_data[0]["price"] != "" and market_data[0]["price"] == rule.threshold_price:
                publish_threshold_alert(rule.symbol)
    except Exception as e:
        print(f'Error occurred while fetching data for {rule.symbol}: {e}')

def publish_threshold_alert(rule):
    # Publish a message
    print(f"Publishing threshold alert for {rule}...")
    message_body = {"eventName": "THRESHOLD_ALERT", "eventData": {"symbol": [rule]}}
    print(f"Published threshold alert for {rule} successfully!")
    send_message(message_body)
