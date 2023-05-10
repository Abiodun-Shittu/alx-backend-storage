#!/usr/bin/env python3
"""
Task 12: a python function
"""
from pymongo import MongoClient


if __name__ == '__main__':
    # Connect to MongoDB and select the logs.nginx collection
    client = MongoClient()
    collection = client.logs.nginx

    # Print the number of logs
    print(f"{collection.count_documents({})} logs")

    # Print the number of logs per HTTP method
    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in http_methods:
        count = collection.count_documents({'method': method})
        print(f"    method {method}: {count}")

    # Print the number of logs for a specific method and path
    method = 'GET'
    path = '/status'
    count = collection.count_documents({'method': method, 'path': path})
    print(f"{count} {method} {path}")
