# WEB 1.1 (Web Architecture)

<span class="refresh-instructions">This syllabus is a living document! Hold down the `SHIFT` key and press `Refresh` to get the latest version.</span>

## Course Description

This course is designed to introduce students to the Flask web framework. Students will learn language independent patterns that are repeated across many common servers. The course will cover topics including the request-response cycle, server-side templating, APIs, databases, & unit testing, to help students to build the skills necessary to create custom web sites.

This course covers language-independent web server frameworks and patterns in full-stack web design. Students will use their prior knowledge in HTML, CSS, and JavaScript to build the front-end of a simple web application, and then will learn new concepts to write a supporting back-end. This course covers the request-response cycle, server-side templating, parsing data from an HTML form, HTTP methods, and using APIs. More advanced concepts include document-based databases and controller testing. 

## Prerequisites:

1. WEB 1.0 (Web Foundations)

## Course Specifics

**Course Delivery**: online | 7 weeks | 13 sessions

**Course Credits**: 3 units | 37.5 Seat Hours | 75 Total Hours

## Learning Outcomes

By the end of the course, you will be able to ...

1. Use Flask routes & route variables to create web pages with dynamic content.
1. Use forms & Jinja2 templates to take user input and display a result.
1. Make API calls & use/analyze the JSON data to show a result to the user.
1. Read and write to the MongoDB database using the PyMongo Object Document Mapper (ODM).
1. Implement Flask route tests to verify the correctness of routes.
1. Understand how the “create, read, update, deletion” (C.R.U.D) operations form the basis of user interactions in web architecture.


<!-- 
## Learning Modules

This course has been broken down into 5 modules for students to approach at their own pace. See the **schedule** below for recommendations on where you should be at in terms of content completion to help assess your pace.

##### Although this course has self-pacing elements--attendance is still a requirement! We will be doing activites, checking-in, and learning as a class!

#### MODULE 1: [ Introduction to internet communication patterns, C.R.U.D, and servers](https://www.notion.so/makeschool/MODULE-1-Introduction-to-internet-communication-patterns-C-R-U-D-and-servers-7238735fb1ec46a1af69c9585a87d34d) 

