from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/c790b4d5cab58020d391"
post_title = ""

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(URL)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>/')
def get_post(id):
    global post_title
    response2 = requests.get(URL)
    all_posts = response2.json()
    for post in all_posts:
        print(post)
        if post["id"] == id:
            title = post["title"]
            subtitle = post["subtitle"]
            body = post["body"]
            break
    return render_template("post.html", post_title=title, post_subtitle=subtitle, post_body=body)
    

if __name__ == "__main__":
    app.run(debug=True)
