# import flask
from flask import Flask, request, render_template

# create an instance of the flask server
# assign the root directory
app = Flask(__name__)

# create some routes
@app.route('/')
def displayHomepage():
    return render_template('index.html')

@app.route('/formExample')
def firstForm():
    return render_template('form.html')

@app.route('/result', methods=['GET'])
def simple_pizza_results():
    
    # a context object contains all of the needed form data for the template
    context = {
        'pizza_flavor': request.args.get('pizza_flavor'),
        'crust': request.args.get('crust')
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

# turn on the server
if __name__ == "__main__":
    app.run(debug=True, port=3000)