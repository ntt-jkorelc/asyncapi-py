from .base import BaseApi


class Bindings(BaseApi):
    http: HTTPServerBinding
    ws: WebSocketsServerBinding
    kafka: KafkaServerBinding
    anypointmq: AnypointMQServerBinding
    amqp: AMQPServerBinding
    amqp1: AMQP1ServerBinding
    mqtt: MQTTServerBinding
    mqtt5: MQTT5ServerBinding
    nats: NATSServerBinding
    jms: JMSServerBinding
    sns: SNSServerBinding
    solace: SolaceServerBinding
    sqs: SQSServerBinding
    stomp: StompServerBinding
    redis: RedisServerBinding
    mercure: MercureServerBinding
    ibmmq: IBMMQServerBinding
    googlepubsub: GooglePubSubServerBinding
    pulsar: PulsarServerBinding