
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, LongType
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, count
# from delta import *
# Initialize Spark session
spark = SparkSession.builder.appName("readdelta")\
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

delta_table_path = "hdfs://192.168.80.67:9000/mobile_predict"

# Read the Delta table in streaming mode
df = spark.readStream.format("delta")\
  .option("ignoreChanges", "true")\
  .load(delta_table_path)

query = df.writeStream \
    .format("console") \
    .outputMode("append") \
    .start()

query.awaitTermination()