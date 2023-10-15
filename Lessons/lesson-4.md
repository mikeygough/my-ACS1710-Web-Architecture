# GET vs POST

ACS 1710 - Module 1: Lesson 4

## Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Explain the differences between GET and POST requests.
- For a given example of a request, identify whether it should be a GET or POST request.

## Videos 🎥

https://youtu.be/jjwQQGIR1RU

## Exercises 💪

Answer the review questions for Module 1 section 3 on GradeScope. 

## Written Companion 🗒

Sometimes we want to receive data, while other times we want to send data. How do we differentiate between these two different types of requests?

Clients can create many types of requests. 

Try to imagine some of the user situations in which different requests might get made. For example, perhaps the user wants to get a list of shopping items from a website—while other times the user wants to upload their item for sale.

In this article, we will be exploring the two most common request methods— GET and POST.

The GET method provides data to the client, from the server, while the POST method provides data from the client, to the server. 

### Summary of the HTTP GET Method

- Used to make requests for **receiving** data.
- User data can be visibly seen in the URL when using `GET`

Examples:

- making a search query to a database
- sending a simple confirmation message

### Summary of the HTTP  POST Method

- Used to make requests geared towards **sending data** to be utilized as resource—usually to change the state of a system
- Form data can not be visibly seen in the URL

Examples:

- sending a username/password information to a sign-in portal
- updating a users profile information (i.e. adding a phone number or changing an account's email)

### GET and POST in relation to C.R.U.D

When the user needs to **read** data—`GET` should typically be employed.

**Creating, updating, and deleting** operations traditionally utilized the `POST` method. However, other HTTP methods have emerged such as `PUT` (for updating) and `DELETE` (for deleting)—leaving `POST` as the go-to for creation operations.



