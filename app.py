import os
from os import path
if path.exists("env.py"):
    import env
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId

app = Flask(__name__)
MONGO_DBNAME = 'scran'
app.config['MONGO_URI'] = os.environ['MONGO_URI']

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',recipes=mongo.db.recipes.find(),cuisines=mongo.db.cuisines.find(),mealChoice=mongo.db.mealChoice.find().sort('mealChoiceName',1),serves=mongo.db.serves.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    post_request = request.form.to_dict()
    print(recipe[recipe_name])
    return render_template('index.html')

@app.route('/get_cuisines')
def get_cuisines():
    return render_template('getcuisines.html',recipes=mongo.db.recipes.find(),cuisines=mongo.db.cuisines.find())




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)