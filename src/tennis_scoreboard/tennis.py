class TennisGame:

    def __init__(self, pl_name, p2_name):
        self.p1_name = pl_name
        self.p2_name = p2_name
        self.p1_points = 0
        self.p2_points = 0
        
    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1
    
    def score(self):
        if (self.p1_points==self.p2_points):
            return self._equal()
        elif self._is_endgame():
            return self._get_endgame_result()
        return self._get_score()

    def _equal(self):
        points = self.p1_points

        if points < 3:
            point_text = self._point_text(points)
            return f"{point_text}-All"
        return "Deuce"

    def _is_endgame(self):
        return self.p1_points>=4 or self.p2_points>=4

    def _get_endgame_result(self):
        point_delta = abs(self.p1_points-self.p2_points)
        leader = self._get_leader()
        
        if (point_delta == 1):
            return f"Advantage {leader}"
        return f"Win for {leader}"

    def _get_leader(self):
        if self.p1_points > self.p2_points:
            return self.p1_name
        return self.p2_name

    def _get_score(self):
        p1_point_text = self._point_text(self.p1_points)
        p2_point_text = self._point_text(self.p2_points)
        return f"{p1_point_text}-{p2_point_text}"

    def _point_text(self, point: int):
        return ["Love", "Fifteen", "Thirty", "Forty"][point]
