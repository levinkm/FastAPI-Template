from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
import json
from decouple import config
import socket

default = json.loads(config("default"))

config = default
config.update(
    {
        "client.id": socket.gethostname(),
        "key.serializer": StringSerializer("utf_8"),
        # "value.serializer": JsonSerializer(),
    }
)

topic = "accounts"

producer = SerializingProducer(config)

def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush()."""
    if err is not None:
        print("Message delivery failed: {}".format(err))
        return False
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))
        return True

def produce(key, value,topic="accounts", delivery_report=delivery_report):
    """
    Produce a single message to confluent kafka topic
    """
    print(f"Producing message to topic {topic} with key {key} and value {value}")

    producer.produce(
        topic,
        key=key,
        value=value,
        on_delivery=delivery_report,
    )

    producer.flush()


