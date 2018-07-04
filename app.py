# render_template(Displays HTML on the screen)
# request(Grabs content provided by the user),
from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

# Server object
app = Flask(__name__)
CORS(app)

# Creating endpoints - Allows the server to decide what data to send back to the user
# Defining methods the route will use


@app.route("/", methods=['GET', 'POST'])
# A function that'll call when a method is made
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        # Setting the input value
        name = request.form.get('name')
        post = request.form.get('post')
        # Creating a function passing in the input values
        create_post(name, post)

    posts = get_posts()
    # Rendering html file and all posts when a user visits this file
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
