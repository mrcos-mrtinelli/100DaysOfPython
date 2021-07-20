from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Nothing to see here</h1>'


@app.route('/guess/<name>')
def guess(name):
    url = 'https://api.agify.io?name='
    r = requests.get(url=f'{url}{name}')
    r.raise_for_status()
    result = r.json()

    return render_template('agify.html', name=name, age=result['age'])


if __name__ == "__main__":
    app.run(debug=True)
