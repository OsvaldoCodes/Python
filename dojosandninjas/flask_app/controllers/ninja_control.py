from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo_model, ninja_model


@app.route('/add_ninja')
def add_ninja():

    return render_template('add_ninja.html', dojos=dojo_model.Dojo.select_all_from_dojos())


@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    ninja_model.Ninja.save(request.form)
    return redirect('/')

@app.route('/destroy_ninja/{{ninja.id}}')
def destroy(id):
    info = {
        'id': id
    }
    ninja_model.Ninja.destroy(info)
    return redirect('/show_dojo/{{d.id}}')