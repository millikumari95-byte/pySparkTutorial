import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr   # ✅ Import expr

# ✅ Force Spark to use your venv Python
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# ✅ Correct JAVA_HOME and PATH
os.environ['JAVA_HOME'] = r'C:\Users\Milli\.jdks\corretto-1.8.0_472'
#C:\Users\Milli\.jdks\corretto-1.8.0_482
os.environ['PATH'] = r'C:\Users\Milli\.jdks\corretto-1.8.0_472\bin' + os.pathsep + os.environ['PATH']

# ================== Spark Setup ==================
spark = SparkSession.builder \
    .appName("csv-test") \
    .master("local[*]") \
    .getOrCreate()



# data4 = [
#     (1, "raj"),
#     (2, "ravi"),
#     (3, "sai"),
#     (5, "rani")
# ]
# cust = spark.createDataFrame(data4, ["id", "name"])
# cust.show()
#
# data3 = [
#     (1, "mouse"),
#     (3, "mobile"),
#     (7, "laptop")
# ]
#
# prod = spark.createDataFrame(data3, ["id", "product"])
# prod.show()

data4 = [
    (1, "raj"),
    (2, "ravi"),
    (3, "sai"),
    (5, "rani")
]
cust = spark.createDataFrame(data4, ["id", "name"])
cust.show()

data3 = [
    (1, "mouse"),
    (3, "mobile"),
    (7, "laptop")
]

prod = spark.createDataFrame(data3, ["id", "product"])
prod.show()


# print("=====FULL  join=====")
# fulldf= cust. join(prod,cust["id"]==prod ["cid"], "full")
# fulldf.show()
# finaldf=(
#     fulldf.withColumn("id",expr("coalesce(id,cid) "))
# )
# finaldf.show()

leftAnti=cust.join(prod,["id"],"leftanti")
leftAnti.show()