from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnan
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.linalg import DenseVector

# Initialize Spark session
spark = SparkSession.builder.appName("SpamClassifier")\
  .config('spark.cassandra.connection.host', '127.0.0.1:9042')\
  .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

# Load data into a Spark DataFrame
file_path = 'hdfs://192.168.80.67:9000/mobile_price/train.csv'
df = spark.read.csv(file_path, header=True)

def dosomething(x):
    return (DenseVector(x[:20]), x[20])

input_data = df.rdd.map(dosomething)

# Replace `df` with the new DataFrame
df1 = spark.createDataFrame(input_data, ["features", "price_range"])

from pyspark.ml.feature import StringIndexer
indexer = StringIndexer(inputCol="price_range", outputCol="price_ranges")
indexed = indexer.fit(df1).transform(df1)

# Logistic Regression model
lr = LogisticRegression(labelCol="price_ranges", featuresCol="features")

# Fit the model
model = lr.fit(indexed)

basePath = "hdfs://192.168.80.67:9000/mobile_price_model"
model.save(basePath)

spark.stop()