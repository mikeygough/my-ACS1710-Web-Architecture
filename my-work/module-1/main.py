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

# turn on the server
if __name__ == "__main__":
    app.run(debug=True, port=3000)