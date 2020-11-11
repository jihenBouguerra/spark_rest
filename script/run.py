import json

import requests
from pyspark.sql import SparkSession


def init_spark():
    spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
    sc = spark.sparkContext
    return spark, sc


def call_rest_get():
    spark, sc = init_spark()
    response = requests.get("http://127.0.0.1:5000/api/jobs/all")
    jobs = sc.parallelize(response.json())
    print(jobs.map(lambda x: x['name']).collect())


def call_rest_post():
    # spark, sc = init_spark()
    json_file_path = "../data/data.json"
    with open(json_file_path) as json_file:
        jobs = json.load(json_file)

    # Making a POST request
    r = requests.post('http://localhost:5000/api/jobs/add', json=jobs)
    # check status code for response received
    # success code - 200
    print(r)
    # print content of request


if __name__ == '__main__':
    call_rest_get()
    call_rest_post()
