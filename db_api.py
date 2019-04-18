import pymongo
from mlab_credentials import credentials

if __name__ == "__main__":
    uri = "mongodb://{dbuser}:{dbpassword}@ds039007.mlab.com:39007/hack-roles".format(dbuser = credentials["username"], dbpassword = credentials["password"])
    client = pymongo.MongoClient(uri)

    client.close()