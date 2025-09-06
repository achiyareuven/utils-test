# dal/kafka_dal.py
from kafka import KafkaProducer, KafkaConsumer
import json, os

class KafkaDAL:
    def __init__(self, bootstrap_servers=None, topic=None, group_id=None):
        self.bootstrap_servers = bootstrap_servers or os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
        self.topic = topic or os.getenv("KAFKA_TOPIC", "test-topic")
        self.group_id = group_id or os.getenv("KAFKA_GROUP", "group1")

        # Producer
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8")
        )

    def send(self, message: dict):
        self.producer.send(self.topic, message)
        self.producer.flush()

    def consume(self, auto_offset_reset="earliest"):
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            auto_offset_reset=auto_offset_reset,
            value_deserializer=lambda m: json.loads(m.decode("utf-8"))
        )
        for msg in consumer:
            yield msg.value

    def close(self):
        self.producer.close()
