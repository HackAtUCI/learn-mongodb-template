# learn-mongoDB with Hack <4/30/2019>
In this workshop, you will learn about MongoDB and write a small script using PyMongo that will allow us to transfer data from the jobs.csv file to a MongoDB database.

### Requirements
- Download Python 3
- MongoDB Atlas account

On repo:
- Sample data from https://www.hackuci.com/recruit
- Virtual environment mongo with Pymongo installed (both win and linux)

### Basic Overview on Databases
The two main classes of databases are relational and non-relational. These classes are also refered to as SQL and NoSQL, where SQL stands for "Structured Query Language". The difference between the two classes lies in how the data is stored. SQL databases enforce a certain structure or "schema" that all data must have, while data NoSQL databases can differ in structure. 

Why would you use one type over the other? There is no one criteria that will let you decide, but a good general rule would be to look at your data. Is your data set up in certain way and not prone to change? Then a SQL database may work better. Is your data chaotic? Then using NoSQL may be better. 

Consider a case where you have a chaotic data set, one where some data have attributes that other data don't. If you were populating a NoSQL database, the uncertainty of data structure is not an issue. It will just put it in. However if the database is relational, you would need to update all entries for every new attribute that's encountered. This slows insertion to a linear time operation (O(n)) from constant time (O(1)).

Now the flexible nature of NoSQL databases may make NoSQL databases look like they outclass SQL ones, but what NoSQL databases offer in flexibility they return in uncertainty. There is no structure you can assume when using a NoSQL database if you take advantage of the flexibility.  

An additional thing to consider is how SQL and NoSQL databases generally scale. Without getting too detailed, SQL scales vertically(adding more capability to an existing machine) while NoSQL scales horizontally(adding more machines).  

Regardless of the type of database you work with, they will always have four fundamental operations: creating an entry, reading an entry, updating an entry, and deleting an entry (CRUD).

### MongoDB
MongoDB is a No-SQL database, so it organizes data in a schema-less manner by default. 
- Data is stored as BSON objects (binary representations of JSON objects). 

    Sample BSON object:
    {
        firstName: "George",
        lastName: "Louis",
        favColor: "Blue"
    }

- Each BSON object is called a "document", and a group of these documents are called a "collection". MongoDB is a database of collections. You can picture the organization like so.
    
    Database -> collections -> documents

The CRUD operations are called by:
- Create: insert_many() and insert_one()
- Read:   find()        and find_one()
- Update: update_many() and update_one()
- Delete: delete_many() and delete_one()

For create, you just need to pass data as a dict, either an iterable of them or just one.
For read, update, and delete, you can pass nothing to specify any document, or filter documents with a dict containing specific fields and values as well as operators and modifiers like $eq and $set. More information on this can be found at
https://docs.mongodb.com/manual/reference/operator/query/. Examples using query selectors and modifiers can be found in the db.py script.

### Further Reading:
- SQL vs NoSQL: https://medium.com/xplenty-blog/the-sql-vs-nosql-difference-mysql-vs-mongodb-32c9980e67b2
- Scalability: https://softwareengineering.stackexchange.com/questions/194340/why-are-nosql-databases-more-scalable-than-sql
- MongoDB Documentation: https://api.mongodb.com/python/current/api/pymongo/
- W3 Schools MongoDB Tutorial: https://www.w3schools.com/python/python_mongodb_getstarted.asp
