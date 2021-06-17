from typing import Optional
from abc import ABC, abstractmethod
from tennis_scoreboard.domain.game_states.i_game_state import IGameState
from tennis_scoreboard.domain.players.i_player import IPlayer

class GameState(IGameState, ABC):
    def get_leader(self, p1:IPlayer, p2:IPlayer) -> Optional[IPlayer]:
        if p1.points > p2.points:
            return p1
        elif p2.points > p1.points:
            return p2
        else:
            return None

    def _point_text(self, point: int):
        return ["Love", "Fifteen", "Thirty", "Forty"][point]

    def _is_endgame(self, p1, p2):
        return p1.points > 3 or p2.points > 3

    def _get_point_delta(self, p1, p2) -> int:
        return abs(p1.points - p2.points)

    @abstractmethod
    def is_in_game_state(self, p1: IPlayer, p2: IPlayer) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def scoreboard_format(self, p1:IPlayer, p2:IPlayer) -> str:
        raise NotImplementedError()

