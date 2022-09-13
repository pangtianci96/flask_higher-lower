from flask import Flask
import random

app = Flask(__name__)
# print(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route('/guess/<int:guess>')
def check_guess(guess):
    if guess > random_number:
        return '<h1 style="color: red;">Too high. Try again!</h1>' \
               '<img src="https://media.giphy.com/media/CoND5j6Bn1QZUgm1xX/giphy.gif"/>'
    elif guess < random_number:
        return '<h1 style="color: purple;">Too Low. Try again!</h1>' \
               '<img src="https://media.giphy.com/media/zkIIzwcq7LwUhSbPyu/giphy.gif"/>'
    else:
        return '<h1 style="color: green;">You found me</h1>' \
               '<img src="https://media.giphy.com/media/pPzjpxJXa0pna/giphy.gif"/>'


if __name__ == '__main__':
    app.run(debug=True)
