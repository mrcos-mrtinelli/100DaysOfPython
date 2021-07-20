from flask import Flask, render_template, redirect
from post import Post
import requests

app = Flask(__name__)
r = requests.get(url='https://api.npoint.io/3a5c17a4a7337a29219f')
r.raise_for_status()
json_posts = r.json()

all_posts = []

for p in json_posts['posts']:
    post_obj = Post(p['id'], p['title'], p['subtitle'], p['content'])
    all_posts.append(post_obj)
    print(all_posts)


@app.route("/")
def home():
    print(f"from home() - {type(all_posts)}")
    return render_template('index.html', blog_posts=all_posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for i, pst in enumerate(all_posts):
        if pst.id == post_id:
            requested_post = pst
    if requested_post is not None:
        return render_template("post.html", post=requested_post)
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
