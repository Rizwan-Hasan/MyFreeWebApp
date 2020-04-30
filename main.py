from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/<string:name>')
def nameArg(name: str):
    print(type(name))
    return 'Hello, ' + name


if __name__ == '__main__':
    app.run()
