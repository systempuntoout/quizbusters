from config import db
import random
import web
class Question():
    def __init__(self, description,answer):
        self.description=description
        self.answer=answer
    def get_obf_dot_number(self):
        return ((len(self.description) % 10)+2)*2
    def get_obf_busted(self):
        busted='..'
        for count in range(1,self.get_obf_dot_number()):
            busted=busted+'.'
        return busted
    def get_obf_plausible(self):
        plausible='.'
        for count in range(1,self.get_obf_dot_number()):
            plausible=plausible+'.'
        return plausible
    def get_obf_confirmed(self):
        confirmed='...'
        for count in range(1,self.get_obf_dot_number()):
            confirmed=confirmed+'.'
        return confirmed    
    def get_obf_answer(self):
        if self.answer=='B':
            return self.get_obf_busted()
        elif self.answer=='P':
            return self.get_obf_plausible()
        elif self.answer=='C':
            return self.get_obf_confirmed()
            

class SpecialQuestion():
    def __init__(self, description,question_list):
        self.description=description
        self.question_list=question_list
        

def shuffle_question_list():
    question_list = [row['ID_question'] for row in list(db.select('questions',what='ID_question',where='ID_special_question is NULL'))]
    random.shuffle(question_list)
    return question_list

def shuffle_special_question_list():
    question_list = [row['ID_special_question'] for row in list(db.select('special_questions',what='ID_special_question'))]
    random.shuffle(question_list)
    return question_list

def get_question(ID_question):
    question_row = web.listget(list(db.select('questions',dict(ID_question=ID_question),where='ID_question=$ID_question')), 0, default=None)
    if question_row is None:
        return None
    else:
        return Question(question_row['Description'],question_row['Answer'])

def get_special_question(ID_special_question):
    special_question_row = web.listget(list(db.select('special_questions',dict(ID_special_question=ID_special_question),where='ID_special_question=$ID_special_question')), 0, default=None)
    if special_question_row is None:
        return None
    else:
        ID_special_question=special_question_row['ID_special_question']
        description_special_question=special_question_row['Description']
        question_list = [Question(row['Description'],row['Answer']) for row in list(db.select('questions',dict(ID_special_question=ID_special_question),where='ID_special_question=$ID_special_question'))]
        return SpecialQuestion(description_special_question,question_list)
        
