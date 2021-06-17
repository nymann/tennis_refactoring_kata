
from abc import ABC, abstractmethod

from tennis_scoreboard.domain.players.i_player import IPlayer


class IGameState(ABC):

    @abstractmethod
    def scoreboard_format(self, p1: IPlayer, p2: IPlayer) -> str:
        pass
