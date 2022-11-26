from flask import Flask, render_template

app = Flask(__name__, template_folder='assets')


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == "__main__":
    app.run()
