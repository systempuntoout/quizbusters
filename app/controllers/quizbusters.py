import web
from app.models import rankings 
from app.logic import game
from config import view

 
class index:
    def GET(self):
        return view.index()

class quiz:
    def GET(self):
        web.localsession.kill()
        return view.username()
    
    def POST(self):
        
        try:
            timeout=bool(web.input()['timeout'])
        except:
            timeout=False
        try:
            name=web.input()['name']
        except:
            name=''
        try:
            answer=web.input()['answer']
        except:
            answer=''
        try:
            bonus=web.input()['bonus']
        except:
            bonus=''

        try:
            current_game=web.localsession.current_game    
        except:
            current_game=None
        
        try:    
            if current_game is None:
                if name!='':
                    current_game=game.Game(name)
                else:
                    return view.index()
            if (answer!='' or timeout or bonus!=''):
                current_game.check_answer(answer,timeout,bonus)
            question=current_game.get_question()
            web.localsession.current_game=current_game
            if current_game.is_over():
                web.localsession.kill()
            return view.quiz(current_game.username,question,current_game.is_over(), \
                             current_game.is_complete(),current_game.is_timed_out(),current_game.question_number, \
                             current_game.level,web.utils.commify(current_game.score),current_game.lifes,current_game.timer,current_game.is_special_question_enabled(),current_game.ranking,current_game.get_bonus_percentage())
        except Exception as e:
            print e
            web.localsession.kill()
            return view.oops()

class ranking:
    def GET(self,player_ranking=-1):
        top_players = rankings.get_top_players(limit=100)
        return view.ranking(top_players,player_ranking)

class downloads:
    def GET(self):
        return view.downloads()

class about:
    def GET(self):
        return view.about()
