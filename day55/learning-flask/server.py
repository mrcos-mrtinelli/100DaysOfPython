from flask import Flask
import random

RANDOM_NUMBER = random.randint(0, 9)
print(RANDOM_NUMBER)

app = Flask(__name__)


@app.route("/")
def welcome():
    return '<h1>Guess a number between 0 and 9</h1>' \
           ' <a href="/1">#1</a> ' \
           ' <a href="/2">#2</a>' \
           ' <a href="/3">#3</a>' \
           ' <a href="/4">#4</a>' \
           ' <a href="/5">#5</a>' \
           ' <a href="/6">#6</a>' \
           ' <a href="/7">#7</a>' \
           ' <a href="/8">#8</a>' \
           ' <a href="/9">#9</a>' \
           '<p><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></p>'


@app.route("/<int:number>")
def guessed_number(number):
    if number > RANDOM_NUMBER:
        return '<h1 style="color:red;">Too High!</h1>' \
               '<p><img src="https://media.giphy.com/media/vPN3zK9dNL236/giphy.gif"></p>'
    elif number < RANDOM_NUMBER:
        return '<h1 style="color:purple;">Too LOW!</h1>' \
               '<p><img src="https://media.giphy.com/media/ceeN6U57leAhi/giphy.gif"></p>'
    else:
        return '<h1 style="color:green;">Great Job!</h1>' \
               '<p><img src="https://media.giphy.com/media/l378plFwSe6x8JGbS/giphy.gif"></p>'


if __name__ == "__main__":
    app.run(debug=True)
