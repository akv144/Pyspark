# Databricks notebook source

# Usage of spark object in PySpark shell
spark.version

# COMMAND ----------

# Create SparkSession from builder
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName('SparkByExamples.com').getOrCreate()
spark

'''
master() – If you are running it on the cluster you need to use your master name as an argument to master(). usually, it would be either yarn or mesos depends on your cluster setup.

Use local[x] when running in Standalone mode. x should be an integer value and should be greater than 0; this represents how many partitions it should create when using RDD, DataFrame, and Dataset. Ideally, x value should be the number of CPU cores you have.
appName() – Used to set your application name.

getOrCreate() – This returns a SparkSession object if already exists, and creates a new one if not exist.
'''

# COMMAND ----------

# Create new SparkSession
spark2 = SparkSession.newSession
print(spark2)

# COMMAND ----------

# Get Existing SparkSession
spark3 = SparkSession.builder.getOrCreate
print(spark3)

# COMMAND ----------

# Usage of config()
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .config("spark.some.config.option", "config-value") \
      .getOrCreate()

# COMMAND ----------

# Enabling Hive to use in Spark -- enableHiveSupport()
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .config("spark.sql.warehouse.dir", "<path>/spark-warehouse") \
      .enableHiveSupport() \
      .getOrCreate()

# COMMAND ----------

# MAGIC %md
# MAGIC # Set Config
# MAGIC spark.conf.set("spark.executor.memory", "5g")
# MAGIC # Get a Spark Config
# MAGIC partions = spark.conf.get("spark.sql.shuffle.partitions")
# MAGIC print(partions)

# COMMAND ----------

# Create DataFrame
df = spark.createDataFrame(
    [("Scala", 25000), ("Spark", 35000), ("PHP", 21000)],["language","price"])
df.show()


# COMMAND ----------

# Spark SQL
df.createOrReplaceTempView("sample_table")
df2 = spark.sql("SELECT * FROM sample_table")
df2.show()

# COMMAND ----------

# Create Hive table & query it.  
spark.table("sample_table").write.saveAsTable("sample_hive_table")
df3 = spark.sql("SELECT * FROM sample_hive_table")
df3.show()

# COMMAND ----------

# Get metadata from the Catalog
# List databases
dbs = spark.catalog.listDatabases()
print(dbs)

# COMMAND ----------

# List Tables
tbls = spark.catalog.listTables()
print(tbls)


# COMMAND ----------

# MAGIC %md
# MAGIC 8. SparkSession Commonly Used Methods
# MAGIC 
# MAGIC version() – Returns the Spark version where your application is running, probably the Spark version your cluster is configured with.
# MAGIC 
# MAGIC createDataFrame() – This creates a DataFrame from a collection and an RDD
# MAGIC 
# MAGIC getActiveSession() – returns an active Spark session.
# MAGIC 
# MAGIC read() – Returns an instance of DataFrameReader class, this is used to read records from csv, parquet, avro, and more file formats into DataFrame.
# MAGIC 
# MAGIC readStream() – Returns an instance of DataStreamReader class, this is used to read streaming data. that can be used to read streaming data into DataFrame.
# MAGIC 
# MAGIC sparkContext() – Returns a SparkContext.
# MAGIC 
# MAGIC sql() – Returns a DataFrame after executing the SQL mentioned.
# MAGIC 
# MAGIC sqlContext() – Returns SQLContext.
# MAGIC 
# MAGIC stop() – Stop the current SparkContext.
# MAGIC 
# MAGIC table() – Returns a DataFrame of a table or view.
# MAGIC 
# MAGIC udf() – Creates a PySpark UDF to use it on DataFrame, Dataset, and SQL
