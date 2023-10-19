# Named Parameters

## ACS 1710 - Module 2: Lesson 2

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Explain how named parameters can be used in place of a context dictionary to pass key-value pairs to a template.

# Exercises 💪

No exercises for this one, but if you want, try refactoring the previous exercise(s) to use named parameters instead of a context dictionary!

# Written Guide 🗒

<aside>
🤔 Wouldn't it sometimes be a better practice to pass in an entire **key-value** pair as a parameter instead of the `context` object? This could help in situations where the `context` object gets defined dynamically (i.e. we don't know the `context` values before run time)!

</aside>

```python
# a Python route that returns a rendered template
def submit_pizza():
    context = {
        'users_email': request.args.get('email'),
        'users_phone': request.args.get('phone'),
        'crust_type': request.args.get('crust'),
        'pizza_size': request.args.get('size')
    }
		
		# this code returns a template of HTML instead of plain text
    return render_template('submission_page.html', **context)
```

<aside>
💡 Since we pass the `context` object to `render_template()` using the `**kwargs` syntax, we could also pass in a series of **key-value** pairs defined as parameters as in *Fig 2.*

</aside>

This example gives exactly the same result as the previous example.

```python
def submit_pizza():
    return render_template('submission_page.html',
        users_email=request.args.get('email'),
        users_phone=request.args.get('phone'),
        crust_type=request.args.get('crust'),
        pizza_size=request.args.get('size'))
```

