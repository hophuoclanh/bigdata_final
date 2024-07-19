import os
import subprocess
import threading

def start_spark():
    try:
        os.chdir("/home/phamtranthithungan/Downloads/spark-3.5.1-bin-hadoop3-scala2.13")
        try:
            subprocess.run("./sbin/start-all.sh", check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error starting Spark: {e}")
        print("Read model")
        # Run the spark-submit command using subprocess
        spark_submit_command = [
            "./bin/spark-submit",
            "--packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:3.4.3,io.delta:delta-spark_2.13:3.2.0,org.apache.spark:spark-sql_2.12:3.4.0",
            "/home/phamtranthithungan/PycharmProjects/CS411/load1.py"
        ]
        # Run the command
        subprocess.run(spark_submit_command, check=True)
        print("load model")
        print("spark on")
    except Exception as e:
        print(f"Error in start_spark: {e}")

def start_and_timeout():
    start_spark_thread = threading.Thread(target=start_spark)
    start_spark_thread.start()
    start_spark_thread.join(timeout=120)  # Wait for 2 minutes (120 seconds)

def read_delta():
    try:
        os.chdir("/home/phamtranthithungan/Downloads/spark-3.5.1-bin-hadoop3-scala2.13")
        try:
            subprocess.run("./sbin/start-all.sh", check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error starting Spark: {e}")
        print("Read delta")
        spark_read_delta_command = [
            "./bin/spark-submit",
            "--packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:3.4.3,io.delta:delta-spark_2.13:3.2.0,org.apache.spark:spark-sql_2.12:3.4.0",
            "/home/phamtranthithungan/PycharmProjects/CS411/readdelta_mobile_price.py"
        ]
        subprocess.run(spark_read_delta_command, check=True)
        print("load model")
        print("spark on")
    except Exception as e:
        print(f"Error in read_delta: {e}")

# Example usage
start_and_timeout()
read_delta()
