from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Anonymize Large CSV") \
    .getOrCreate()

# Input and output paths
input_csv = "../data/large_data.csv"
output_folder = "../data/anonymized_data/"

# Load the CSV file into a DataFrame
df = spark.read.csv(input_csv, header=True, inferSchema=True)

# Anonymize specific columns using SHA-256
anonymized_df = df.withColumn("first_name", sha2(col("first_name"), 256)) \
    .withColumn("last_name", sha2(col("last_name"), 256)) \
    .withColumn("address", sha2(col("address"), 256))

# Save the anonymized DataFrame to a new folder
anonymized_df.write.csv(output_folder, header=True, mode="overwrite")

# Stop SparkSession
spark.stop()
