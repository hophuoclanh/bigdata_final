from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, udf
from pyspark.sql.types import StringType, IntegerType, FloatType, StructType, StructField
from pyspark.ml.linalg import DenseVector, VectorUDT
from pyspark.ml.classification import LogisticRegressionModel

# Initialize Spark session
spark = SparkSession.builder.appName("final_report") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

# Kafka Configuration
kafka_bootstrap_servers = "192.168.80.83:9092"
kafka_topic = "mobile_price"

# Load the saved model from HDFS
model_path = "hdfs://192.168.80.75:9000/mobile_price_model"
model = LogisticRegressionModel.load(model_path)

# Read from Kafka
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "latest") \
    .option("failOnDataLoss", False) \
    .load() \
    .selectExpr("CAST(value AS STRING)")

# UDF to parse JSON and create a feature vector
@udf(VectorUDT())
def parse_json_to_vector(value):
    import json
    data = json.loads(value)
    fields = [
        data.get("battery_power", 0),
        data.get("blue", 0),
        data.get("clock_speed", 0.0),
        data.get("dual_sim", 0),
        data.get("fc", 0),
        data.get("four_g", 0),
        data.get("int_memory", 0),
        data.get("m_dep", 0.0),
        data.get("mobile_wt", 0),
        data.get("n_cores", 0),
        data.get("pc", 0),
        data.get("px_height", 0),
        data.get("px_width", 0),
        data.get("ram", 0),
        data.get("sc_h", 0),
        data.get("sc_w", 0),
        data.get("talk_time", 0),
        data.get("three_g", 0),
        data.get("touch_screen", 0),
        data.get("wifi", 0)
    ]
    return DenseVector(fields)

# Apply UDF to create feature vectors
df_vectors = df_raw.withColumn("features", parse_json_to_vector(col("value")))

# Perform predictions
predictions = model.transform(df_vectors)

# Write predictions to console
hadoop_ip_address = "192.168.80.75"
hadoop_port = "9000"

# Stream to console
predictions.select("features", "prediction").writeStream \
    .trigger(processingTime="10 seconds") \
    .format("console") \
    .option("checkpointLocation", f"hdfs://{hadoop_ip_address}:{hadoop_port}/checkpoints/checkpoint30") \
    .outputMode("update") \
    .start()

# Stream to HDFS on another Hadoop address
predictions.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", f"hdfs://{hadoop_ip_address}:{hadoop_port}/checkpoints/checkpoint20") \
    .start(f"hdfs://{hadoop_ip_address}:{hadoop_port}/mobile_predict")

# Await termination

spark.streams.awaitAnyTermination()
