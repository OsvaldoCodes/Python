from multiprocessing import current_process
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model

class Property:
    def __init__(self, info):
        self.id = info['id']
        self.image = info['image']
        self.transaction = info['transaction']
        self.type = info['type']
        self.price = info['price']
        self.sqft = info['sqft']
        self.build_date = info['build_date']
        self.address = info['address']
        self.city = info['city']
        self.state = info['state']
        self.zipcode = info['zipcode']
        self.phone = info['phone']
        self.description = info['description']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']
        self.user_id = info['user_id']
        self.seller = None

    @staticmethod
    def validation(property):
        is_valid = True
        if property['image'] == '':
            flash("Must upload an image", "property_message")
            is_valid = False
        if property['price'] == '':
            flash("Price must be greater than $1", "property_message")
            is_valid = False
        if property['sqft'] == '':
            flash("Square feet must be greater than 1", "property_message")
            is_valid = False    
        if property['build_date'] == '':
            flash("Must select a Build Date", "property_message")
            is_valid = False
        if len(property['address']) < 5:
            flash("Address must be at least 5 characters", "property_message")
            is_valid = False
        if len(property['city']) < 3:
            flash("City must be at least 3 characters", "property_message")
            is_valid = False
        if len(property['state']) < 2:
            flash("State must be at least 2 characters", "property_message")
            is_valid = False
        if len(property['zipcode']) < 5:
            flash("Zip Code must be at least 5 digits", "property_message")
            is_valid = False
        if len(property['phone']) != 10:
            flash("Phone Number must be at least 10 digits", "property_message")
            is_valid = False
        if len(property['description']) < 3:
            flash("Description length minimum requirement is 3 characters", "property_message")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO properties (image,transaction,type,price,sqft,build_date,address,city,state,zipcode,phone,description,user_id) VALUES(%(image)s,%(transaction)s,%(type)s,%(price)s,%(sqft)s,%(build_date)s,%(address)s,%(city)s,%(state)s,%(zipcode)s,%(phone)s,%(description)s,%(user_id)s);"
        return connectToMySQL('properties_schema').query_db(query, data)

    @classmethod
    def select_all_properties(cls):
        query = "SELECT * FROM properties JOIN users ON properties.user_id = users.id;"
        result = connectToMySQL('properties_schema').query_db(query)
        properties = []
        for count in result:
            select_property = cls(count)
            user_info = {
                "id": count['users.id'],
                "first_name": count['first_name'],
                "last_name": count['last_name'],
                "dob": count['dob'],
                "email": count['email'],
                "password": "",
                "created_at": count['users.created_at'],
                "updated_at": count['users.updated_at']
            }
            select_property.seller = user_model.User(user_info)
            properties.append(select_property)
        return properties

    @classmethod
    def select_my_properties(cls, user_id):
        query = "SELECT * FROM properties WHERE user_id = %(user_id)s;"
        data = {'user_id': user_id}
        result = connectToMySQL('properties_schema').query_db(query, data)
        properties = []
        for count in result:
            select_property = cls(count)
            properties.append(select_property)
        return properties

    @classmethod
    def select_one_property(cls, data):
        query = "SELECT * FROM properties WHERE id = %(id)s;"
        result = connectToMySQL('properties_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE properties SET image=%(image)s,transaction=%(transaction)s,type=%(type)s,price=%(price)s,sqft=%(sqft)s,build_date=%(build_date)s,address=%(address)s,city=%(city)s,state=%(state)s,zipcode=%(zipcode)s,phone=%(phone)s,description=%(description)s,user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL('properties_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM properties WHERE id = %(id)s;"
        return connectToMySQL('properties_schema').query_db(query, data)

    @classmethod
    def select_with_id(cls, data):
        query = """
            SELECT * FROM properties
            JOIN users ON properties.user_id = users.id
            WHERE properties.id = %(id)s;
            """
        result = connectToMySQL('properties_schema').query_db(query, data)
        if not result:
            return False
        result = result[0]
        select_property = cls(result)
        user_data = {
            "id": result['users.id'],
            "first_name": result['first_name'],
            "last_name": result['last_name'],
            "dob": result['dob'],
            "email": result['email'],
            "password": "",
            "created_at": result['users.created_at'],
            "updated_at": result['users.updated_at']
        }
        select_property.seller = user_model.User(user_data)
        return select_property