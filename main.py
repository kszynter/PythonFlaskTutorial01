from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return 'Using POST\n'
    else:
        return 'Probably using GET\n'


# decorator maps an URL to return value
@app.route('/about')
def about():
    return 'This is the about page'


# passing a variable value in the URL
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post id is: %s' % post_id


# run the app only when this script is run directly
# do nothing if this file is imported somewhere else
if __name__ == "__main__":
    app.run(debug=True)
