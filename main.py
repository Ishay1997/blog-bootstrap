from flask import Flask, render_template, request
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/f4dc99f755ee29815828").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        sender_email = "ishaylevy8@gmail.com"
        receiver_email = request.form["email"]
        subject = request.form["message"]
        message = f"Name: {request.form['name']}\nEmail: {request.form['email']}\nPhone: {request.form['phone']}\nMessage: {request.form['message']}"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, "edky jezu hbjw pqdv")
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
