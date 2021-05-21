class TennisGame(object):
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, playername: str):
        if playername == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self) -> str:
        if self.player1_points == self.player2_points:
            current_score = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")
        elif self.player1_points >= 4 or self.player2_points >= 4:
            player1_score_delta = self.player1_points - self.player2_points
            if player1_score_delta == 1:
                current_score = "Advantage {player}".format(player=self.player1_name)
            elif player1_score_delta == -1:
                current_score = "Advantage {player}".format(player=self.player2_name)
            elif player1_score_delta >= 2:
                current_score = "Win for {player}".format(player=self.player1_name)
            else:
                current_score = "Win for {player}".format(player=self.player2_name)
        else:
            p1_score = self._letter_score(self.player1_points)
            p2_score = self._letter_score(self.player2_points)
            current_score = "{p1}-{p2}".format(p1=p1_score, p2=p2_score)
        return current_score

    def _letter_score(self, points: int) -> str:
        words = ["Love", "Fifteen", "Thirty", "Forty"]
        return words[points]
