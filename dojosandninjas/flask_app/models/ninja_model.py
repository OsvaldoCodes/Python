from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:

    def __init__(self, info):
        self.id = info['id']
        self.first_name = info['first_name']
        self.last_name = info['last_name']
        self.age = info['age']
        self.created_at = info['created_at']
        self.updated_at = info['updated_at']

    @classmethod
    def save(cls, info):
        query = "INSERT INTO ninjas (first_name, last_name,age,dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, info)

    @classmethod
    def destroy(cls, info):
        query = "DELETE FROM ninjas (id)) VALUES %(id)s;"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, info)
