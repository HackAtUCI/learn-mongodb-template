import csv
import pymongo
from mlab_credentials import credentials

if __name__ == "__main__":

    uri = "mongodb+srv://{dbuser}:{dbpassword}@hackworkshop-f4a9a.mongodb.net/test?retryWrites=true".format(dbuser = credentials["dbuser"], dbpassword = credentials["dbpassword"])
    client = pymongo.MongoClient(uri)
    db = client["hack-roles"]
    role_info = db["role-info"]     # Collection functions: https://api.mongodb.com/python/current/api/pymongo/collection.html



    # *CREATING DOCUMENTS* #
    #
    # TO-DO (1): Insert data into database using csv.DictWriter (comment out code after inserted to avoid multiple insertions)
    #
    # csv_file = open("roles.csv") 
    # reader = csv.DictReader(csv_file)   # will use the fieldnames in the first row to create dict for each row 
    # for row in reader:                  # could use insert_many() if you had a multiple dicts in a list
    #     role_info.insert_one(row)
    # csv_file.close()



    # *READING DOCUMENTS* #
    #
    # TO-DO (2): Read all data from database 
    # for i in role_info.find():
    #     print(i)
    #
    # TO-DO (3): Print data that has no qualifications
    # filter = {"qualifications": "[]" }
    # for i in role_info.find(filter):
    #     print(i)
    #
    # TO-DO (4): Read data that has something in its qualification header with a query selector
    # filter = {"qualifications": {"$regex": "[A-Za-z]+"}}
    # for i in role_info.find(filter):
    #     print(i)
    #
    # TO-DO (5): Read same data as TO-DO (4), but omit everything except the prompt
    # filter = {"qualifications": {"$regex": "[A-Za-z]+"}}
    # for i in role_info.find(filter, {"_id": 0, "prompt": 1}):
    #     print(i)



    # *UPDATING DOCUMENTS* #
    #
    # TO-DO (6): Insert {"foo":"bar"} into first document with committee marketing and print it out to see update
    # role_info.update_one({"committee":"marketing"}, {"$set": {"foo": "bar"}})
    # print(role_info.find_one({"committee":"marketing"}))
    #
    # TO-DO (7): Rename the "role" field to "title"
    # role_info.update_many({}, {"$rename": {"role" : "title"}})
    # for i in role_info.find():
    #     print(i)
    # 
    # TO-DO (8): Take out the description field for all technology roles
    # print(role_info.update_many({"committee":"technology"}, {"$unset":{"description":""}}).modified_count) # show how many documents are changed
    # for i in role_info.find({"committee":"technology"}, {"description": 1}):
    #     print(i)



    # *DELETING DOCUMENTS* #
    #
    # TO-DO (9): Delete the first document
    # print(role_info.delete_one())
    # TO-DO (10): Delete any documents with no deliverable prompt
    # role_info.delete_many({"prompt":"[]"})



    # *SORTING DOCUMENTS* #
    #
    # TO-DO (11): Print all data in database sorted by committee in reverse order
    # for i in role_info.find({}, {"_id": 0, "committee":1}).sort("committee", -1):
    #     print(i)
    #
    # TO-DO (12): Print all data sorted by committee 
    # for i in role_info.find({}, {"_id": 0, "committee":1}).sort("committee", 1):
    #     print(i)
    
    # *Exercises* #

    #role_info.delete_many() # deletes all documents 
    client.close()

