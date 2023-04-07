from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.sighting_model import Sighting
from flask_app.models.user_model import User


@app.route('/create')
def create_sighting():
    data = {"id":session['user_id']}
    return render_template('add.html', user = User.select_with_id(data))


@app.route('/add/sighting', methods=['POST'])
def add_sighting():
    if 'user_id' not in session:
        return redirect('/home')
    if not Sighting.validation(request.form):
        data = {"id":session['user_id']}
        return render_template('add.html', user = User.select_with_id(data))

    info = {
        "user_id": session['user_id'],
        "location": request.form['location'],
        "num_of_sasquatches": request.form['num_of_sasquatches'],
        "description": request.form['description'],
        "date": request.form['date']
    }

    Sighting.save(info)

    return redirect('/sighting/list')


@app.route('/sighting/list')
def sighting_list():
    if 'user_id' not in session:
        return redirect('/logout')

    info = {'id': session['user_id']}
    return render_template("sightings.html", sightings=Sighting.select_all_sightings(), user=User.select_with_id(info))


@app.route('/view/<int:id>')
def view_sighting(id):
    data = {"id":session['user_id']}
    info = {"id": id}
    return render_template("view.html", sighting=Sighting.select_with_id(info), user = User.select_with_id(data))


@app.route('/edit/<int:id>')
def edit(id):
    data = {"id":session['user_id']}
    info = {"id": id}
    return render_template("edit.html", sighting=Sighting.select_one_sighting(info), user = User.select_with_id(data))


@app.route('/sighting/edit/<int:id>', methods=['POST'])
def edit_page(id):
    if 'user_id' not in session:
        return redirect('/home')
    if not Sighting.validation(request.form):
        data = {"id":session['user_id']}
        return render_template('add.html', user = User.select_with_id(data))

    info = {
        'id': id,
        'user_id': request.form['user_id'],
        'location': request.form['location'],
        'description': request.form['description'],
        'date': request.form['date'],
        'num_of_sasquatches': request.form['num_of_sasquatches']
    }
    Sighting.update(info)

    return redirect('/sighting/list')


@app.route('/destroy/<int:id>')
def delete(id):
    info = {
        'id': id
    }
    Sighting.delete(info)
    return redirect('/sighting/list')
