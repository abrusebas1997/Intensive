from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


app = Flask(__name__)

@app.route('/')
def index():
	# home page
	return render_template('index.html')

@app.route('/donate')
def donate():
	# Donate page
	return render_template('donate.html')


if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
