from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model


class Sighting:

    def __init__(self, info):
        self.id = info['id']
        self.location = info['location']
        self.num_of_sasquatches = info['num_of_sasquatches']
        self.description = info['description']
        self.date = info['date']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']
        self.user_id = info['user_id']
        self.reporter = None

    @staticmethod
    def validation(sighting):
        is_valid = True
        if len(sighting['location']) < 3:
            flash("Location length minimum requirement is 3 characters", "sighting_message")
            is_valid = False
        if len(sighting['description']) < 3:
            flash("Description length minimum requirement is 3 characters", "sighting_message")
            is_valid = False
        if sighting['date'] == '':
            flash("Must select a date", "sighting_message")
            is_valid = False
        if sighting['num_of_sasquatches'] == '':
            flash("Number of Sasquatches must be greater than 1", "sighting_message")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO sightings (location,num_of_sasquatches,description,date,user_id) VALUES(%(location)s,%(num_of_sasquatches)s,%(description)s,%(date)s,%(user_id)s);"
        return connectToMySQL('sightings_schema').query_db(query, data)

    @classmethod
    def select_all_sightings(cls):
        query = """SELECT * FROM sightings JOIN users on sightings.user_id = users.id;"""

        result = connectToMySQL('sightings_schema').query_db(query)
        sightings = []
        for count in result:
            select_sighting = cls(count)
            user_info = {
                "id": count['users.id'],
                "first_name": count['first_name'],
                "last_name": count['last_name'],
                "email": count['email'],
                "password": "",
                "created_at": count['users.created_at'],
                "updated_at": count['users.updated_at']
            }
            select_sighting.reporter = user_model.User(user_info)
            sightings.append(select_sighting)
        return sightings

    @classmethod
    def select_one_sighting(cls, data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        result = connectToMySQL('sightings_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE sightings SET location=%(location)s,num_of_sasquatches=%(num_of_sasquatches)s,description=%(description)s,date=%(date)s,user_id=%(user_id)s WHERE id = %(id)s;"

        return connectToMySQL('sightings_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"

        return connectToMySQL('sightings_schema').query_db(query, data)

    @classmethod
    def select_with_id(cls, data):
        query = """
                SELECT * FROM sightings
                JOIN users on sightings.user_id = users.id
                WHERE sightings.id = %(id)s;
                """
        result = connectToMySQL('sightings_schema').query_db(query, data)
        if not result:
            return False

        result = result[0]
        select_sighting = cls(result)
        user_data = {
            "id": result['users.id'],
            "first_name": result['first_name'],
            "last_name": result['last_name'],
            "email": result['email'],
            "password": "",
            "created_at": result['users.created_at'],
            "updated_at": result['users.updated_at']
        }
        select_sighting.reporter = user_model.User(user_data)
        return select_sighting
