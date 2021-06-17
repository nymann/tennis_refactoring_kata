from tennis_scoreboard.domain.game_states.game_state import GameState
from tennis_scoreboard.domain.players.i_player import IPlayer


class Advantage(GameState):
    def scoreboard_format(self, p1: IPlayer, p2: IPlayer):
        leader = self.get_leader(p1, p2)
        return f"Advantage {leader.name}"

    def is_in_game_state(self, p1: IPlayer, p2: IPlayer) -> bool:
        delta = self._get_point_delta(p1, p2)
        return self._is_endgame(p1, p2) and delta == 1
