from flask import Flask, render_template, request

from random import randrange

app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [randrange(0, 100) for _ in range(10)]
    return render_template('index.html', name="Кот Васька",
                           numbers=numbers)


@app.route('/sum/', methods=['GET', 'POST'])
def sum_handler():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        return render_template('sum.html', a=a, b=b, total=int(a) + int(b))
    else:
        return render_template('sum.html')


if __name__ == '__main__':
    app.run(port=80)
