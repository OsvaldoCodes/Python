from flask import render_template, redirect, request, session, current_app
from flask_app import app
from flask_app.models.property_model import Property
from flask_app.models.user_model import User

@app.route('/contact_us')
def contact_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("contact_us.html")

@app.route('/settings')
def settings_page():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("settings.html")

@app.route('/sell')
def sell_property():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {"id": session['user_id']}
    return render_template('sell.html', user=User.select_with_id(data))


@app.route('/list', methods=['POST'])
def add_property():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Property.validation(request.form):
        data = {"id": session['user_id']}
        return render_template('sell.html', user=User.select_with_id(data))
    
    info = {
        "user_id": session['user_id'],
        "image": request.form['image'],
        "transaction": request.form['transaction'],
        "type": request.form['type'],
        "price": request.form['price'],
        "sqft": request.form['sqft'],
        "build_date": request.form['build_date'],
        "address": request.form['address'],
        "city": request.form['city'],
        "state": request.form['state'],
        "zipcode": request.form['zipcode'],
        "phone" : request.form['phone'],
        "description": request.form['description']
    }

    Property.save(info)

    return redirect('/my_listings')


@app.route('/my_listings')
def property_list():
    if 'user_id' not in session:
        return redirect('/logout')
    user_id = session['user_id']
    info = {'id': session['user_id']}
    return render_template("my_list.html", properties=Property.select_my_properties(user_id), user=User.select_with_id(info))

@app.route('/view/<int:id>')
def view_property(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {"id": session['user_id']}
    info = {"id": id}
    return render_template("view.html", property=Property.select_with_id(info), user=User.select_with_id(data))

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {"id": session['user_id']}
    info = {"id": id}
    return render_template("edit.html", property=Property.select_one_property(info), user=User.select_with_id(data))

@app.route('/property/edit/<int:id>', methods=['POST'])
def edit_page(id):

    if 'user_id' not in session:
        return redirect('/logout')
    
    info = {
        'id': id,
        'user_id': request.form['user_id'],
        "image": request.form['image'],
        "transaction": request.form['transaction'],
        "type": request.form['type'],
        "price": request.form['price'],
        "sqft": request.form['sqft'],
        "build_date": request.form['build_date'],
        "address": request.form['address'],
        "city": request.form['city'],
        "state": request.form['state'],
        "zipcode": request.form['zipcode'],
        "phone" : request.form['phone'],
        "description": request.form['description']
    }
    
    if not Property.validation(request.form):
        data = {"id": session['user_id']}
        return render_template('edit.html', property=Property.select_one_property(info), user=User.select_with_id(data))
    
    Property.update(info)

    return redirect('/my_listings')

@app.route('/destroy/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    info = {
        'id': id
    }
    Property.delete(info)
    return redirect('/my_listings')

@app.route('/view/destroy/<int:id>')
def view_page_delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    info = {
        'id': id
    }
    Property.delete(info)
    return redirect('/my_listings')