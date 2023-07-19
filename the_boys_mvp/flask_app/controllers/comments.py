from flask import render_template,redirect,request,session, flash
from flask_app import app
from flask_app.models.topic import Topics
from flask_app.models.user import User
from flask_app.models.comment import Comments

@app.route('/update/<int:comment_id><int:topic_id>')
def edit_page(comment_id):
    data = {
        'id': comment_id
    }
    return render_template("update_ninja.html", Comment = Comments.get_one(data))

@app.route('/update/<int:comment_id>/', methods=['POST'])
def update(comment_id):
    data = {
        'id': comment_id,
        "title":request.form['title'],
        "comment":request.form['comment'],
        "topic_id": request.form['topic_id'],
    }
    Comments.update_comment(data)
    topic = request.form['topic_id'] 
    session[topic] = topic
    return redirect(f'/topic/comments/all/{int(topic)}')

@app.route('/delete/<int:comment_id>/<int:topic_id>')
def delete(comment_id,topic_id):
    data = {
        'id': comment_id,
        "topic_id": topic_id
    }
    Comments.destroy(data)
    return redirect(f'/topic/comments/all/{int(topic_id)}')