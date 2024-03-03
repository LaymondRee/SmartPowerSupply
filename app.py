from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
	return render_template('index3.html')


@app.route('/data', methods=["GET", "POST"])
def data():
	# Data Format
	# [TIME, Temperature, Humidity]

	with open('usb_data.txt', 'r') as file:
		Volt1 = float(file.readline())
		Volt2 = float(file.readline())
		Curr1 = float(file.readline())
		Curr2 = float(file.readline())
		Temp1 = float(file.readline())
		Temp2 = float(file.readline())

	data = [time() * 1000, Volt1, Volt2, Curr1, Curr2, Temp1, Temp2]

	response = make_response(json.dumps(data))

	response.content_type = 'application/json'

	return response


if __name__ == "__main__":
	app.run(debug=True)
