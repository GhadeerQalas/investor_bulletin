from amqpstorm import Connection
import os
from dotenv import load_dotenv
import json

# Load the .env file
load_dotenv()

# Create a connection object to publish events
connection = Connection(os.environ["HOSTNAME"], os.environ["RABBITMQ_DEFAULT_USER"], os.environ["RABBITMQ_DEFAULT_PASS"])

# Create a channel on the connection
channel = connection.channel()

# Declare a queue to send to
queue_name = 'alerts_queue'
channel.queue.declare(queue_name)

# Publish a message
message_body = { "eventName": "THRESHOLD_ALERT",
                "eventData": {
                "symbol": ["DELL"]
            },
        }
channel.basic.publish(exchange='', routing_key=queue_name, body=json.dumps(message_body))

print(f" [x] Sent '{message_body}'")

# Close the connection
connection.close()
