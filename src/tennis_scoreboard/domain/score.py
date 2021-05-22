from typing import Optional

from tennis_scoreboard.domain.player import Player


class Score(object):
    def __init__(self, p1: Player, p2: Player):
        self.p1 = p1
        self.p2 = p2

    def add_point(self, name: str):
        if name == self.p1.name:
            self.p1.points += 1
        elif name == self.p2.name:
            self.p2.points += 1
        else:
            raise KeyError("The provided name doesn't match any of the players.")

    @property
    def leader(self) -> Optional[Player]:
        delta = self.p1.points - self.p2.points
        if delta == 0:
            return None
        if delta > 0:
            return self.p1
        return self.p2

    def is_equal(self) -> bool:
        return self.leader is None

    def is_early_game(self) -> bool:
        return self.p1.points <= 3 and self.p2.points <=3

    def is_advantage(self) -> bool:
        if self.is_early_game():
            return False
        return abs(self.p1.points - self.p2.points) == 1

    def is_win(self) -> bool:
        if self.is_early_game():
            return False
        return abs(self.p1.points - self.p2.points) > 1
