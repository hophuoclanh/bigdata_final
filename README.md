

<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h3 align="center">Big Data</h3>

  <p align="center">
Mobile Price Prediction and Streaming Project    <br />
    <a href="https://www.canva.com/design/DAGLKbMhFtY/SZyxvommJOsJmA8BRyAQUg/edit"><strong>Explore the slides »</strong></a>
    <br />
    <br />
  
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project implements a mobile price prediction pipeline using Apache Spark, Kafka, and Delta Lake. The pipeline involves data ingestion, real-time data processing, model storage, and orchestration with Airflow and Redis Queue.

<h2>UML Diagram</h2>

<img src="uml.png" >
Note: Worker "69" means that the task is executed at address 192.168.80.69 and so on.
## Components

# Data Ingestion

- **CSV File**: 
  - Contains the data for training, evaluating and streaming. We save it to hdfs to access easily.
  
- **Kafka Producer**: 
  - Reads data from the CSV file and sends it to a Kafka topic.
  
- **Kafka Topic**: 
  - Receives data from the Kafka producer.

# Model Storage

- **Hadoop**: 
  - Storage system for the trained model.
  
- **Logistic Regression Model**: 
  - Trained model stored in Hadoop.

# Real-Time Data Processing

- **Spark Streaming**: 
  - Reads data from Kafka, applies the model, and produces predictions.
  
- **Logistic Regression Model**: 
  - Used for predictions.
  
- **HDFS**: 
  - Storage for the model and predictions.

# Reading Delta Table

- **Delta Table in HDFS**: 
  - Stores the predictions.
  
- **Spark DataFrame**: 
  - Loads data from the Delta table for further processing.

# Orchestration

- **Airflow DAG**: 
  - Manages the execution of tasks.
  
- **Redis Queue**: 
  - Manages the queue of tasks to be executed.
  
- **Tasks**: 
  - Include starting Redis, Hadoop, Spark, Kafka, and reading the Delta table.

# Task Execution

- **RQ Worker**: 
  - Listens on the Redis at "69" queue and executes tasks.

## Workflow

1. **Start Redis**: 
   - Airflow DAG enqueues the task to start Redis.
   
2. **Start Hadoop**: 
   - Redis server enqueues the task to start Hadoop, executed by RQ Worker.
   
3. **Start Spark**: 
   - Enqueued the tasks to start Spark and execute relevant tasks including load model from HDFS and streaming and reading data before the prediction. And reading predictions to delta table.
   
4. **Start Kafka**: 
   - Enqueued and start Kafka and streaming data file.
  
5. **Read Delta**: 
   - Reads the Delta table from HDFS.

## Scripts
To ensure that the execution does not encounter any interruptions, the different machines or computers where tasks are executed will need to have the files from each folder in the repository readily available.
## Directory Structure
# `redis/`

- **`.py`**
  - Defines the Airflow DAG that orchestrates the workflow of starting services and running scripts.
# `airflow/`

- **`mobileprice.py`**
  - Defines the Airflow DAG that orchestrates the workflow of starting services and running scripts.
 
# `hadoop/`

- **`mobile_price.py`**
Contains the PySpark script for training a Logistic Regression model using data from HDFS.
tasks.py: Includes a script for starting Hadoop services.
**`test.csv`**: Sample data file for testing purposes (if applicable).
**`test.csv`**: Sample data file for training purposes (if applicable).
  **`tasks.py`**: This script starts Hadoop services using the command-line interface.

# `kafka/`

- **`mobile_price_streaming.py`**
  - Reads data from `test.csv`.
  - Sends data to the Kafka topic `mobile_price`.

- **`tasks.py`**
  - Starts Kafka and Zookeeper services using the command-line interface.


### `spark/`

- **`load1.py`**
  - Reads streaming data from Kafka.
  - Applies a pre-trained Logistic Regression model.
  - Writes predictions to the console and HDFS.
  - - **`tasks.py`**
  - Starts spark services and submit file load1.py using the command-line interface.


### `delta/`

- **`readdelta_mobile_price.py`**
  - Reads streaming data from a Delta Lake table.
  - Writes the output to the console 
  - - **`tasks.py`**
  - Submit file readdelta_mobile_price.py using the command-line interface.


## Kafka Setup

### `mobile_price_streaming.py`

- **Purpose**: Streams data from `test.csv` to Kafka.
- **Functionality**:
  - Reads rows from `test.csv`.
  - Sends each row as a JSON message to the Kafka topic `mobile_price`.
  - Introduces a random delay between messages.

### `tasks.py`

- **Purpose**: Manages the startup of Kafka and Zookeeper.
- **Functionality**:
  - Changes the directory to Kafka installation path.
  - Starts Zookeeper and Kafka servers.
  - Handles interruptions and errors.

## Spark Setup

### `load1.py`

- **Purpose**: Processes streaming data from Kafka and applies a model.
- **Functionality**:
  - Reads data from Kafka topic `mobile_price`.
  - Transforms JSON data into feature vectors.
  - Loads a pre-trained Logistic Regression model from HDFS.
  - Applies the model to the streaming data.
  - Writes predictions to both the console and HDFS in Delta format.

## Delta Lake Setup

