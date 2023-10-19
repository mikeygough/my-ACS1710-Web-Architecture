# Working with Virtual Environments and the ``requirements.txt`` File

## ACS 1710 - Module 4: Lesson 1

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Create and use a Python virtual environment in your project to manage dependencies.
- Install requirements for an existing project using a `requirements.txt` file.

# Videos 🎥

[Video 1 - Introduction to virtual environments](https://youtu.be/wNbqyD1OEXY)

Video 1 - Introduction to virtual environments

[Video 2 - Creating, activating, and deactivating virtual environments](https://youtu.be/VmgMbrDIDLA)

Video 2 - Creating, activating, and deactivating virtual environments

# Exercises 💪

Try creating and using a virtual environment for one of your past homework assignments.

# Written Companion 🗒

<aside>
🤔 How can we manage all of the development environments on our computer—especially if several projects have conflicting dependencies?

</aside>

---

Large scale applications and projects will often times require multiple coding languages and production environments in order to function properly. For example, the front-end and back-end might use the same programming languages with different dependencies, and the product must account for users running older versions of a product!

How can all of these dependencies and environments get managed effectively?

<aside>
💡 Virtual environments allow different projects to have unique dependency "spaces" that ensures conflicts do not occur, and that each area of a product has exactly what it needs to function.

</aside>

### Creating Virtual Environments with `venv`

The Python library `venv` enables developers to quickly create, activate, and deactivate Python virtual environments.

Use the following commands to get started with `venv`:

1. `venv` comes installed with Python3 so no installation needed!
2. creating a new `venv` within a directory: `python3 -m venv env`
3. activating an existing `venv`: 
    1. navigate to the directory containing the `venv` (in this case the directory hasn't changed yet and the `venv` instance uses the name `env`)
    2. use the command: `source env/bin/activate`
4. deactivating an active `venv`: `deactivate`

### Loading Dependencies via `requirements.txt`

A fresh project will often contain a file called `requirements.txt`. This file contains all of the dependency information needed to recreate the project environment.

To install all the dependencies packages in a `requirements.txt` file use the following commands:

1. navigate to the directory containing `requirements.txt`
2. use `pip3 install -r requirements.txt` to install all listed packages

A good practice to implement after adding new dependencies project would be updating the `requirements.txt` file associated with the project. This can be done with the following command:

- `pip3 freeze > requirements.txt`