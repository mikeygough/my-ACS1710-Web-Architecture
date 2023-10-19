# Loops in Templates

## ACS 1710 - Module 2: Lesson 4

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Use Jinja2 for loops to iteratively show list data in a template.

# Videos 🎥

<aside>
🚨 See the video companion in the lesson before this "Conditional Rendering in Templates" to see a `Jinja2` `for` loop in action.

</aside>

# Exercises 💪

Complete the exercise in [this repl.it](https://repl.it/team/WebArchitecture/Module-203JinjaLoops) and submit your work.

# Written Companion 🗒

<aside>
🤔 If the user needs to pass in a long array of elements, how do we iteratively process it?

</aside>

---

`Jinja2` supports `for` loops in a similar manner to conditional statements. Within the template file, create a `for` loop using the same syntax as python and wrap it within curly brackets and percentage signs:  `{% for element in elements %}`.

```python
# a route that uses an array as a value within context
@app.route('/compliments')
def get_compliments():

   compliments = [
       'brave',
       'witty',
       'tenacious'
   ]

   context = {
       'compliments': compliments
   }

   return render_template('compliments.html', **context)
```

*Fig 1 - rendering a template with a context containing an iterable array object*

```html
<! -- iterating through the context key compliment -- > 
Hello there, user! You are so...

<ul>
{% for compliment in compliments %}
   <li> {{ compliment }} </li>
{% endfor %}
</ul>
```

*Fig 2 - a template that uses a `for` loop to iterate through each compliment within the `context` object passed to it*