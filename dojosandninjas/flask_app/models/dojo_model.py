from flask_app.config.mysqlconnection import connectToMySQL
from .ninja_model import Ninja


class Dojo:

    def __init__(self, info):
        self.id = info['id']
        self.name = info['name']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, info):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, info)
        return result

    @classmethod
    def select_all_from_dojos(cls):
        query = "SELECT * FROM dojos;"

        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojo_list = []

        for count in result:
            dojo_list.append(cls(count))
        return dojo_list

    @classmethod
    def ninjas_in_dojo(cls, info):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, info)
        dojo = cls(result[0])
        for info in result:
            ninja_dict = {
                'id': info['ninjas.id'],
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'age': info['age'],
                'created_at': info['ninjas.created_at'],
                'updated_at': info['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_dict))
        return dojo
