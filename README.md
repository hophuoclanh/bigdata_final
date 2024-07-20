

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



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
