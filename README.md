

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Big Data</h3>

  <p align="center">
Mobile Price Prediction and Streaming Project    <br />
    <a href="https://www.canva.com/design/DAGLKbMhFtY/SZyxvommJOsJmA8BRyAQUg/edit"><strong>Explore the docs »</strong></a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project implements a mobile price prediction pipeline using Apache Spark, Kafka, and Delta Lake. The pipeline involves data ingestion, real-time data processing, model storage, and orchestration with Airflow and Redis Queue.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2>UML Diagram</h2>


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
# Example command to run your project
./run.sh


<p align="right">(<a href="#readme-top">back to top</a>)</p>







<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project (`https://github.com/hophuoclanh/bigdata_final/fork`)
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ho Phuoc Lanh -
Pham Tran Thi Thu Ngan  

Project Link: [https://github.com/hophuoclanh/bigdata_final/edit](https://github.com/hophuoclanh/bigdata_final/edit)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

