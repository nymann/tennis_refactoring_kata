from abc import ABC
from abc import abstractmethod

from tennis_scoreboard.domain.game_states.i_game_state import IGameState


class IGameStateFactory(ABC):
    @abstractmethod
    def create_game_state(self) -> IGameState:
        raise NotImplementedError()
