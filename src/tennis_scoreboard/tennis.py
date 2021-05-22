from tennis_scoreboard.domain.game_states.game_state_factory import GameStateFromTwoPlayersFactory
from tennis_scoreboard.domain.players.i_player import IPlayer
from tennis_scoreboard.domain.players.player import Player

class TennisGame(object):

    def __init__(self, p1_name, p2_name):
        self.p1: IPlayer = Player(p1_name)
        self.p2: IPlayer = Player(p2_name)
        
    def won_point(self, player_name):
        if player_name == self.p1.name:
            self.p1.add_point()
        else:
            self.p2.add_point()
    
    def score(self):
        game_state = GameStateFromTwoPlayersFactory(self.p1, self.p2).create_instance()
        return game_state.scoreboard_format()
