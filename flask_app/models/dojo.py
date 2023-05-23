from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.data = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comments = data["comments"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comments) VALUES (%(name)s, %(location)s, %(language)s, %(comments)s);"
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos WHERE ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL("encuesta_dojo").query_db(query)
        return Dojo(results[0])
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo["name"]) < 3:
            flash("El nombre debe de contener minimo tres caracteres.")
            is_valid = False
        if len(dojo["location"]) < 3:
            flash("La ubicacion debe de contener minimo tres caracteres.")
            is_valid = False
        if len(dojo["language"]) < 1:
            flash("El lenguaje debe de contener minimo un caracter.")
            is_valid = False
        return is_valid
        