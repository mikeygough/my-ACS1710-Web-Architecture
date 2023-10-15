# Interacting with Form Data in Flask

ACS 1710 - Module 1: Lesson 6

# Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Write Flask routes that accept either a GET or a POST request.
- Collect form data from a user-submitted form, perform operations on the data, and show the user a result.

## Videos 🎥

https://youtu.be/5KvnErD1YG8

# Exercises 💪

Answer the review questions for Module 1 Section 5 on [Gradescope](http://gradescope.com).

# Written Companion 🗒

<aside>
🤔 We now know how to create forms and connect them to routes using the `action` property—but how do we interact with the data collected from the `<form>`?

</aside>

`<form>` data can be utilized on the server-side with Flask's built-in `request` function. More specifically, the following two methods of `request` must be invoked for the following two use-cases:

- `request.args.get('inputNameAttribute')` for `GET` requests
- `request.form.get('inputNameAttribute')` for `POST` requests

Do not be confused by the the naming of the request.form.get() method! A <form> can send information to any type of route. request.form.get() must be used to access <form> data in POST routes; no more no less. This can be quite confusing unfortunately, so just remember to use args.get() for GET requests and form.get() for POST requests.

```html
<!-- a form tag with an action and method attribute added to it -->
<form action="/results" method="GET">
   What's your favorite pizza flavor?
   <input type="text" name="pizza_flavor">
   <input type="submit" value="Submit">
</form>
```

Fig 1 (HTML) - the same <form> from the previous lesson repeated here to keep code consolidated

Once a <form> sends information to the route specified in the action attribute, the route can access any `<input>` values using the name attribute of the <input> tag.
