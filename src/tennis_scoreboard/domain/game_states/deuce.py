from tennis_scoreboard.domain.game_states.game_state import GameState
from tennis_scoreboard.domain.players.i_player import IPlayer

class Deuce(GameState):
    def scoreboard_format(self, p1: IPlayer, p2: IPlayer):
        return "Deuce"
    def is_in_game_state(self, p1: IPlayer, p2: IPlayer) -> bool:
        points = p1.points
        return points == p2.points and points > 2
