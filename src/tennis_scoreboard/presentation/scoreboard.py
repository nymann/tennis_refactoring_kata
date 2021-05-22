from tennis_scoreboard.domain.player import Player
from tennis_scoreboard.domain.score import Score


class Scoreboard(object):
    def __init__(self, p1: str, p2: str):
        self.score = Score(Player(p1), Player(p2))

    def add_point(self, name: str):
        self.score.add_point(name=name)

    def __str__(self):
        if self.score.is_equal():
            return self._equal_text()

        if self.score.is_early_game():
            return self._early_game_text()

        if self.score.is_advantage():
            return "Advantage {name}".format(name=self.score.leader.name)

        if self.score.is_win():
            return "Win for {name}".format(name=self.score.leader.name)

        raise Exception("Unhandled score")

    def _equal_text(self) -> str:
        if self.score.p1.points > 2:
            return "Deuce"
        return "{word}-All".format(word=self._point_text(self.score.p1.points))

    def _early_game_text(self) -> str:
        p1_point_text = self._point_text(self.score.p1.points)
        p2_point_text = self._point_text(self.score.p2.points)
        return "{p1}-{p2}".format(p1=p1_point_text, p2=p2_point_text)

    def _point_text(self, points):
        return ["Love", "Fifteen", "Thirty", "Forty"][points]
