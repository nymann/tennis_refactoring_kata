from tennis_scoreboard.domain.players.i_player import IPlayer
from tennis_scoreboard.domain.players.player import Player
from tennis_scoreboard.domain.game_states.early_game_lead import EarlyGameLead
from tennis_scoreboard.domain.game_states.deuce import Deuce
from tennis_scoreboard.domain.game_states.tie import Tie
from tennis_scoreboard.domain.game_states.win import Win
from tennis_scoreboard.domain.game_states.advantage import Advantage

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
        if (self.p1.points == self.p2.points):
            state = self._equal()
        elif self._is_endgame():
            state =  self._get_endgame_result()
        else:
            state = self._get_score()
        return state.scoreboard_format()

    def _equal(self):
        points = self.p1.points

        if points < 3:
            return Tie(self.p1, self.p2)
        return Deuce(self.p1, self.p2)

    def _is_endgame(self):
        return self.p1.points >= 4 or self.p2.points >= 4

    def _get_endgame_result(self):
        point_delta = abs(self.p1.points - self.p2.points)
        
        if (point_delta == 1):
            return Advantage(self.p1, self.p2)
        return Win(self.p1, self.p2)

    def _get_score(self):
        return EarlyGameLead(self.p1, self.p2)
