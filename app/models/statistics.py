from config import db
import web

class Statistic():
    def __init__(self, games_played):
        self.games_played=games_played

def get_games_played():
    games_played_row = web.listget(list(db.select('counters',what='counter',where='ID_counter="gamesplayed"')), 0, default=0)
    if games_played_row == 0:
        return 0
    else:
        return games_played_row['counter']
        
def increment_games_played():
    games_played=get_games_played()
    db.update('counters',counter = games_played+1,where='ID_counter="gamesplayed"')
    
def get_best_score():
    best_score_row = web.listget(list(db.select('ranking',what='max(score)')), 0, default=0)
    if best_score_row == 0:
        return 0
    else:
        return best_score_row['max(score)']
        
def get_total_number_of_questions():
    total_questions_row = web.listget(list(db.select('questions',what='count(ID_question)')), 0, default=0)
    if total_questions_row == 0:
        return 0
    else:
        return total_questions_row['count(ID_question)']