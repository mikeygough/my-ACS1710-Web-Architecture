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

# example form

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