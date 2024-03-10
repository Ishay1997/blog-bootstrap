import requests
from flask import Flask, render_template

posts = requests.get("https://api.npoint.io/cbaf2e1513ffda165f3a").json()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts =posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/show_post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)