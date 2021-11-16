import csv
import random


class Quiz:
    counter = 0
    score = 0
    correct = 0
    wrong = 0

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.id = Quiz.counter + 1
        Quiz.counter += 1

    def check_the_answer(self, answer):
        if self.answer.__eq__(answer):              # __eq__ means: equal to (==)
            print("Correct answer!")
            Quiz.correct += 1
        else:
            print('Wrong answer!')
            Quiz.wrong += 1

    @classmethod
    def calculate_score(cls, answer, answer1):
        if answer.__eq__(answer1):
            Quiz.score = Quiz.score.__add__(10)         # __add__ means: +
        elif answer.__ne__(answer1):                    # __ne__ means: not equal (!=)
            Quiz.score = Quiz.score.__sub__(3)          # __sub__ means: -
        elif not answer1:
            Quiz.score = Quiz.score.__add__(0)
        else:
            print("Invalid Character!")
        return Quiz.score

    def __str__(self):
        return f'Question No.{self.id} :{self.question}'


class Score(Quiz):
    winner_status = False

    @classmethod
    def win_checking(cls):
        if Quiz.score.__ge__(40):
            print("You Win!")
            cls.winner_status = True
        else:
            print("You lost!")
        return cls.winner_status

    def __str__(self):
        return f"your score is: {Quiz.score}"

    @classmethod
    def correct_wrong(cls):
        return f"correct: {Quiz.correct} ,wrong : {Quiz.wrong}"


class TrueFalse(Quiz):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def check_the_answer(self, answer):
        if answer == 'true':
            if self.answer.__eq__('true'):
                print('Correct answer!')
                Quiz.correct += 1
            else:
                print('Wrong answer!')
                Quiz.wrong += 1
        elif answer == 'false':
            if self.answer.__eq__('false'):
                print('Correct answer!')
                Quiz.correct += 1
            else:
                print('Wrong answer!')
                Quiz.wrong += 1
        else:
            print('Enter True or False!')


class MultipleChoice(Quiz):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def check_the_answer(self, answer):
        super().check_the_answer(answer)


class ShortAnswer(Quiz):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def check_the_answer(self, answer):
        super().check_the_answer(answer)


questions_list = [{'question': 'All prime numbers are odd \n1.True\n2.False', 'answer': 'true'},
                  {'question': 'The capital of the Netherlands is not Amsterdam.\n1.True\n2.False ', 'answer': 'false'},
                  {'question': 'In the equation 3x+3 = 6, the value of x is equal to 1.\n1.True\n2.False',
                   'answer': 'true'},
                  {'question': 'Python is a compiler language.\n1.True\n2.False ', 'answer': 'false'},
                  {'question': 'The Nile is the longest river in the world.\n1.True\n2.False ', 'answer': 'true'},
                  {'question': 'What is the capital of France?', 'answer': 'paris'},
                  {'question': 'If A+B = 76 and A-B = 38 then A/B = ?', 'answer': '3'},
                  {'question': 'What is the highest mountain and the highest point on the planet?',
                   'answer': 'everest'},
                  {'question': 'Does each person have a unique fingerprint?', 'answer': 'yes'},
                  {'question': 'What is the capital of Canada?', 'answer': 'ottawa'},
                  {'question': 'How many provinces does Iran have? \na)28 \tb)29 \tc)30 \td)31 ', 'answer': 'd'},
                  {'question': 'What is the most populous country in the world? \na)India \tb)China \tc)Russia '
                               '\td)America', 'answer': 'b'},
                  {'question': 'In which country is the Leaning Tower of Pisa? \na)France \tb)Spain \tc)Italy '
                               '\td)Greece', 'answer': 'c'},
                  {'question': 'Which of the following numbers is different? \na)2 \tb)3 \tc)4 \td)7', 'answer': 'c'},
                  {'question': "Approximately what percentage of the world's population is left-handed?"
                               "\na)15\t b)20 \tc)30 \td)5", 'answer': 'a'}]

with open('question_file.csv', mode='w') as questions_file:
    fieldnames = ['question', 'answer']
    """
    Writing questions and answers in the csv file.
    First 5 question --> true-false
    Second 5 question --> short-answer
    Third 5 question --> multiple-choice
    """
    writer = csv.DictWriter(questions_file, fieldnames=fieldnames)
    writer.writeheader()
    for item in questions_list:
        writer.writerow(item)


def writing_file(q, correct, wrong, score, remaining):
    with open('csv_file.csv', 'a') as csv_file:
        count_row = 0
        fieldnames1 = ['Q', 'Correct', 'Wrong', 'Score', 'Remaining']
        writing = csv.DictWriter(csv_file, fieldnames=fieldnames1)
        if count_row == 0:
            writing.writeheader()
            count_row += 1
        writing.writerow({'Q': q, 'Correct': correct, 'Wrong': wrong, 'Score': score, 'Remaining': remaining})


def get_data():
    """
     In this function we create instance of classes (questions) randomly
     And according to the user's answer and using the writing_file function we reach the result.
    """

    a = questions_list[random.randint(0, 2)]
    q1 = TrueFalse(question=a['question'], answer=a['answer'])
    b = questions_list[random.randint(5, 7)]
    q2 = ShortAnswer(b['question'], b['answer'])
    c = questions_list[random.randint(10, 13)]
    q3 = MultipleChoice(c['question'], c['answer'])
    d = questions_list[random.randint(3, 4)]
    q4 = TrueFalse(d['question'], d['answer'])
    e = questions_list[random.randint(8, 9)]
    q5 = ShortAnswer(e['question'], e['answer'])
    my_list = [q1, q2, q3, q4, q5]

    for item in my_list:
        print(item)
        answer1 = input('Enter Answer: ').lower()
        item.check_the_answer(answer1)
        if my_list[0] == item:
            item.calculate_score(a['answer'], answer1)
            writing_file('1', Quiz.correct, Quiz.wrong, Quiz.score, '4')

        elif my_list[1] == item:
            item.calculate_score(b['answer'], answer1)
            writing_file('2', Quiz.correct, Quiz.wrong, Quiz.score, '3')

        elif my_list[2] == item:
            item.calculate_score(c['answer'], answer1)
            writing_file('3', Quiz.correct, Quiz.wrong, Quiz.score, '2')

        elif my_list[3] == item:
            item.calculate_score(d['answer'], answer1)
            writing_file('4', Quiz.correct, Quiz.wrong, Quiz.score, '1')

        elif my_list[4] == item:
            item.calculate_score(e['answer'], answer1)
            writing_file('5', Quiz.correct, Quiz.wrong, Quiz.score, '0')

    Score.win_checking()
    print(f"winner status : {Score.winner_status}")


get_data()
