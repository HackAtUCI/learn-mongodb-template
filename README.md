# learn-mongoDB with Hack <4/30/2019>
In this workshop, you will learn about MongoDB and write a small script using PyMongo that will allow us to transfer data from the jobs.csv file to a MongoDB database.

### Materials and Resources
On repo:
- Sample data from https://www.hackuci.com/recruit
- Virtual environment mongo with Pymongo installed 
- 
-
-
-

### Basic Overview on Databases
The two main classes of databases are relational and non-relational. These classes are also refered to as SQL and NoSQL, where SQL stands for "Structured Query Language". The difference between the two classes lies in how the data is stored. SQL databases enforce a certain structure or "schema" that all data must have, while data NoSQL databases can differ in structure. 

Why would you use one type over the other? There is no one criteria that will let you decide, but a good general rule would be to look at your data. Is your data set up in certain way and not prone to change? Then a SQL database may work better. Is your data chaotic? Then using NoSQL may be better. 

Consider a case where you have a chaotic data set, one where some data have attributes that other data don't. If you were populating a NoSQL database, the uncertainty of data structure is not an issue. It will just put it in. However if the database is relational, it will update all entries for every new attribute that's encountered. This devolves insertion of new data into a linear time operation (O(n)) from constant time (O(1)).

Now the flexible nature of NoSQL databases may make NoSQL databases look like they outclass SQL ones, but what NoSQL databases offer in flexibility they return in uncertainty. There is no structure you can assume when using a NoSQL database if you take advantage of the flexibility.  

Regardless of the type of database you work with, they will always have four fundamental operations: creating an entry, reading an entry, updating an entry, and deleting an entry (CRUD).

Other things to write:..........................
Scalability?

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

Queries:
Sorting, function, using cursor

Filtering

### Further Reading:
- MongoDB Documentation: https://docs.mongodb.com/manual/tutorial/getting-started/
- SQL vs NoSQL: https://medium.com/xplenty-blog/the-sql-vs-nosql-difference-mysql-vs-mongodb-32c9980e67b2