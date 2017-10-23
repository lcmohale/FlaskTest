# -*- coding: ascii -*-
import flask
from cs50 import SQL
from flask import Flask, render_template, url_for, request, request, redirect


app = Flask(__name__) #tell the App the name
db = SQL('sqlite:///Database.db') #locate the database


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('home.html')
	      	
@app.route('/about/')
def about():
    return render_template('about.html')
	
@app.route('/contact/')	
def contact():
    return render_template('contact.html')
	
@app.route('/stories/')
def stories():
    return render_template('stories.html')
	
@app.route('/blog/input/', methods=['GET','POST'])
def blogInput():
    if request.method == 'GET':
        return render_template('input.html')
    else:
        db.execute("INSERT INTO BlogPosts ('blogDate', 'blogTitle', 'blogText') VALUES (:blogDate, :blogTitle,:blogText)", blogDate = request.form['blogDate'], blogTitle = request.form['blogTitle'], blogText = request.form['blogText'])
        return redirect(url_for('showBlog'))
 
@app.route('/blog/<postId>/')
@app.route('/blog/')
def showBlog(postId = None):
    if postId == None:
        rows = db.execute('SELECT * FROM BlogPosts ORDER BY id DESC')
        return render_template('blog.html',blogPosts = rows)
    else:
        post = db.execute('SELECT * FROM BlogPosts WHERE id = :postId', postId = int(postId))
        if post:
            return render_template('bl.html', post = post)
        else:
            postId = None
            return redirect(url_for('showBlog'))
 	
@app.route('/projects')
def projects():
    return render_template('projects.html')
#make this route receive a parameter to enable direct download	
@app.route('/music/')
def music():
    return render_template('music.html')	

	

	
if __name__ == '__main__':
    print(flask.__version__)
    app.run(debug = True)