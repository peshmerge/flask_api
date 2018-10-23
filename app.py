from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route("/")
def index():
    return make_response("This is sample flask api with two endpoints", 200)


@app.route("/about")
def about():
    return make_response("This is made by Peshmerge Morad", 200)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
