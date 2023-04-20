from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User


@app.route('/create')
def create_recipe():

    return render_template('add.html')


@app.route('/add/recipe', methods=['POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect('/home')
    if not Recipe.validation(request.form):
        return render_template('add.html')

    info = {
        "user_id": session['user_id'],
        "name": request.form['name'],
        "under_30_min": request.form['under_30_min'],
        "instruction": request.form['instruction'],
        "description": request.form['description'],
        "date_made": request.form['date_made']
    }

    Recipe.save(info)

    return redirect('/recipe/list')


@app.route('/recipe/list')
def recipe_list():
    if 'user_id' not in session:
        return redirect('/logout')

    info = {
        'id': session['user_id']
    }
    return render_template("recipes.html", recipes=Recipe.select_all_recipes(), user=User.select_with_id(info))


@app.route('/view/<int:id>')
def view_recipe(id):

    info = {
        "id": id
    }
    return render_template("view.html", recipe=Recipe.select_with_id(info))


@app.route('/edit/<int:id>')
def edit(id):
    info = {
        "id": id
    }
    return render_template("edit.html", recipe=Recipe.select_one_recipe(info))


@app.route('/recipe/edit/<int:id>', methods=['POST'])
def edit_page(id):
    # added after submission
    if 'user_id' not in session:
        return redirect('/home')
    if not Recipe.validation(request.form):
        return redirect('/recipe/list')

    info = {
        'id': id,
        'user_id': request.form['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instruction': request.form['instruction'],
        'date_made': request.form['date_made'],
        'under_30_min': request.form['under_30_min']
    }
    Recipe.update(info)

    return redirect('/recipe/list')


@app.route('/destroy/<int:id>')
def delete(id):
    info = {
        'id': id
    }
    Recipe.delete(info)
    return redirect('/recipe/list')
