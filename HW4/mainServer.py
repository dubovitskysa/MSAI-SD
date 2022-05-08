from flask import Flask, render_template, request, redirect, url_for
from Post import Post
import datetime

app = Flask(__name__)
posts = []


@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html", posts=posts)


@app.route('/newPost')
def newPost():
    return render_template("newPost.html")


@app.route('/post/<int:id>')
def showPost(id):
    if 0 <= id < len(posts):
        return render_template("post.html", post=posts[id])
    else:
        print(f"Invalid post id: {id}")
        return index()


@app.route('/savePost', methods=['POST'])
def savePost():

    if request.form['postheader'] and request.form['postbody']:
        post = Post(len(posts), request.form['postheader'], request.form['postbody'], datetime.datetime.utcnow())
        posts.append(post)
        return redirect(url_for("index"))
    else:
        return newPost()


@app.route('/about')
def about():
    return "SD HW4 posts board v. 0.1"


if __name__ == "__main__":
    app.run(debug=True)