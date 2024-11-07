from fastapi import FastAPI

"""Creates an instance of the FastAPI class, called app. 
This instance, app, is the core of my web application. 
It allows me to define routes (URLs) and handle incoming requests."""

app = FastAPI()

"""This is a decorator (see below) that registers a function to handle GET requests to the root URL (/). also / mean the localhost 8000
decorator tells FastAPI, "When a user sends a GET request to /, run the function below

"""


@app.get("/")
def index():
    return {"data": {"name": "Sarthak"}}


@app.get("/about")
def about():
    return {"data": "about page"}
