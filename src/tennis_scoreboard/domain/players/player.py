from tennis_scoreboard.domain.players.i_player import IPlayer


class Player(IPlayer):
    def __init__(self, name: str, points: int = 0) -> None:
        self._name = name
        self._points = points

    def add_point(self) -> None:
        self._points += 1

    @property
    def points(self) -> int:
        return self._points

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, player: IPlayer) -> bool:
        if not isinstance(player, IPlayer):
            return False
        return self.name == player.name
