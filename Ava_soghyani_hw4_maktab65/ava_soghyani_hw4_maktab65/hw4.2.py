from os import scandir, write
import random #for choosing random question
import csv #for read question data in csv fil
#Quiz Class make object of question and answer
class Quiz:
   
    def __init__(self, question, answer_key,question_type):
        self.question = question #question to be asked
        self.answer_key = answer_key #options for the answer
        self.question_type=question_type #type of question
        self.user_answer=None #user answer
        self.ckeck=None #contain string value correct wrong and none


    def __repr__(self) :
        return f"{self.question_type} question :{self.question} "
        
        
    def ask_check_answer(self):# get the user answer and check the answer 
        self.user_answer=input(">>>>")
        if self.user_answer.lower() == self.answer_key:
            self.ckeck='correct'
            print("correct answer!")
        elif self.user_answer=='':
            self.ckeck='none'
            print("you dont answer this question")
        elif self.user_answer.lower()!=self.answer_key:
            self.ckeck='wrong'
            print("wrong answer")
        return self.ckeck

               
# class TrueFalse(Quiz): #TrueFalse class work the same as Quiz class   
    
# class MultipleChoice(Quiz): #MultipleChoice class work the same as Quiz class    
    
# class ShortAnswer(Quiz):  #ShortAnswer class work the same as Quiz class    

#ckass Score sub or sum the wrong or coorect answer and choose the winner or looser    
class Score:
    def __init__(self,scores=0): 
        self.scores=scores
        self.state=None
 

    def __add__(self,other):#add score
         return Score(self.scores+other)


    def __sub__(self,other) :#sub score
         return Score(self.scores-other)


    def check_winner(self):#choose the winner or looser
        if self.scores>=40:
            self.state='win'  
        else:
            self.state='loss'   
        return F' you {self.state} '


    def __str__(self):
       return f"{self.scores}"           


correct=0  #number of questions answeres correct
wrong=0 #number of questions answeres wrong
remaining=5 #number of question left over
q_no=0 #number of question asks
list_q=[] #list of question answers and question type
with open('soal.csv','r') as saq:#read the questions and answers from the csv list
    csv_reader=csv.DictReader(saq)
    line_count=0
    for row in csv_reader:
        if line_count==0:
            line_count += 1
        list_q.append(row)
        line_count += 1

score=Score()  

for i in range (5) :#its the main code to use classes,ask 5 question,count the score and choose winner or looser
    a=random.choice(list_q)
    soal=Quiz(a['question'],a['answer'],a['kind'])
    print(soal)
    remaining-=1
    q_no+=1
    javab=soal.ask_check_answer()
    if javab=='correct':
            score+=10
            correct+=1
    elif javab=='wrong':
            score-=3   
            wrong+=1 
    elif javab=='none':
            score=score
    with open('score.csv', mode='a') as score_table:#write the scores and quiz analiz in csv 
        fieldnames=['Q','Correct','Wrong','Score','remaining']   
        writer = csv.DictWriter(score_table,fieldnames=fieldnames)        
        writer.writerow({'Q':q_no,'Correct':correct,'Wrong':wrong,'Score':score,'remaining':remaining})
    print('Q '+'  Correct '+'  Wrong '+'  Score '+'  remaining ')
    print(f"{q_no}\t{correct}\t{wrong}\t{score}   \t  {remaining}")
print(Score.check_winner(score))
