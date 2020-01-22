import os
from os import path
if path.exists("env.py"):
    import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId

app = Flask(__name__)
MONGO_DBNAME = 'scran'
app.config['MONGO_URI'] = os.environ['MONGO_URI']

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)