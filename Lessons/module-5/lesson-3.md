# Connecting a Flask Server to MongoDB Cluster

## ACS 1710 - Module 3: Lesson 3

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Conceptually create a data query
- Identify relationships in data
- Explain the trade-offs between a SQL and NoSQL database
- Connect a Flask server to a MongoDB cluster

# Video Companions 🎥

[Setting Up MongoDB Atlas Video](https://youtu.be/0ENeevQ_1e0) (recommended before you watch the rest of this lesson)

https://youtu.be/05_dDRR9TyA

# Exercises 💪

Solve the #TODO's in this [this Repl.it](https://repl.it/team/WebArchitecture/Module-53Connecting-Flask-to-MongoDB) and submit your work.

# Written Companion 🗒

<aside>
🤔 How do we connect a Flask server with API routes to a MongoDB database cluster?

</aside>

---

The `Flask` object has a built-in property called `config` which allows developers to easily create **configuration variables** (see the **environment variables** lesson for relevant information) with the Python dictionary syntax: `app.config['URL_ROUTE'] = 'URLdestination'`

Using this `config` property, developers can create globally accessible URL connection points to help the Flask server find the MongoDB cluster destination.

<aside>
💡 Once a Flask server gets connected to a MongoDB cluster—we must use the PyMongo library to create a `mongo` object capable of interfacing between the server and database!

</aside>

```python
# create a Flask server, connect it to a MongoDB cluster, then make a mongo object
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# create a configuration variable called MONGO_URI,
# this connects the Flask server to the MongoDB cluster location
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

# create a Mongo object using the PyMongo library that can interact with MongoDB
mongo = PyMongo(app)
```

*Fig 1 - importing the Flask and PyMongo Python libraries, creating a Flask server, and connecting the server to the MongoDB database via a `config` variable*

- *Note: all operations between the server and the MongoDB database must be performed through the `mongo` object!*