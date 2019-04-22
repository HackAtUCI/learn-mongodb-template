import csv

import pymongo
from mlab_credentials import credentials

'''
Danh's Notes:
Give exercises: "How would you query this"
Skeleton code with commented out full implementation
'''

class MongoManager:
    def __init__(self):
        pass

if __name__ == "__main__":
    #uri = "mongodb://{dbuser}:{dbpassword}@ds039007.mlab.com:39007/hack-roles".format(dbuser = credentials["username"], dbpassword = credentials["password"])
    #client = pymongo.MongoClient(uri)
    #print(client)

    reader = csv.DictReader(["committee", "role", "description", "qualifications", "prompt"])
    for i in reader:
        print(i)

    #client.close()

