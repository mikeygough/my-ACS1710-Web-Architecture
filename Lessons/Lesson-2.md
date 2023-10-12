# Setting up and Using Flask Servers

ACS 1710 - Module 1: Lesson 2

## Learning Outcomes

By the end of this lesson, you should be able to...

- Create and run a Flask server using Visual Studio Code
- (Optional) Explain how Python's decorator `@` symbol aids in writing routes
- (Optional) Explain how Python's `__name__` keyword allows us to write code that will run when the program starts

## Videos 🎥

Building our first Flask server step-by-step video walkthrough

video coming soon

Diving deeper into Python's Decorator @ syntax

video coming soon

Diving deeper into Python's __name__ keyword

Video coming soon

## Exercises 💪

Send your instructor a screenshot via Slack of your functioning web server! Your screenshot should look something like this:

![module-1-lesson-2-1.png](module-1-lesson-2-1.png)

## Written Companion 🗒

How can we develop a server capable of generating responses?

Servers can be created using many programming languages and frameworks. In this class we will be learning to develop servers capable of serving large user bases with the Python framework Flask.

Flask = a Python framework that allows developers to create servers and routes. Flask can be a great entry point because it is a micro framework, which means that it requires no other libraries to work!

Always feel free to ask for help when learning new technologies and frameworks. While you should always give things a good attempt on your own first—do not struggle to the point of exasperation as it will kill your motivation to learn!

## Installing Flask

1. Open a terminal on your computer (this can either be a dedicated terminal app on the terminal in your code editor).
2. run the following installation command: `pip3 install flask`

See the boilerplate and video walkthrough below for step-by-step instructions on creating our first Flask server.

## Code References 📀

### Terminal Commands:

- installation command = `pip3 install flask`
- running a local server = `python3 fileName.py`

### Boilerplates

```python
# standard flask boilerplate

# import the Flask server object
from flask import Flask

# create new Flask instance and assign it a root directory of the 
# working file (should be named 'main.py')
app = Flask(__name__)

# routes can be created using @app.route('routeName')
# NOTE: Flask uses Python's decorater syntax so a function must 
# be definied directly beneath the route declaration
@app.route('/')
def homepage():
    return "Hello, world!"

# the server can be accessed in your web browser using the URL localhost:3000/
if __name__ == '__main__':
    app.run(debug=True, port=3000)
```


