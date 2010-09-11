from config import db
import web
class Player():
    def __init__(self, username,level,score,id_ranking=-1):
        self.id_ranking=id_ranking
        self.username=username
        self.level=level
        self.score=score

def get_top_players(limit=100):
    player_list=[]
    for player_row in db.select('ranking',order="score DESC",limit=limit):
        player_list.append(Player(player_row['Name'],player_row['Level'],web.utils.commify(player_row['Score']),player_row['ID_ranking']))
    return player_list
    
def insert_player(player):
    id_insert=db.insert('ranking',Name=player.username,Level=player.level,Score=player.score)
    return get_player_ranking(id_insert,limit=100)
  
def get_player_ranking(id_ranking,limit=100):
    player_list=get_top_players()
    for standing,player in enumerate(player_list):
        if player.id_ranking==id_ranking:
            return standing+1
    return -1