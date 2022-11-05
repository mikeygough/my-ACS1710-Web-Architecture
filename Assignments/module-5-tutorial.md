# Working with databases

In this lesson you will create a Python/Flask application that performs CRUD operations with a database. 

By the end of this tutorial you should be able to: 

- 
- 

## Getting started 

You need to install MongoDB. This is the database. 

Check to see if you have MongoDB installed. In your terminal: 

```
mongod --version
```

If the output looks something like: 

```
db version v4.0.2
git version: fc1573ba18aee42f97a3bb13b67af7d837826b47
allocator: system
modules: none
build environment:
    distarch: x86_64
    target_arch: x86_64
```

Then you have MongoDB installed and can skip this step. 

If it says something like Command not found you'll need to follow the steps below and install MongoDB. 

Follow the link here: 

https://www.mongodb.com/docs/manual/administration/install-community/

Choose your system and follow the instructions. 

Be sure to follow the instructions through the step: Run MongoDB Community Edition, and the step: To Run MongoDB...

You don't need to stop MongoDB! Once you've successfully started the MongoDB service you can move on to the next step. 

## Start a new project

Start a new project. Create a folder where you will work. You can also take time to initialize a new GitHub repo. 

## Setup and start your virtual environment

Follow the steps covered in Module 4. 

create venv

```
python3 -m venv env
```

Activate you virtual environment

```
source env/bin/activate
```

## Install dependencies

With the virtual environment activated you can now install depedencies. 

```
pip3 install Flask pymongo
```

You just installed pymongo you might be interested in the docs:

https://pymongo.readthedocs.io/en/stable/

Take a couple minutes to glance at the docs. Take note of points of interest:

