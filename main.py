import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello World!'
