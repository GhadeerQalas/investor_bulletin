from amqpstorm import Connection
import os
from dotenv import load_dotenv
import json
from colorama import init, Fore

# Load the .env file
load_dotenv()
init(autoreset=True)

def send_message(message_body):
    # Create a connection object to publish events
    connection = Connection(os.environ["HOSTNAME"], os.environ["RABBITMQ_DEFAULT_USER"], os.environ["RABBITMQ_DEFAULT_PASS"])

    # Create a channel on the connection
    channel = connection.channel()

    # Declare a queue to send to
    queue_name = 'alerts.threshhold'

    # Declare the exchange
    exchange_name = 'alerts_exchange'
    # topic exchange type is used to route messages to one or many queues based on a matching pattern between the message routing key and the pattern that was used to bind a queue to an exchange
    channel.exchange.declare(exchange=exchange_name, exchange_type='topic')

    # Publish a message
    print("Publishing message....................................")
    channel.basic.publish(exchange=exchange_name, routing_key=queue_name, body=json.dumps(message_body))
    print(f"{Fore.GREEN} [x] Sent {message_body} to {queue_name} queue successfully! 🚀")

    # Close the connection
    connection.close()
