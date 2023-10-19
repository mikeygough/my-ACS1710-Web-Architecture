# Templating

ACS 1710 - Module 2: Lesson 1

## Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Refactor an existing Flask route to render to a template
- Explain how variables are passed via `**kwargs` to a template
- Use passed-in variables within a Jinja2 template to show data to the user

## Videos 🎥

Vid 1 - Walking through templates and the render_template() function in Python

https://youtu.be/fHhuLnDJ7N0

Vid 2 - Using the context object to provide templates access to `<form>` data

https://youtu.be/p6BqrImSjrY

<!-- # Exercises 💪

Complete the challenges in [this repl.it](https://repl.it/team/WebArchitecture/Module-201JinjaRefactor) and submit your work. -->

# Written Companion 🗒

<aside>
🤔 How can we efficiently separate the Python code from the HTML code in a way that supports scalability and readability?

</aside>

### Coding without Templates

So far the previous examples up to this point have been intermingling Python and HTML code in the same file.

```python
# a route using Python Flask that returns HTML information in plaintext form
@app.route('/pizza/submit', methods=['GET', 'POST'])
def submit_pizza():
    users_email = request.args.get('email')
    users_phone = request.args.get('phone')
    crust_type = request.args.get('crust')
    pizza_size = request.args.get('size')
    list_of_toppings = request.args.getlist('toppings')
    accepted_terms = request.args.get('terms_conditions')

    if accepted_terms != 'accepted':
        return 'Please accept the terms and conditions and try again!'

		# HTML being returned as plain text
    return f"""
    Your order summary: <br>
    Email: {users_email} <br>
    Phone number: {users_phone} <br><br>

    You ordered a {crust_type} crust pizza of size {pizza_size}-inch
    with the following toppings: {', '.join(list_of_toppings)}
    """
```

Intermingling code as demonstrated in Fig 1 leads to poor readability, no code editor support, and challenging to scale code!

Combining Python and HTML into the same file violates several key principles of good coding—most notably the Don't Repeat Yourself (D.R.Y) rule. Imagine that an application had 10,000 routes that needed to return the same snippet of HTML and how this approach would not support that in any way.

### Coding with Templates

<aside>
💡 If we seperate the Python from the HTML, we can create easily interchangeable components capable of being reused and developed in their respective environments.

</aside>

Flask utilizes an approach to seperating Python code from HTML code known as templates. A template file exists seperatly from a Python file and contains all of the HTML code as a stand-alone, **reusable**, file that can be utilizied in any Flask route.

<aside>
🤔 Wouldn't seperating the code into two files require importing the templates into the route somehow? If so, how do we pass the template important Python variables and `<form>` data?

</aside>

Rendering a template requires two key pieces of information—the templateFile HTML file to be rendered and any Python data needed for that template. That second piece of information (the Python data needed to populate the HTML within the template) will be referred to as a context.

A context value most commonly gets passed to a template as an object using key-value pairs. 

```python
# a context variable using the `object` data structure
context = {
		'key1': request.args.get('input_name1'),
		'key2': request.args.get('input_name2')
}
```

<aside>
🤔 Now that we know about the `templateFile` and `context` values, how do we use them?

</aside>

To render a template, Flask provides a method called `render_template()`.

It takes two key arguments, `templateFile` and `context`, and looks like this: `render_template(templateFile, **context)`

<aside>
🚨 Note the `**kwargs` syntax in `**context` being utilized by `render_template()`. We do this because we do not know the number of **key-value** pairs that will be passed to the template. The `**kwargs` syntax lets the compiler know that the `context` object might have a different size each time it gets called and to handle it accordingly.

</aside>

```python
# the same `submit_pizza` route from Fig 1 - that returns a template instead of raw HTML
def submit_pizza():
    ...
    context = {
        'users_email': request.args.get('email'),
        'users_phone': request.args.get('phone'),
        'crust_type': request.args.get('crust'),
        'pizza_size': request.args.get('size'),
        'toppings': ', '.join(list_of_toppings)
    }
		
		# this code returns a template of HTML instead of plain text
    return render_template('submission_page.html', **context)
```

```html
<! -- an HTML file utilizing the Jinja2 templating syntax -- >
Your order summary: <br>
Email: {{ users_email }} <br>
Phone number: {{ users_phone }} <br><br>

You ordered a {{ crust_type }} crust pizza 
of size {{ pizza_size }}-inch
with the following toppings: {{ toppings }}
```

Note that the Jinja2 templating syntax wraps all the key names coming in from the context object with double curly brackets:`{{ keyName }}`