1. [Introduction to the Request/Response Cycle](https://www.notion.so/makeschool/Introduction-to-the-Request-Response-Cycle-b4f79a60f14044fe89e5765729c57534)
2. [Setting up and Using Flask Servers](https://www.notion.so/makeschool/Setting-up-and-Using-Flask-Servers-676ae2ed51db414d8605265ab1dbf1cb)
3. [Introduction to C.R.U.D](https://www.notion.so/makeschool/Introduction-to-C-R-U-D-6721ed692d5b4eaab2fa4a42b69c525e)
4. [`GET` vs `POST`](https://www.notion.so/makeschool/GET-vs-POST-10a1f44eb63141ebafe614960ba9a310)
5. [Working with Route Variables and Forms](https://www.notion.so/makeschool/Working-with-Route-Variables-and-Forms-989a154e9723449986ee188ee42b45d8)
6. [Interacting with Form Data in Flask](https://www.notion.so/makeschool/Interacting-with-Form-Data-in-Flask-0961ad39ea924109bb478b25e6f98f48)
7. [Understanding `**args` and `**kwargs`](https://www.notion.so/makeschool/Understanding-args-and-kwargs-77df2ff437dc4f0a9f57aa99610c6dcb)

#### MODULE 2: [ Creating scalable web applications and templating](https://www.notion.so/makeschool/MODULE-2-Creating-scalable-web-applications-and-templating-f952b99874f44ed7a886609ec4ecbd6c)

1. [Templating](https://www.notion.so/makeschool/Templating-3d4e522e057643169a3af209bea33b77)
2. [Named Parameters](https://www.notion.so/makeschool/Named-Parameters-e86280fd4a7a488eb9494a7de93288a2)
3. [Conditional Rendering with Templates](https://www.notion.so/makeschool/Conditional-Rendering-with-Templates-1d02a420605b4ecc9e999e9f9acdd03d)
4. [Loops in Templates](https://www.notion.so/makeschool/Loops-in-Templates-0350470fb2d349f29fe2af77546e5dd0)
5. [Creating Reusable Components via Template Inheritance](https://www.notion.so/makeschool/Creating-Reusable-Components-via-Template-Inheritance-816309fd9b084509a183a05ca22b4c79)


#### MODULE 3: [ Building robust services that connect to platforms via API's ](https://www.notion.so/makeschool/MODULE-3-Building-robust-services-that-connect-to-platforms-via-API-s-886ab4e636574ebca8e6e157ee8bf82b)
1. [Introduction to APIs](https://www.notion.so/makeschool/Introduction-to-APIs-cb1db95de4c24fdfbbdf9be49d4c201e)
2. [C.R.U.D in API's](https://www.notion.so/makeschool/C-R-U-D-in-API-s-d0478a7c928946b881fa62af058b22cb)
3. [Working with JSON Objects](https://www.notion.so/makeschool/Working-with-JSON-Objects-f95e153725f042a69bd06224f116d8b2)
4. [Testing API Routes with Postman](https://www.notion.so/makeschool/Testing-API-Routes-with-Postman-2c3abe212a424d3682bd94fc3724e180)
5. [Using the Requests Library to Generate User Requests](https://www.notion.so/makeschool/Using-the-Requests-Library-to-Generate-User-Requests-3c5c50b0fc374eb88708bb312a9a1def)


#### MODULE 4: [ Developing secure and distributable web applications](https://www.notion.so/makeschool/MODULE-4-Developing-secure-and-distributable-web-applications-bcc343ed1483406e8bb928ebf223e19c)
1. [Working with Virtual Environments and the `requirements.txt` File](https://www.notion.so/makeschool/Working-with-Virtual-Environments-and-the-requirements-txt-File-6dc8b6d6b8924d8db65db60eec68dfcc)
2. [Creating and Managing Environment Variables with `dotenv`](https://www.notion.so/makeschool/Creating-and-Managing-Environment-Variables-with-dotenv-ddb6aa5630fe464c884cfc1a75af9c2f)
3. [Leveraging the Datetime Library](https://www.notion.so/makeschool/Leveraging-the-Datetime-Library-c02959f8f3cc45b19e6582c215ed85d0)

#### MODULE 5: [ Introduction to databases and connecting servers to them ](https://www.notion.so/makeschool/MODULE-5-Introduction-to-databases-and-connecting-servers-to-them-ec864dcc497e44339ebb35381eb325a3)
1. [Introduction to Databases](https://www.notion.so/makeschool/Introduction-to-Databases-601c42c9732e46d595dd2c65a4186253)
2. [SQL vs NoSQL and Introduction to MongoDB](https://www.notion.so/makeschool/SQL-vs-NoSQL-and-Introduction-to-MongoDB-782a225705ad418d8c1af422c9c57083)
3. [Connecting a Flask Server to MongoDB Cluster](https://www.notion.so/makeschool/Connecting-a-Flask-Server-to-MongoDB-Cluster-6385c238c38f433f9babc5e85fb67082)
4. [Performing C.R.U.D Operations with PyMongo](https://www.notion.so/makeschool/Performing-C-R-U-D-Operations-with-PyMongo-0689895c65b24873b429423f14bacfa9)

 -->
## Schedule

Please look in the [tracker](https://docs.google.com/spreadsheets/d/1WDNjqiczzgwPRvCugKP7ZRxO2botYHpkjR1iKLAjmsM/edit#gid=0)

## Assignments

Assignments are turned in via the [tracker](https://docs.google.com/spreadsheets/d/1WDNjqiczzgwPRvCugKP7ZRxO2botYHpkjR1iKLAjmsM/edit#gid=0).

##### Assignments should be completed by the recommended date in the above **schedules** section. Students falling behind should connect with the instructor for help staying on pace!

1. [Task List Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA)
2. [Playlistr](https://github.com/Tech-at-DU/Flask-Playlister)
3. Contractor Project
4. Final Project
5. 
## Evaluation

**To pass this course, you must**: 

- Attend class
- Complete all assigned projects

## Attendance Policy

If you are not going to be in class, please let me know your progress and how you intend to stay on track with the projects and topics.


## Extra Materials

[ Introduction to WEB 1.1 (Web Architecture)](https://www.notion.so/makeschool/Introduction-to-WEB-1-1-Web-Architecture-44bea79b8e8245b8b61b364f8348569e)
