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
    print(cuisines)
    print(type(cuisines))
    mealChoice=mongo.db.mealChoice.find().sort("mealChoiceName")
    serves=mongo.db.serves.find()
    return render_template('addrecipe.html',
                            recipes=recipes,
                            cuisines=cuisines,
                            mealChoice=mealChoice,
                            serves=serves)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    post_request = request.form.to_dict()
    print(post_request)
    return render_template('index.html')

@app.route('/browse_recipes')
def get_recipes():
    recipes=mongo.db.recipes.find()
    cuisines=mongo.db.cuisines.find()
    mealChoice=mongo.db.mealChoice.find()
    serves=mongo.db.serves.find()
    return render_template('browse_recipes.html',recipes=recipes, cuisines=cuisines,mealChoice=mealChoice,serves=serves)

@app.route('/nrecipe')
def nrecipe():
    recipes=mongo.db.recipes.find()
    totalrecipes=[recipes]
    return render_template('nrecipe.html',totalrecipes=totalrecipes,recipes=recipes)

@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    recipes=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("get_recipe.html", recipes=recipes)


@app.route('/get_cuisines')
def get_cuisines():
    return render_template('getcuisines.html',recipes=mongo.db.recipes.find(),cuisines=mongo.db.cuisines.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)