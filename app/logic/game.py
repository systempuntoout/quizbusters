import random
from app.models import questions
from app.models import rankings
from app.models import statistics

SECONDS_FOR_QUESTION = 20
SECONDS_FOR_QUESTION_SPECIAL = 30
LIVES = 3
CORRECT_ANSWERS_TO_BONUS = 10
SCORE_CORRECT_ANSWER= 2

class Game(object):
    def __init__(self,username):
        self.username=username
        self.questions=questions.shuffle_question_list()
        self.special_questions=questions.shuffle_special_question_list()
        self.game_over=False
        self.game_complete=False
        self.time_out=False
        self.score=0
        self.level=1
        self.id_question_to_be_answered=-1
        self.question_number=1
        self.timer=SECONDS_FOR_QUESTION
        self.lifes=LIVES
        self.good_answers=0
        self.level_up=False
        self.special_question_enabled=False
        self.ranking=-1
        self.bonus_percentage=0
        self.timer_temp=SECONDS_FOR_QUESTION
    
    def get_question(self):
        if not self.is_over():
            if not self.is_waiting_for_answer():
                if self.level_up and len(self.special_questions)>0:
                    self.special_question_enabled=True
                    self.timer_temp=self.timer
                    self.timer=SECONDS_FOR_QUESTION_SPECIAL
                    return questions.get_special_question(self.special_questions.pop(0)) 
                id_question=self.questions.pop(0)
                self.id_question_to_be_answered=id_question
                return questions.get_question(id_question)
            else:
                self.set_game_over()
                raise QuestionsException

    def check_answer(self, answer, timeout, bonus):
        self.timeout=timeout
        if self.is_waiting_for_answer():
            if answer==questions.get_question(self.id_question_to_be_answered).answer and not self.is_timed_out():
                self.score+=SCORE_CORRECT_ANSWER
                self.good_answers+=1
                if self.good_answers % CORRECT_ANSWERS_TO_BONUS==0: 
                    self.level+=1
                    self.level_up=True   
                    if self.level % 3 == 0 :
                        self.timer-=1
                        if self.lifes<6:
                        	self.lifes+=1
            elif self.lifes > 1:
                self.lifes-=1
            else:
                self.set_game_over(write_to_db=True)
                return False
                
            self.id_question_to_be_answered=-1
            self.question_number+=1
            if len(self.questions)==0:
                self.set_game_over(write_to_db=True,game_complete=True)
            return True
        elif bonus!='':
            if self.special_question_enabled:
                self.score=self.score*int(bonus)
                self.level_up=False
                self.special_question_enabled=False
                self.timer=self.timer_temp
        else:
            self.set_game_over()
            raise QuestionsException
    
    def is_over(self):
        return self.game_over
         
    def is_complete(self):
        return self.game_complete
    
    def is_timed_out(self):
        return self.time_out

    def is_special_question_enabled(self):
        return self.special_question_enabled
        
    def is_waiting_for_answer(self):
        return self.id_question_to_be_answered!=-1
    
    def get_bonus_percentage(self):
        if self.special_question_enabled:return 100
        else: return (self.good_answers % CORRECT_ANSWERS_TO_BONUS)*10
              
    def set_game_over(self,write_to_db=False,game_complete=False):
        self.game_over=True
        self.game_complete=game_complete
        if write_to_db:
            statistics.increment_games_played()
            if self.score>0:
                self.ranking=rankings.insert_player(rankings.Player(self.username,self.level,self.score))
           

class QuestionsException(Exception): pass 