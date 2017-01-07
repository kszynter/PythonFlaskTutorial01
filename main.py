from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the homepage'


@app.route('/about')
def about():
    return 'This is the about page'


# run the app only when this script is run directly
# do nothing if this file is imported somewhere else
if __name__ == "__main__":
    app.run(debug=True)
