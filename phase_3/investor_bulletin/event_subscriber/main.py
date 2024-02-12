import pika
import os
from dotenv import load_dotenv
from colorama import init, Fore
import json
from resources.alerts.alert_service import create_new_alert
from db.models.models import session

# Load the .env file
load_dotenv()
init(autoreset=True)

def init_subscriber():
    # Define your connection parameters
    parameters = pika.ConnectionParameters(os.environ["HOSTNAME"])

    # Create a connection
    connection = pika.BlockingConnection(parameters)

    return connection

def on_event(ch, method, properties, body):
      print(f"{Fore.RED} [!] ALERT: {body}")
      if body is None:
            return
      data = json.loads(body)
      if data["eventName"] == "THRESHOLD_ALERT":
            print(f"{Fore.RED} [!] ALERT: {data['eventData']}")
            if 'symbol' not in data['eventData']:
                  return
            symbols = data['eventData']['symbol']
            create_new_alert(symbols, session=session)

if __name__ == "__main__":
    print(f"{Fore.YELLOW}        *** *** Welcome to Alert Serivce 🚀 *** ***")
    print(f"{Fore.GREEN} [*] Waiting for messages. To exit press CTRL+C 🥱")
    connection = init_subscriber()
    channel = connection.channel()

    # Declare the exchange and queue
    exchange_name = 'alerts_exchange'
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    # Bind the queue to the exchange
    binding_key = 'alerts.*'
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=binding_key)

    channel.basic_consume(queue=queue_name, on_message_callback=on_event, auto_ack=True)

    # Start consuming
    channel.start_consuming()
