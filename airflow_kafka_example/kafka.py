from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

KAFKA_CONF = {
    'KAFKA_TOPIC':'data_topic',
    'KAFKA_BOOTSTRAP_SERVERS':'mykafka:9092',
}

def create_topic(conf):
    from confluent_kafka.admin import AdminClient, NewTopic

    a = AdminClient({'bootstrap.servers': conf['KAFKA_BOOTSTRAP_SERVERS']})
    topic = NewTopic(conf['KAFKA_TOPIC'], num_partitions=3, replication_factor=1)
    a.create_topics([topic])


def consume_from_kafka(conf):
    from confluent_kafka import Consumer

    c = Consumer({
        'bootstrap.servers': conf['KAFKA_BOOTSTRAP_SERVERS'],
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe([conf['KAFKA_TOPIC']])

    for _ in range(10):
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()

def produce_to_kafka(conf):
    from confluent_kafka import Producer

    p = Producer({'bootstrap.servers': conf['KAFKA_BOOTSTRAP_SERVERS']})

    def delivery_report(err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    for data in ["DATA1", "DATA2"]:
        # Trigger any available delivery report callbacks from previous produce() calls
        p.poll(0)

        # Asynchronously produce a message. The delivery report callback will
        # be triggered from the call to poll() above, or flush() below, when the
        # message has been successfully delivered or failed permanently.
        p.produce(conf['KAFKA_TOPIC'], data.encode('utf-8'), callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    p.flush()

# Define the default arguments for the Airflow DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
dag = DAG(
    'kafka_example_1',
    default_args=default_args,
    description='A simple example DAG to consume messages from Kafka',
    schedule="@daily"
)

create_topic_task = PythonVirtualenvOperator(
    task_id='create_topic',
    python_callable=create_topic,
    requirements=["confluent-kafka==2.3.0"],
    op_kwargs={'conf': KAFKA_CONF},
    dag=dag,
)

produce_task = PythonVirtualenvOperator(
    task_id='produce_to_kafka',
    python_callable=produce_to_kafka,
    requirements=["confluent-kafka==2.3.0"],
    op_kwargs={'conf': KAFKA_CONF},
    dag=dag,
)

consume_task = PythonVirtualenvOperator(
    task_id='consume_from_kafka',
    python_callable=consume_from_kafka,
    requirements=["confluent-kafka==2.3.0"],
    op_kwargs={'conf': KAFKA_CONF},
    dag=dag,
)

create_topic_task >> produce_task >> consume_task
