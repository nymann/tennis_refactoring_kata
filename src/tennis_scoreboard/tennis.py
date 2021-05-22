from tennis_scoreboard.domain.players.i_player import IPlayer
from tennis_scoreboard.domain.players.player import Player

class GameState(object):
    def __init__(self, p1: IPlayer, p2: IPlayer):
        self.p1 = p1
        self.p2 = p2
        if self.p1.points > self.p2.points:
            self.leader = self.p1
        elif self.p2.points > self.p1.points:
            self.leader = self.p2
        else:
            self.leader = None

    def _point_text(self, point: int):
        return ["Love", "Fifteen", "Thirty", "Forty"][point]

class EarlyGameLead(GameState):
    def scoreboard_format(self):
        p1_point_text = self._point_text(self.p1.points)
        p2_point_text = self._point_text(self.p2.points)
        return f"{p1_point_text}-{p2_point_text}"

class Deuce(GameState):
    def scoreboard_format(self):
        return "Deuce"
    
class Tie(GameState):
    def scoreboard_format(self):
        point_text = self._point_text(self.p1.points)
        return f"{point_text}-All"

class Advantage(GameState):
    def scoreboard_format(self):
        return f"Advantage {self.leader.name}"

class Win(GameState):
    def scoreboard_format(self):
        return f"Win for {self.leader.name}"

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
