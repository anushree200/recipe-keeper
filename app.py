from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://axxshxxe20:aoWa1PDYvM78QgtX@cluster0.czqryun.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['recipe_db']
collection = db['recipes']

@app.route('/')
def index():
    recipes = list(collection.find())
    return render_template('front.html', recipes=recipes)

@app.route('/add', methods=['POST'])
def add_recipe():
    title = request.form['title']
    ingredients = request.form['ingredients'].split(',')
    steps = request.form['steps']
    cuisine = request.form['cuisine']
    collection.insert_one({
        "title": title,
        "ingredients": ingredients,
        "steps": steps,
        "cuisine": cuisine
    })
    return redirect('/')

@app.route('/search')
def search():
    ingredient = request.args.get('ingredient')
    results = list(collection.find({"ingredients": {"$regex": ingredient, "$options": "i"}}))
    return jsonify([{"title": r["title"], "cuisine": r["cuisine"]} for r in results])

if __name__ == '__main__':
    app.run(debug=True)