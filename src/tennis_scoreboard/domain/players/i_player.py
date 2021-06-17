from abc import ABC
from abc import abstractmethod
from abc import abstractproperty


class IPlayer(ABC):

    @abstractmethod
    def add_point(self) -> None:
        raise NotImplementedError()

    @abstractproperty
    def points(self) -> int:
        raise NotImplementedError()

    @abstractproperty
    def name(self) -> str:
        raise NotImplementedError()
