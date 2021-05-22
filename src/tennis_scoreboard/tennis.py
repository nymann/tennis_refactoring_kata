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
        if (self.p1.points == self.p2.points):
            return self._equal()
        elif self._is_endgame():
            return self._get_endgame_result()
        return self._get_score()

    def _equal(self):
        points = self.p1.points

        if points < 3:
            point_text = self._point_text(points)
            return f"{point_text}-All"
        return "Deuce"

    def _is_endgame(self):
        return self.p1.points >= 4 or self.p2.points >= 4

    def _get_endgame_result(self):
        point_delta = abs(self.p1.points - self.p2.points)
        leader = self._get_leader()
        
        if (point_delta == 1):
            return f"Advantage {leader}"
        return f"Win for {leader}"

    def _get_leader(self):
        if self.p1.points > self.p2.points:
            return self.p1.name
        return self.p2.name

    def _get_score(self):
        p1_point_text = self._point_text(self.p1.points)
        p2_point_text = self._point_text(self.p2.points)
        return f"{p1_point_text}-{p2_point_text}"

    def _point_text(self, point: int):
        return ["Love", "Fifteen", "Thirty", "Forty"][point]
