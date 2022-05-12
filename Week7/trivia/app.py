from flask import Flask, request, render_template
import triviagame

app = Flask(__name__)

myGame = triviagame.TriviaGame()
myGame.getAllQuestions(15, 10, 'medium')

@app.route("/", methods=['GET'])
def home():
    return render_template('questions.html', questions=myGame.getMultiQuestions())

@app.route("/score", methods=['POST'])
def score():
    correct = []
    incorrect = []
    for question in myGame.getMultiQuestions():
        if (request.form.get(str(question.getID())) == question.getCorrectAnswer()):
            correct.append(question)
        else:
            incorrect.append(question)
    return render_template('answers.html', answers=myGame.getMultiQuestions(), correctQuestions = correct, incorrectQuestions = incorrect)