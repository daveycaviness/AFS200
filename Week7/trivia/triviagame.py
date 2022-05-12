import requests
import triviaquestion

class TriviaGame():
    def __init__(self):
        self.multi_questions = []

    def getMultiQuestions(self):
        return self.multi_questions

    def getAllQuestions(self, amount, category, difficulty):
        URL =  f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"

        try:
            response = requests.get(URL, timeout=5)
            response.raise_for_status()
            response_JSON = response.json()
            question_list = response_JSON
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

        count = 0

        for questions in question_list['results']:
            newQuestion = questions['question']
            newCategory = questions['category']
            newDifficulty = questions['difficulty']
            newCorrectAnswers = questions['correct_answer']
            newIncorrectAnswers = questions['incorrect_answers']

            count = count + 1

            newTriviaQuestion = triviaquestion.TriviaQuestion(newQuestion, newCategory, newDifficulty, newCorrectAnswers, newIncorrectAnswers, [], count)
            newTriviaQuestion.getShuffledAnswers()
            self.multi_questions.append(newTriviaQuestion)

            print(newTriviaQuestion.getCorrectAnswer)

