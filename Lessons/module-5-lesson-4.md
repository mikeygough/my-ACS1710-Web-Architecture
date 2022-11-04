## WEB 1.1 - Module 5: Lesson 4

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Conceptually create a data query
- Identify relationships in data
- Explain the trade-offs between a SQL and NoSQL database
- Utilize MongoDB and the `ObjectId`

# Video Companions 🎥

[Video 1 - Performing C.R.U.D. operations to a MongoDB cluster via Flask and PyMongo](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6b33d5f-0398-4a3a-85c9-d3ae0c7078db/18_PyMongo_and_CRUD.mov)

Video 1 - Performing C.R.U.D. operations to a MongoDB cluster via Flask and PyMongo

# Exercises 💪

Complete the #TODO's in [this Repl.it](https://repl.it/team/WebArchitecture/Module-54CRUD-operations-in-PyMongo) and submit your work.

# Written Companion 🗒

<aside>
🤔 How do we use MongoDB in Python, and how can we connect a Flask server to a MongoDB database?
</aside>

---

The four primary operations that can be performed in a database can be described using the acronym **C.R.U.D:**

- create - the act of creating new collections or inserting new documents into a collection
- read - finding and retrieving documents/collections from the database for processing
- update - modifying a currently existing document or collection
- delete - removing a document or collection from the database

### Create = `insert_one()` and `insert_many()` in PyMongo

To **create** a new document within a MongoDB collection, the `insert_one(data)` or `insert_many(data)` methods must be used.

```python
# creating a new Python dictionary called `new_user`
new_user = {
   'first_name': 'Jay',
   'role': 'instructor',
   'teaches': 'WEB 1.1'
}

# insert this document into the mongo database collection called `users`
result = mongo.db.users.insert_one(new_user)
```

*Fig 1 - using the `insert_one` method to insert a Python dictionary object as a MongoDB document into the `users` collection.*

- *Note: since an `_id`* property did not get assigned an `ObjectId` value, MongoDB will create a default `_id`

### Read = `find()` in PyMongo

To **read** an existing document within a MongoDB collection, the `find(searchParam)` method must be used.

Using the `find()` method without any parameters will default to reading **all documents** in the collection.

Passing a specific **key-value** pair as a parameter to `find(searchParam)` will only return documents that contain a matching property.

```python
# reading all documents in a collection and printing the results
all_users = mongo.db.users.find()
for user in all_users:
   print(user['name'])

# reading documents that have a `role` of `instructor
all_instructors = mongo.db.users.find({'role': 'instructor'})
for user in all_instructors:
   print(user['name'])
```

*Fig 2 - using `find()` with and without a `searchParam`*

<aside>
🚨 If you only want the first matching document of your `find()` parameter to be returned (instead of all matching documents)—use `find_one(searchParam)` instead of `find(searchParam)`.

</aside>

### Update = `update_one()` in PyMongo

To **update** an existing document within a MongoDB collection, the `update_one(searchParam, changes)` method must be used.

<aside>
💡 In many ways, **updating** combines **reading** and **creating**. We must first pass the `update_one()` a `searchParam` to find the data to update—then modify the found data with the `changes` object.

</aside>

The `changes` update can perform many operations. Some of the most common include:

- `$set` = set old value to the new given value
- `$inc` = increment the found value by one
- `$regex` = utilize a regular expression

```python

# finding a document and updating it with changes
searchParam = { 'first_name': 'Jay' }
changes = {'$set': { 'role': 'CEO' }}
user1 = mongo.db.users.update_one(searchParam, changes)
```

*Fig 3 - using `update_one()` to perform a **change** in MongoDB*

- Note: *searchParam and changes get defined separate from `update_one()` in this example to make seeing the data easier. These can be written write into the `update_one()` function as well.*

### Delete = `delete_one()` in PyMongo

To **delete** an existing document within a MongoDB collection, the `delete_one(searchParam)` method must be used.

```python
# removing the document with a `first_name` of `Jay` from the users collection
result = mongo.db.users.delete_one({
   'first_name': 'Jay'
})
print(result.deleted_count)

>>> 1
```

*Fig 4 - deleting a document using `delete_one()`*

- *Note: the result returned after most operations will either be a 1 (for success) or an error number (for failure)*

### 👈 Previous Lesson

[Connecting a Flask Server to MongoDB Cluster](https://www.notion.so/Connecting-a-Flask-Server-to-MongoDB-Cluster-6385c238c38f433f9babc5e85fb67082)