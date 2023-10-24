# import flask
from flask import Flask, request, render_template

# create an instance of the flask server
# assign the root directory
app = Flask(__name__)

# create some routes
@app.route('/')
def displayHomepage():
    return "<h1>Welcome to your first website!</h1>"

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

formData = f"""
    <form action="/result" method="GET">
        What's your favorite pizza flavor?
        <input type="text" name="pizza_flavor">
        <br>
        What's your favorite crust type?
        <input type="text" name="crust">
        <input type="submit" value="submit pizza!">
    </form>
    """

@app.route('/formExample')
def firstForm():
    return formData

@app.route('/result', methods=['GET'])
def simple_pizza_results():
    pizza_flavor = request.args.get('pizza_flavor')
    crust = request.args.get('crust')
    return f"<h3>A {crust}-crust {pizza_flavor} pizza has been ordered!</h3>"

# turn on the server
if __name__ == "__main__":
    app.run(debug=True, port=3000)