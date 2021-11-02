import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import functions
from pyspark.sql.functions import *
from pyspark.sql.types import FloatType

sc = SparkContext("local", "task2")
spark_context = SQLContext.getOrCreate(sc)

city_path, global_path = sys.argv[1:]
c = spark_context.read.csv(city_path, header=True)
g = spark_context.read.csv(global_path, header=True)

d0 = c.select("dt","AverageTemperature","Country")
g_df = g.select("dt","LandAverageTemperature")

d1 = d0.withColumn("AverageTemperature", d0.AverageTemperature.cast('float'))
dfAverage = d1.groupBy(d1.dt,d1.Country).agg(max(d1.AverageTemperature).alias("max_temp"))

df_join=dfAverage.join(g_df,dfAverage.dt ==  g_df.dt,"inner")
df1=df_join.withColumn("LandAverageTemperature",df_join.LandAverageTemperature.cast(FloatType()))
d4=df1.select("Country","max_temp","LandAverageTemperature").filter(df1.LandAverageTemperature < df1.max_temp)

d5=d4.groupBy("Country").count()
d6=d5.sort('Country').collect()
for item in d6:
    print(item[0]+"\t"+str(item[1]))
