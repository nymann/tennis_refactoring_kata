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
        if self._is_early_game_lead():
            return EarlyGameLead(self.p1, self.p2)
        if self._is_tie():
            return Tie(self.p1, self.p2)
        if self._is_deuce():
            return Deuce(self.p1, self.p2)
        if self._is_advantage():
            return Advantage(self.p1, self.p2)
        if self._is_win():
            return Win(self.p1, self.p2)
        raise Exception("Game state not found")

    def _is_endgame(self):
        return self.p1.points > 3 or self.p2.points > 3

    def _is_win(self):
        delta = abs(self.p1.points - self.p2.points)
        return self._is_endgame() and delta > 1

    def _is_advantage(self):
        delta = abs(self.p1.points - self.p2.points)
        return self._is_endgame() and delta == 1

    def _is_tie(self):
        return self.p1.points < 3 and self.p1.points == self.p2.points

    def _is_deuce(self):
        points = self.p1.points
        return self.p1.points == self.p2.points and points > 2

    def _is_early_game_lead(self):
        delta = abs(self.p1.points - self.p2.points)
        return not self._is_endgame() and delta > 0
