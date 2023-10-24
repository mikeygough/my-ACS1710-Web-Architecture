# import flask
from flask import Flask, request, render_template

A new function, 'render_template'

to leverage templates, make a directory called 'templates'. then you can put your .html in there.

to run flask (hot-reload) without it erroring it out all the time, use this:

flask --app main --debug run

where main is the name of your file.