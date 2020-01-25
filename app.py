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
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addrecipe')
def add_recipe():
    recipes=mongo.db.recipes.find()
    cuisines=mongo.db.cuisines.find()
    mealChoice=mongo.db.mealChoice.find().sort('mealChoiceName',1)
    serves=mongo.db.serves.find()
    return render_template('add_recipe.html', recipes=recipes,cuisines=cuisines,mealChoice=mealChoice,serves=serves)

@app.route('/insert_recipe', methods=['GET','POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return render_template('index.html')

@app.route('/browse_recipes')
def get_recipes():
    recipes=mongo.db.recipes.find()
    cuisines=mongo.db.cuisines.find()
    mealChoice=mongo.db.mealChoice.find()
    serves=mongo.db.serves.find()
    return render_template('browse_recipes.html',recipes=recipes, cuisines=cuisines,mealChoice=mealChoice,serves=serves)

@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    cuisines=mongo.db.cuisines.find()
    mealChoice=mongo.db.mealChoice.find()
    serves=mongo.db.serves.find()
    recipes=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("get_recipe.html", recipes=recipes, cuisines=cuisines,mealChoice=mealChoice,serves=serves)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=False)