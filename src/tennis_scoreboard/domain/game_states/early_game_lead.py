from tennis_scoreboard.domain.game_states.game_state import GameState
from tennis_scoreboard.domain.players.i_player import IPlayer

class EarlyGameLead(GameState):
    def scoreboard_format(self, p1: IPlayer, p2: IPlayer):
        p1_point_text = self._point_text(p1.points)
        p2_point_text = self._point_text(p2.points)
        return f"{p1_point_text}-{p2_point_text}"

    def is_in_game_state(self, p1: IPlayer, p2: IPlayer) -> bool:
        return not self._is_endgame(p1, p2) and p1.points != p2.points