### `readdelta_mobile_price.py`

- **Purpose**: Streams data from a Delta Lake table.
- **Functionality**:
  - Reads streaming data from the Delta Lake table at `hdfs://192.168.80.67:9000/mobile_predict`.
  - Writes the data to the console.

## Running the Pipeline

1. **Start Services**:
   - Use `tasks.py` to start Kafka and Zookeeper.

2. **Stream Data**:
   - Run `mobile_price_streaming.py` to stream data to Kafka.

3. **Process Data**:
   - Execute `load1.py` to read from Kafka, apply the model, and store results in HDFS.

4. **Read Processed Data**:
   - Run `readdelta_mobile_price.py` to read and display data from Delta Lake.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section lists the major frameworks/libraries used to bootstrap your project.

* [![Apache Spark][Spark-logo]][Spark-url]
* [![Apache Kafka][Kafka-logo]][Kafka-url]
* [![Delta Lake][Delta-logo]][Delta-url]
* [![Hadoop][Hadoop-logo]][Hadoop-url]
* [![Airflow][Airflow-logo]][Airflow-url]
* [![Redis Queue][Redis-logo]][Redis-url]

<!-- Add your logos and URLs here -->
[Spark-logo]: https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white
[Spark-url]: https://spark.apache.org/

[Kafka-logo]: https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white
[Kafka-url]: https://kafka.apache.org/

[Delta-logo]: https://img.shields.io/badge/Delta%20Lake-00A3E0?style=for-the-badge&logo=deltalake&logoColor=white
[Delta-url]: https://delta.io/

[Hadoop-logo]: https://img.shields.io/badge/Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=white
[Hadoop-url]: https://hadoop.apache.org/

[Airflow-logo]: https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white
[Airflow-url]: https://airflow.apache.org/

[Redis-logo]: https://img.shields.io/badge/Redis%20Queue-DC382D?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/topics/queues


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is a guide to get your project up and running locally. Follow these steps to set up your environment and run the project.

### Prerequisites

Ensure you have the following software installed on your machine:

* [Java](https://www.oracle.com/java/technologies/javase-downloads.html) (version 8 or higher)
* [Apache Spark](https://spark.apache.org/downloads.html)
* [Apache Kafka](https://kafka.apache.org/downloads)
* [Delta Lake](https://delta.io/downloads/)
* [Hadoop](https://hadoop.apache.org/releases.html)
* [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation.html)
* [Redis](https://redis.io/download)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/repo_name.git
    cd repo_name
    ```

2. Set up your environment:

    - **Apache Spark**:
        ```sh
        tar xvf spark-3.4.3-bin-hadoop3-scala2.13.tgz
        export SPARK_HOME=$(pwd)/spark-3.4.3-bin-hadoop3-scala2.13
        export PATH=$PATH:$SPARK_HOME/bin
        ```

    - **Apache Kafka**:
        ```sh
        tar -xzf kafka_2.13-2.8.0.tgz
        export KAFKA_HOME=$(pwd)/kafka_2.13-2.8.0
        export PATH=$PATH:$KAFKA_HOME/bin
        ```

    - **Delta Lake**:
        Add the Delta Lake package to your Spark configuration:
        ```sh
        export SPARK_OPTS="--packages io.delta:delta-core_2.12:1.0.0"
        ```

    - **Hadoop**:
        ```sh
        tar -xzf hadoop-3.3.1.tar.gz
        export HADOOP_HOME=$(pwd)/hadoop-3.3.1
        export PATH=$PATH:$HADOOP_HOME/bin
        ```

    - **Apache Airflow**:
        ```sh
        pip install apache-airflow
        airflow db init
        airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
        ```

    - **Redis**:
        ```sh
        wget http://download.redis.io/redis-stable.tar.gz
        tar xvzf redis-stable.tar.gz
        cd redis-stable
        make
        ```

3. Start the services:

    - **Apache Kafka**:
        ```sh
        zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
        kafka-server-start.sh $KAFKA_HOME/config/server.properties &
        ```

    - **Redis**:
        ```sh
        redis-server &
        ```

    - **Apache Airflow**:
        ```sh
        airflow webserver --port 8080 &
        airflow scheduler &
        ```

### Running the Project

1. Compile and package your code:
    ```sh
    ./build.sh
    ```

2. Submit your Spark job:
    ```sh
    spark-submit --class com.yourcompany.YourApp --master local[4] target/your-app-1.0-SNAPSHOT.jar
    ```

3. Monitor your Airflow DAGs by accessing the Airflow web interface at `http://localhost:8080`.

4. Ensure Kafka and Redis are running properly by checking their respective logs and dashboards.

### Usage

Provide examples and explanations for how to use your project. Consider including code snippets or step-by-step instructions.

```sh
./run.
```


<p align="right">(<a href="#readme-top">back to top</a>)</p




### Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project (`https://github.com/hophuoclanh/bigdata_final/fork`)
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- CONTACT -->
## Contact

Ho Phuoc Lanh -
Pham Tran Thi Thu Ngan  

Project Link: [https://github.com/hophuoclanh/bigdata_final/edit](https://github.com/hophuoclanh/bigdata_final/edit)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

