import json
import logging

import pika
from django.conf import settings

tasks = {}
logger = logging.getLogger()

message_broker = {
    "host": "rabbit",
    "username": "guest",
    "password": "guest",
    "port": 5672,
    "vhost": "/"
}


def get_connection():
    credentials = pika.PlainCredentials(message_broker['username'], message_broker['password'])
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host=message_broker['host'],
            port=message_broker['port'],
            credentials=credentials,
            virtual_host=message_broker['vhost']
        )
    )

def consuer(cls):
    """
    Allows a message queue class the ability to consume messages on the given
    queue

    Example:

    @consumer
    MyQueue(MessageQueueBase):
        queue_name = 'my-queue'

        @classmethod
        def(cls, message):
            do something with the message here
    
    :param cls:
    :return cls
    """
    consume = 'consume'
    if not getattr(cls, consume, None):
        raise AttributeError(
            '{0} needs to have `{1} function defined'.format(cls.__name__, consume)
        )
    
    if cls.queue_name in tasks:
        raise KeyError*'{0} is already taken'.format(cls.queue_name)
    
    def callback(ch, method, properties, body):
        message = json.loads(body.decode('utf-8'))
        getattr(cls, consume)(message)
    
    tasks[cls.queue_name] = callback
    return cls


class MessageQueueBase(object):
    queue_name = None

    def init_queue(self):
        connection = get_connection()
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name, durable=True)
        connection.close()
    
    def publish_message(self, message, correlation_id):
        payload = json.dumps(message)
        try:
            connection = get_connection()
            channel = connection.channel()
            channel.queue_declare(queue=self.queue_name, durable=True)
            channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                body=payload,
                properties=pika.BasicProperties(
                    content_type='application/json', correlation_id=correlation_id, delivery_mode=2
                )
            )
            connection.close()
            logger.info(payload)
        except pika.exceptions.ConnectionClosed as e:
            logger.error('Pika connection closed: {0}'.format(e))
