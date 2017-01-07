from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the homepage'


# decorator maps an URL to return value
@app.route('/about')
def about():
    return 'This is the about page'


# passing a variable value in the URL
@app.route('/profile/<username>')
def profile(username):
    return 'Hello %s' % username


@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post id is: %s' % post_id


# run the app only when this script is run directly
# do nothing if this file is imported somewhere else
if __name__ == "__main__":
    app.run(debug=True)
