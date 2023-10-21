# import flask
from flask import Flask

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
    <form action="" method="">
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

# turn on the server
if __name__ == "__main__":
    app.run(debug=True, port=3000)