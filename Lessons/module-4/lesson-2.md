# Creating and Managing Environment Variables with ``dotenv``

## ACS 1710 - Module 4: Lesson 2

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Explain why it is important to hide secrets using a `.env` file.
- Use a `.env` file to hide secrets such as API keys and retrieve them in your code.

# Videos 🎥

[Vid 1 - Walking through a virtual environment and accessing a `SECRET_KEY`](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b30d583-b100-4707-a44b-a758e73b92bf/15_dotenv_code.mov)

Vid 1 - Walking through a virtual environment and accessing a `SECRET_KEY`

# Exercises 💪

Go back to your Homework 3 (More Forms) submission and use a `.env` file to hide the API key for the GIF Search API. Then in the code, call `load_dotenv()` and use the `os.getenv()` library function to retrieve and use it.

# Written Companion 🗒

<aside>
🤔 How can we easily manage configuration values, such as the URL for a database connection or the production server information, spread out in multiple files of a project?

</aside>

---

Any project that utilizes servers and databases, or multiple global constants, will require **environment variables** (sometimes synonymous with configuration variables). 

<aside>
💡 A variable that contains information required in a global scope that references details about how to connect to external components or internal settings repeated in multiple files can be definied as a **environment variable.**

</aside>

Examples of **environment variables:**

- the URL destination for a database that API calls get made to
- details such as the port and listening status of a server
- refresh rates or delays utilized in multiple front-end components that need to be configured from a single location
- API access keys and tokens required to access a database

### Securly Managing API Security Token and Password Data

<aside>
🚨 If another developer got a copy of our API security tokens—they could utilize the licences we purchased or make data requests in our name!

</aside>

Creating and managing **environment variables** in Python can be easily performed utilizing the `dotenv` library.

Instructions:

1. install the `dotenv` package with: `pip3 install python-dotenv`
2. create a new file in the working directory called `.env` (can be done with the command `touch .env`)
3. add **environment variables** to be referenced as **key-value** pairs

```python
# example environment variable in an `.env` file
SECRET_KEY="ilikebananas"
MY_API_TOKEN=5983-0A
```

*Fig 1 - a pair of **environment variables** called `SECRET_KEY` and `MY_API_TOKEN`*

 **4. within any Python file that needs access to the **environment variables**, utilize the `dotenv` and `os` libraries

```python
import os
from dotenv import load_dotenv

# this gives access to all the environment variables in `.env`
load_dotenv()

# the os library must be used to access the `.env` file itself
secret_key = os.getenv('SECRET_KEY')
print(secret_key) # 'ilikebananas' 
```

*Fig 2 - The `dotenv` and `os` libraries being used to access the **environment variable** called `SECRET_KEY` from the `.env` file*