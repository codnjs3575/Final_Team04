from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark import SparkContext


sc = SparkContext('yarn', 'getLocation')
sc.addFile('/home/ubuntu/anaconda3/lib/python3.7/site-packages')

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test']

def makeMongoSet():
    devColumns = [
        StructField("id", IntegerType()),
        StructField("s_name", StringType()),
        StructField("s_add", StringType()),
        StructField("s_road", StringType()),
        StructField("s_kind", StringType()),
        StructField("lat", FloatType()),
        StructField("lot", FloatType()),
        StructField("s_status", StringType()),
    ]
    devSchema = StructType(devColumns)

    load_loca = "/data/total_rest"
    df = spark.read.schema(devSchema).option("header", "true").csv(load_loca + "/part-00000*")
    df.createOrReplaceTempView('df')

    sql = f'select id, s_name, s_add, s_road, lat, lot from df where lat is not NULL or lat != ""'
    df2 = spark.sql(sql)

    df3 = df2.collect()

    df_list = list()
    for row in df3:
        df_list2 = list()
        df_list2.append(row['lot'])
        df_list2.append(row['lat'])
        df_dict = {'id': (row['id']), 's_name': row['s_name'], 's_add': row['s_add'], 's_road': row['s_road'],
                   'location': {'type': 'Point', 'coordinates': df_list2}}
        df_list.append(df_dict)
        if row['id'] % 100 == 0:
            print(row['id'])

    rest_mongo = db['rest']
    rest_mongo.drop()
    rest_mongo = db['rest']

    rest_mongo.insert_many(df_list)

if __name__ == '__main__':
    spark = SparkSession.builder.master('yarn').appName('addMongodb').getOrCreate()
    makeMongoSet()