import csv

import pymongo
from mlab_credentials import credentials

'''
Process:
Create mlab 
make a database
create dbuser

discuss use of system collections

Powerpoint
- Go over scalability
- Go over advantages SQL vs No SQL (demo if you are ready)
- Describe applications of No SQL (Pick a hot topic to grab people attention)
- Give a brief history of mongodb (if applicable)

Demo
    Note:  Put fully working implementation above the skeleton code, create a class to manage database, Create some exercises

    -  Demo how to query the data (quick demo on how to use this data would be nice)   (Use filter)
    -  Demo how to update the data    (Use filter)
    -  Demo how to delete the data    (Use filter)

'''

if __name__ == "__main__":
    uri = "mongodb://{dbuser}:{dbpassword}@ds039007.mlab.com:39007/hack-roles".format(dbuser = credentials["username"], dbpassword = credentials["password"])
    client = pymongo.MongoClient(uri)
    db = client["hack-roles"]
    role_info = db["role-info"]


    # *CREATING DOCUMENTS* #
    # csv_file = open("roles.csv") 
    # reader = csv.DictReader(csv_file)   # will use the fieldnames in the first row to create dict for each row 
    # for row in reader:                  # could use insert_many() if you had a multiple dicts in a list
    #     role_info.insert_one(row)

    # *READING DOCUMENTS* #
    # filter = {"committees": {"regex": "^c.+"} }
    # for i in role_info.find(filter):
    #     print(i)
    # # find_one is pretty much the same thing, but find the first document with the specifications

    # just shows prompts -> could process the string and get the links and scrape them
    # for i in role_info.find({}, {"_id": 0, "prompt":1}):
    #     print(i)


    # *UPDATING DOCUMENTS* #
    role_info.update_one({"committee":"marketing"}, {"$set": {"foo": "bar"}})
    for i in role_info.find({}):
        print(i)

    # *DELETING DOCUMENTS* #
    role_info.delete_one()


    # *SORTING DOCUMENTS* #
    # for i in role_info.find({}, {"_id": 0, "committee":1}).sort("committee", -1):
    #     print(i)
    # for i in role_info.find({}, {"_id": 0, "committee":1}).sort("committee", 1):
    #     print(i)

    
    # *Exercises* #

  

    # https://api.mongodb.com/python/current/api/pymongo/collection.html
    # https://docs.mongodb.com/manual/reference/operator/aggregation/filter/
    # https://www.w3schools.com/python/python_mongodb_delete.asp

    # role_info.delete_many({}) # deletes all documents 
    # csv_file.close()
    client.close()

