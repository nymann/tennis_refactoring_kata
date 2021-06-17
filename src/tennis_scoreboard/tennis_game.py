from tennis_scoreboard.domain.game_state_factory import GameStateFromTwoPlayersFactory
from tennis_scoreboard.domain.game_states.i_game_state import IGameState
from tennis_scoreboard.domain.players.i_player import IPlayer


class TennisGame(object):

    def __init__(self, p1: IPlayer, p2: IPlayer):
        self.p1 = p1
        self.p2 = p2
        
    def won_point(self, player: IPlayer):
        if self.p1 == player:
            self.p1.add_point()
        else:
            self.p2.add_point()
    
    def score(self):
        game_state: IGameState = GameStateFromTwoPlayersFactory.create_game_state(self.p1, self.p2)
        return game_state.scoreboard_format(p1=self.p1, p2=self.p2)