- [Installing / upgrading](https://pymongo.readthedocs.io/en/stable/installation.html)
- [Tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html)
- [Eaxamples](https://pymongo.readthedocs.io/en/stable/examples/index.html)

## Start writing your app!

Since this is a Flask Web app you will want to use templates to render your web pages. 

Create a new folder named: templates

We need a file to run our app code. 

Create a new file: app.py

In app.py add the following: 

```Python
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos
```

Here you've imported your dependencies, created a new Flask app, and defined a client. This client variable contains a connection to your MongoDB database which should be running on port 27017. 

Last you got a reference to the database (db) from MongoDB and the todos collection. You haven't created any todos but you will! 

Your databases might contain multiple collections. A collection is a group of the same types of things. For example your new social media app might have a collection of posts, another collection of users, and yet another collection of friends. 

## Add a route

This route will be the main "home" page for the app. 

```python
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
```

This route handles both GET and POST requests from the `/` path. It renders `index.html`. This this page doesn't exist yet, you should create it!

Create: templates/index.html

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FlaskApp</title>
</head>
<body>
    <h1>FlaskTODO</h1>
	<hr>
	<div class="content">
		<form action="/" method="post">
			<p>
				<label>Todo:
				  <input type="text" name="content" placeholder="Todo Content">
        </label>
			</p>

			<div>
        <p>Priority:</p>
				  
        <p><label>
          <input name="priority" required type="radio" value="Important">
          Important</label></p>
				
        <p><label>
          <input name="priority" required type="radio" value="Unimportant">
          Unimportant</label></p>
				
        </div>

			<p><button type="submit">Submit</button></p>
		</form>
	</div>
</body>
</html>
```

This page displays a form with a field to describe your todo, and two radio buttons to set the todo's priority level. There is a submit button to submit the form. 

The action is "/" and the method is "post". The route created earlier should handle this. 

## Set some environment variables 

Set these environment variables to help with testing and development.

In the terminal with your virtual environment activated: 

```
export FLASK_APP=app
export FLASK_DEBUG=True
FLASK_ENV=development
```

These commands are for testing and devlopement. They help by providing more information when you run into errors. They should not be used in a production app. 

## Start your app

Start your app: 

```
flask run
```

Load your page in the browser: http://127.0.0.1:5000

You should see the form. Current your route is only rendering the form. You'll features in the following steps. 

## Add some styles

Your form is pretty bland. Some styles will help! 

Create a new folder: `static`

Add a new file: `static/styles.css`

Add some CSS code: 

```CSS
body {
	font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	font-size: 18px;
}

.todo {
	padding: 20px;
	margin: 10px;
	background-color: #eee;
}

button, input[type=submit] {
	padding: 0.5rem;
	background-color: #000;
	border-radius: 0.5rem;
	border: none;
	color: #fff;
	font-size: 1rem;
}

input[type=text] {
	padding: 0.5rem;
	border-width: 1px;
	border-style: solid;
	border-radius: 0.5rem;
	font-size: 1rem;
}
```

Here you added some tyles to set the default font to the system San Serif, styled class todo, and styled the buttons and inputs. 

In `templates/index.html` add a link to your stylesheet. Add the following in the `<head>` of the document:

```HTML
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
```

Refreshing your page should see your new styles take affect. 

## Handle the form submit and create new todo items

Edit the route in `app.py`.

```python
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        priority = request.form['priority']
        todos.insert_one({'content': content, 'priority': priority})
        return redirect(url_for('index'))

    return render_template('index.html')
```

Read that carefully. Notice the new code checks the request method. If the method is post it does the following: 

- Gets the value from the content field in the form. 
- Gets the value of priority from the form. This will be the value of the selector priority radio button. 
- Inserts one new object into the database in the todos collection. (read this line one more time)

This step creates new todo items it doesn't display them yet. Test your form. You should be able to create todos but you won't see the new todos on the page yet. 

The new document/record added to the database is an object/dictionary. 

```
{'content': content, 'priority': priority}
```

It has two property/keys: content and priority. The value of these are pulled from the form. 

MongoDB and NoSQL databases store values as object/dictionaries. We call these records or documents. 

Every record will also have an `_id` property. This is required. The database will not function without it. We didn't need to set this here because Mongo will generate the `_id` and assign it automatically. 

An `_id` will look similar to: 

```
63669bce67f9242ae8b0d62b
```

Sometimes you'll see it displayed as: 

```
ObjectId("63669bce67f9242ae8b0d62b")
```

What's important is that every document has a unique `_id`. 

You can use the `_id` of a record to: 

- Find a unique record
- Update or delete a unique record
- link or associate two or more records together
- Relate one record to another 

You'll try a couple of these ideas in the coming steps. 

## Displaying todo items

In this step you'll request records from your database and display them on the page. 

Edit the home page route: 

```python
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['priority']
        todos.insert_one({'content': content, 'priority': degree})
        return redirect(url_for('index'))

    all_todos = todos.find() # Add this line outside the if block! 
    return render_template('index.html', todos=all_todos) # add todos here! 
```

Add the new line: `all_todos = todos.find()` below the if block (not inside/indented.)

The new line finds all of the records in the `todos` collection. This should return a list of objects.

Next pass the list of todos to the template when you render it.

Before you can see the todos you'll need to turn that list of todos into HTML. Edit `templates/index.html`. Add the following below the form: 

```HTML
<hr>
{% for todo in todos %}
		<div class="todo">
				<p class="{{ todo.priority }}">{{ todo.content }} <em>({{ todo.priority }})</em></p>
		</div>
{% endfor %}
```

Here you are looping over each `todo` in the `todos` list. For each `todo` you create a div with a p tag displayng the todo content and the todo priority. 

I also added a class name with the priority. This would allow us to style the tag based on the priority which could be useful in the future. 

Refresh you page. You should see the todos in your database listed on the page. You should also be able to add new todo items to the database with the form. 

## Deleting todos

Todos are great but, when they are completed it would be good to remove them from the list. 

So far you have implemented Create, and Read. Let's add another CRUD operation to this app. 

Update `templates/index.html`:

```HTML
{% for todo in todos %}
	<div class="todo">
		<p class="{{ todo.priority }}">{{ todo.content }} <em>({{ todo.priority }})</em></p>
		
		<!-- New: delete button  -->
		<form method="POST" action="{{ '/' ~ todo._id ~ '/delete/'  }}">
			<input 
				type="submit" 
				value="Delete Todo" 
				onclick="return confirm('Are you sure you want to delete this entry?')">
		</form>
	</div>
{% endfor %}
```

The delete button is a form with a single button. Notcie these things: 

- The form action is a url similar to: `/63669bce67f9242ae8b0d62b/delete/`. Here you got the `todo._id` and combined it with some other strings. 
- The method is post. 
- The onclick action will use JavaScript to open an alert asking us to confirm our decision before submitting the form and canceling the operation on cancel. 

What's important is the _id is unique and Mongo can use it to find a unique record in a collection. 

Write a route to handle this new form action

Edit `app.py`:

```python
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))
```

Here you added a new route. The route looks for a url in the form of: 

```
/<id>/delete/
```

Where `<id>` is a Mongo id. 

Next, you used the `.delete_one()` method of the `todos` collection to delete a single record. To Identify the record you needed to include an object/dictionary that includes the `_id` of the record you want to delete. Notice that the value for the `_id` is passed to the `ObjectId()` function. Object ids are more than the string id value. This function takes the id string and turns it into valid Object id that Mongo can work with. 

Give your code a test. You should be able to create new todo items and delete them. 

## Take a look at your Database

Take a look at your database with a desktop tool. Download and install: 

https://studio3t.com

Launch the Studio 3T. Click the connect button. You should be connecting to 27017. 

In the left column you'll see a list of connections. Find flask_db. Open this and look for collections. You should find todos under collections. 

Double clicking todos should open a pane on the right. Click the > button to run the script: `db.getCollection("todos").find({})`. This should find all todos and show them. 

You can inspect the contents of your database, delete and edit items. 

## Stretch Challenges 

If you solved all of the problems here and have a functional app you need to challenge yourself. Try to solve these problems to test your understanding of the concepts here. 

### Add a new priority level

Add a new radio button to the list of priorities. Currently the list shows: Important, and Unimportant. It might be good to have a "normal" or "very important" priority level. 

Add a new radio button with a new value. Give it a matching label. 

Test your work by adding a new todo item with the new priority. 

### Style priorities

It would be helpful if users could spot important priority todos at a glance. Adding some color would heklp with this.

Currrently the todo priority string is displayed in a p tag that has a class name matching the priority value. You can style this name in your style sheet. Add a class for each priority name. Something like: 

```CSS
.Important {
	color: red;
}
```

### Sort your todos

Important! This app is running all of it's application logic on the serverside. The browser isn't doing any work. This gives us two possiblities to handling sorted todos. 

1. Todos can be sorted at the server. 
2. Todos can be sorted at the browser. 

#2 offers a lot of options and possibly more flexibility but requires us to rethink how the client side of our application functions. 

The downside to #1 is that you'll need to make a request to the server to get a sorted list. 

For this example start with #1. The goal here would be to sort the list of todos before they are "rendered" to the template and sent to the browser. 

Pymongo supports sorting with the `sort()` method. 

```python
all_todos = todos.find()
all_todos.sort('content')
```

Or:

```python
all_todos = todos.find().sort('content')
```

Here you are finding all of the records in the `todos` collection and sorting on the `content` field. 

Sorting like this sorts on the character value. That means `Z` sorts before `a` for example: 

- A
- B
- Z
- a
- b

To sort alphabetically try this: 

```python
all_todos = todos.find()
all_todos.collation({'locale': 'en'}) # set english locale
all_todos.sort('content')
```

or 

```python
all_todos = todos.find().collation({'locale': 'en'}).sort('content')
```

Both code snippets function the same. 

### Completion 

It might be good if we had a list that showed all of the todo items but could also show which were complete and which were not. This way we could avoid questions like: "did I feed the cat?"

To solve this challenge you need to add a new property to your todo items: `complete`. This can be a boolean value if your todos are completed True, or not complete False. Or it could be a string if todos might be "not complete", "in progress", and "complete". You decide. 

Follow these steps: 

Add a new field for your todos: complete. Figure all todos are Not complete when they are created. You can just add this field and it's default value to the todo that is initially created. 

Note! Your database has todos that do not have this new property! And, this can cause errors! You may want to delete or update the older todos when you add this new property. Either by using Studio3T or writing some code. 

Display the completion status in your template. 

To mark a todo as complete follow the same pattern as was used with the delete, form, and route. 

In order to update a record you'll need to call: `todos.update_one(filter, new_values)`. This method takes two parameters: `filter`, use this to identify which records to update, and `new_values`, an object/dictionary with the properties and values to updated. 

Here's an example: 

```python
filter = { '_id': ObjectId(id) }
new_values = { '$set': { 'complete': True } }
todos.update_one(filter, new_values)
```

Filter is an object with the `_id` of the record that should be updated. Remember that `_id` is unique for each record. 

New Values is an object with what to set. The format here is a little unexpected. It's the value of `'$set'` that will be set set. Here we are setting the 'complete' property to True. 

### Add a date to each todo

It would be good if each todo stored the date it was added to the list. This might help organize how we complete and prioritize our tasks! 

When the todo is created you'll need add a date field/property to the todo object. Generate a Python date object. It's probably best to store the date a as a UTC value then convert to a date string before it is displayed. 

