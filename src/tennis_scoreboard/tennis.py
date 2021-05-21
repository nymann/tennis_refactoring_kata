class TennisGame(object):
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name: str):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self) -> str:
        if self.player1_points == self.player2_points:
            return self._equal_score(self.player1_points)
        if self.player1_points >= 4 or self.player2_points >= 4:
            player1_score_delta = self.player1_points - self.player2_points
            if abs(player1_score_delta) == 1:
                return self._advantage(player1_score_delta)
            return self._win(player1_score_delta)
        p1_score = self._letter_score(self.player1_points)
        p2_score = self._letter_score(self.player2_points)
        return "{p1}-{p2}".format(p1=p1_score, p2=p2_score)

    def _get_leader(self, point_delta: int) -> str:
        if point_delta > 0:
            return self.player1_name
        return self.player2_name

    def _advantage(self, point_delta: int) -> str:
        name = self._get_leader(point_delta)
        return "Advantage {name}".format(name=name)

    def _win(self, point_delta: int) -> str:
        name = self._get_leader(point_delta)
        return "Win for {name}".format(name=name)

    def _equal_score(self, points: int) -> str:
        if points > 2:
            return "Deuce"
        words = ["Love-All", "Fifteen-All", "Thirty-All"]
        return words[points]

    def _letter_score(self, points: int) -> str:
        words = ["Love", "Fifteen", "Thirty", "Forty"]
        return words[points]
