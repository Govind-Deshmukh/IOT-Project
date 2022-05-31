from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
import mysql.connector

mydb = mysql.connector.connect(
	host = "remotemysql.com",
	user = "uJjQaBfJbk",
	password = "fVIWjMLvvE",
    database = "uJjQaBfJbk"
)

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('testliveupdate.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    data = records[0]
    Temperature = data[2]
    Humidity = data[1]

    data = [time() * 1000, Temperature, Humidity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)