import subprocess
import os

def start_kafka():
    zookeeper_process = None
    kafka_process = None
    
    try:
        # Change the working directory to where the Kafka scripts are located
        os.chdir("/home/labsoe/bigdata/softs/kafka_2.13-3.7.0")
        
        # Start Zookeeper
        print("Starting Zookeeper...")
        zookeeper_process = subprocess.Popen(
            ["bin/zookeeper-server-start.sh", "config/zookeeper.properties"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("Zookeeper started successfully")
        
        # Start Kafka
        print("Starting Kafka...")
        kafka_process = subprocess.Popen(
            ["bin/kafka-server-start.sh", "config/server.properties"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("Kafka started successfully")
        
        # Wait for both processes to complete
        while True:
            if zookeeper_process.poll() is not None:
                print("Zookeeper process has terminated.")
                break
            if kafka_process.poll() is not None:
                print("Kafka process has terminated.")
                break

    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Shutting down...")
        
        # Terminate the processes if they are running
        if zookeeper_process:
            zookeeper_process.terminate()
            zookeeper_process.wait()
            print("Zookeeper process terminated.")
        if kafka_process:
            kafka_process.terminate()
            kafka_process.wait()
            print("Kafka process terminated.")
        
    except FileNotFoundError:
        print("The specified directory or file was not found.")
    except subprocess.CalledProcessError as e:
        print(f"Script execution failed with error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    try:
        os.chdir("/home/labsoe/Documents/stream/")
        result = subprocess.run(["python3", "mobile_price_streaming.py"])

    except:
        print("error")
