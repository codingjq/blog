from flask import Flask, render_template, request

from sqlalchemy.orm import sessionmaker
from database import init_db, Session, session
from database.models import User, BlogEntry


init_db()

app = Flask(__name__)

@app.route("/")
def hello_world():
    blog_entries = session.query(BlogEntry).order_by(BlogEntry.date_created)[0:10]
    return render_template("home.html", blog_entries=blog_entries)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    entry = session.query(BlogEntry).filter(BlogEntry.id==post_id).scalar()
    if entry:
        return render_template("post.html", entry=entry)
    else:
        return render_template("post.html", entry="invalid")




## TODO: SECURE THESE ROUTES 

"""

@app.route("/new_post")
def new_post():
    return render_template("new_post.html")

@app.route("/submit_post", methods=["POST"])
def handle_submit_post():
    if request.method == "POST":
        author  = session.query(User).filter(User.username == "codingjq").scalar().id
        title = request.form['title']
        text = request.form['blog-entry']
        with session:
            blog_entry = BlogEntry(author=author, title=title, entry_text=text)
            session.add(blog_entry)
            session.commit()
            return "Success"


"""