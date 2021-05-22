from abc import ABC, abstractmethod

from tennis_scoreboard.domain.game_states.i_game_state import IGameState
from tennis_scoreboard.domain.game_states.early_game_lead import EarlyGameLead
from tennis_scoreboard.domain.game_states.deuce import Deuce
from tennis_scoreboard.domain.game_states.tie import Tie
from tennis_scoreboard.domain.game_states.win import Win
from tennis_scoreboard.domain.game_states.advantage import Advantage


class IGameStateFactory(ABC):
    @abstractmethod
    def create_instance(self) -> IGameState:
        pass


class GameStateFromTwoPlayersFactory(IGameStateFactory):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def create_instance(self) -> IGameState:
        if (self.p1.points == self.p2.points):
            return self._equal()
        elif self._is_endgame():
            return self._get_endgame_result()
        else:
            return self._get_score()

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
