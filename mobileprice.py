from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define the DAG
with DAG(
    "mobileprice",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple DAG to run mobile price scripts",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 7, 16),
    catchup=False,
    tags=["example"],
) as dag:

    start_redis = BashOperator(
        task_id="start_redis",
        bash_command="sudo /usr/bin/redis-server /etc/redis/redis.conf",
    )

    start_hadoop = BashOperator(
        task_id="start_hadoop",
        bash_command="python3 /home/labsoe/Documents/mobile_price/start_hadoop.py",
    )

    start_spark = BashOperator(
        task_id="start_spark",
        bash_command="python3 /home/labsoe/Documents/mobile_price/start_spark.py",
    )

    start_kafka = BashOperator(
        task_id="start_kafka",
        bash_command="python3 /home/labsoe/Documents/mobile_price/start_kafka.py",
    )

    read_delta = BashOperator(
        task_id="read_delta",
        bash_command="python3 /home/labsoe/Documents/mobile_price/read_delta.py",
    )

    # Define task dependencies
    start_redis >> start_hadoop >> start_spark >> start_kafka >> read_delta
