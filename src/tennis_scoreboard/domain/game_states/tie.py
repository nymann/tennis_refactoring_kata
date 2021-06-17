from tennis_scoreboard.domain.game_states.game_state import GameState
from tennis_scoreboard.domain.players.i_player import IPlayer


class Tie(GameState):
    def scoreboard_format(self, p1: IPlayer, p2: IPlayer):
        point_text = self._point_text(p1.points)
        return f"{point_text}-All"

    def is_in_game_state(self, p1: IPlayer, p2: IPlayer) -> bool:
        return p1.points < 3 and p1.points == p2.points
