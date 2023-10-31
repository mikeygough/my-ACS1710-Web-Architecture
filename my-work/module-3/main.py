# import flask
from flask import Flask, request, render_template
import json

# create an instance of the flask server
# assign the root directory
app = Flask(__name__)

# create some routes
@app.route('/')
def displayHomepage():
    
    shopping_cart = [
        { "name": "Apple", "qty": 3 },
        { "name": "Orange", "qty": 2 },
    ]    
    
    context = {
        'mood': 10,
        'shopping_cart': shopping_cart    
    }
    
    return render_template('index.html', **context)

@app.route('/formExample')
def firstForm():
    return render_template('form.html')

@app.route('/result', methods=['GET'])
def simple_pizza_results():
    
    # a context object contains all of the needed form data for the template
    context = {
        'pizza_flavor': request.args.get('pizza_flavor'),
        'crust': request.args.get('crust'),
        'individual_toppings': ['mushrooms', 'olives', 'garlic']
    }
    
    return render_template('confirmation_page.html', **context)

@app.route('/route1')
def route1Info():
    return "<h3>Congrats on making route1</h3>"

# <> denote a route variable!
@app.route('/profile/<users_name>')
def profile(users_name):
    return "<h2>Hello " + users_name + "!</h2>"

@app.route('/date/<month>/<day>/<year>')
def displayGivenDate(month, day, year):
    return f"{month} / {day} / {year}"

with open('exampleObj.json') as example_obj_file:
    print("raw file printed = ", example_obj_file)
    # turn json into python dict
    jsonData = json.load(example_obj_file)
    print("just the JSON data printed = ", jsonData)

# json object example
@app.route('/jsonExample', methods=['GET'])
def jsonRoute():
    return jsonData

# turn on the server
if __name__ == "__main__":
    app.run(debug=True, port=3000)