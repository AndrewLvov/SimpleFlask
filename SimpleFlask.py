from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html>
    <body>
    <h1>Hello, {name}!</h1>
    </body>
    </html>
    """.format(name='Петро')


if __name__ == '__main__':
    app.run(port=80)
