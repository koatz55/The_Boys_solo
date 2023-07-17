import flask_app
from flask_app.config.mysqlconnection import connectToMySQL
#import other models
db = 'the_boys_schema'
class Topics:
    def __init__(self , db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.bio = db_data['bio']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.comments = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO topics ( name, bio, created_at, updated_at) VALUES (%(name)s, %(bio)s, Now(), NOW());"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM topics;"
        topics_from_db = connectToMySQL(db).query_db(query)
        topics = []
        for topic in topics_from_db:
            topic.append(cls(topic))
        return topics

    @classmethod 
    def get_all_comments(cls, data):
        query ="""select * FROM the_boys_schema.topics
            left join the_boys_schema.comments on comments.topic_id = topics.id
            left join the_boys_schema.users on  comments.users_id = users.id
            where topics.id = %(id)s"""
        results = connectToMySQL(db).query_db(query,data)
        print(results)

    @classmethod 
    def update_topic(cls, data):
        query = "update topics SET name = %(name)s, bio = %(bio)s, updated_at = NOW()) WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)