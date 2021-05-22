
from abc import ABC, abstractmethod


class IGameState(ABC):

    @abstractmethod
    def scoreboard_format(self) -> str:
        pass
