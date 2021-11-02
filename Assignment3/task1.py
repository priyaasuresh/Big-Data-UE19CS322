import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import functions
from pyspark.sql.functions import *
from pyspark.sql.types import FloatType
sc = SparkContext("local", "task3_1")
sql_context = SQLContext(sc)

country, df_path = sys.argv[1:]
df = sql_context.read.csv(df_path, header=True)
df = df.filter(df.Country == country)
city_3 = df.groupBy(df.City).agg(avg(df.AverageTemperature).alias("avg_temp"))
df_sel=df.select("AverageTemperature","City")
df_sel=df_sel.withColumnRenamed("City","City1")

df_join=df_sel.join(city_3,df_sel.City1 ==  city_3.City,"inner")
df1=df_join.withColumn("AverageTemperature",df_join.AverageTemperature.cast(FloatType()))
df2=df1.withColumn("avg_temp",df1.avg_temp.cast(FloatType()))

df3=df2.filter(df2.AverageTemperature > df2.avg_temp)
df3=df3.select("City","AverageTemperature").collect()
df4= sorted(list(map(lambda x: (x[0], x[1]), df3)))

list1=[]
for i in df4:
    list1.append(i[0])

frequency = {}
for item in list1:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items() :
    print("{}\t{}".format(key,value))
