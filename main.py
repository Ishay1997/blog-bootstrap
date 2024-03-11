import wait as wait
from flask import Flask, render_template
import requests
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assuming 'driver' is your WebDriver instance
# Wait up to 10 seconds for the element to be present

posts = requests.get("https://api.npoint.io/f4dc99f755ee29815828").json()
app = Flask(__name__)
image_status = {}

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")



@app.route('/')
def get_all_posts():
    global image_status
    return render_template("index.html", posts=posts)

# Your other routes here

@app.route('/show_post/<int:index>')
def show_post(index):
    requested_post = next((post for post in posts if post["id"] == index), None)
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
