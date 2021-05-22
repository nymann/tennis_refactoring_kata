# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        if (self.p1points==self.p2points):
            return self._equal()
        elif self._is_endgame():
            return self._get_endgame_result()
        return self._get_score()

    def _equal(self):
        points = self.p1points

        if points < 3:
            point_text = self._point_text(points)
            return f"{point_text}-All"
        return "Deuce"

    def _is_endgame(self):
        return self.p1points>=4 or self.p2points>=4

    def _get_endgame_result(self):
        point_delta = abs(self.p1points-self.p2points)
        leader = self._get_leader()
        
        if (point_delta == 1):
            return f"Advantage {leader}"
        return f"Win for {leader}"

    def _get_leader(self):
        if self.p1points > self.p2points:
            return self.player1Name
        return self.player2Name

    def _get_score(self):
        p1_point_text = self._point_text(self.p1points)
        p2_point_text = self._point_text(self.p2points)
        return f"{p1_point_text}-{p2_point_text}"

    def _point_text(self, point: int):
        return ["Love", "Fifteen", "Thirty", "Forty"][point]
