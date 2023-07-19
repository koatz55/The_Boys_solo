from flask_app.config.mysqlconnection import connectToMySQL

db = 'the_boys_schema'
class Comments:
    def __init__(self , db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.title = db_data['title']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.topic_id = db_data['topic_id']
        self.user_id = db_data['user_id']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO comments ( first_name, title, comment, created_at, updated_at, topic_id, user_id) values (%(first_name)s, %(title)s, %(comment)s, now(), now(), %(topic_id)s, %(user_id)s);"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments;"
        comments_from_db = connectToMySQL(db).query_db(query)
        comments = []
        for comment in comments_from_db:
            comments.append(cls(comment))
        return comments

    # @classmethod 
    # def get_all_user_comments(cls, data):
    #     query ="""select * FROM the_boys_schema.topics
    #         left join the_boys_schema.comments on comments.topic_id = topics.id
    #         left join the_boys_schema.users on  comments.users_id = users.id
    #         where topics.id = %(id)s"""
    #     results = connectToMySQL(db).query_db(query,data)
    #     print(results)
    #     topic = cls(results[0])
    #     for row in results:
    #         c = {
    #             'id': row['comments.id'],
    #             'first_name': row['first_name'],
    #             'last_name': row['users.last_name'],
    #             'title': row['title'],
    #             'comment': row['comment'],
    #             'created_at': row['created_at'],
    #             'updated_at': row['updated_at']
    #         }
    #         topic.comments.append(Comments(c))
    #     return topic

    @classmethod 
    def update_comment(cls, data):
        query = "update comments SET title = %(title)s, comment = %(comment)s, updated_at = NOW()) WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod 
    def destroy(cls, data):
        query = "delete from comments where id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)