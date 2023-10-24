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

# example form for airplane ticketing system
formData = f"""
    <form action="/book" method="GET id="ticketform">
        <label for="departure">Departure Airport Code:</label>
        <input type="text" id="departure" name="departure">
        <label for="destination">Destination Airport Code:</label>
        <input type="text" id="destination" name="destination">
        <label for="class">Choose Seating Class</label>
        <select id="class" name="class" form="ticketform">
            <option value="economy">Economy Class</option>
            <option value="premium-economy">Premium Economy Class</option>
            <option value="business">Business Class</option>
            <option value="first">First Class</option>
        </select>
        <input type="submit" value="Book Flight">
    </form>

# example simple login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f"<h3>Thanks for logging in {username}</h3>"
    else:
        form = f"""
        <form action="/login" method="POST" id="loginform">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password">
            <input type="submit" value="Login">
        </form>
        """
        return form