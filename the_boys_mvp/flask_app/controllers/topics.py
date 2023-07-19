from flask import render_template,redirect,request,session, flash
from flask_app import app
from flask_app.models.topic import Topics
from flask_app.models.user import User
from flask_app.models.comment import Comments

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data),all_topics=Topics.get_all())

@app.route('/topic/comments/create/<int:topic_id>')
def get_create_page(topic_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id':  topic_id
    }    
    # pet = 'sally'
    # return render_template('create.html', cat = "Sally")
    return render_template('create.html', topic_id=topic_id)

@app.route('/topic/comments/all/<int:id>')
def show_topic_comments(id):
    data ={
        'id': id
    }
    return render_template('comments.html', topic=Topics.get_all_comments(data))

@app.route('/create',methods=['POST'])
def create_comment():
    Comments.save(request.form)
    topic = request.form['topic_id'] 
    session[topic] = topic
    return redirect(f'/topic/comments/all/{int(topic)}')