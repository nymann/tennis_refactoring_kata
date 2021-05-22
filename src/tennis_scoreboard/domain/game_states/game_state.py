from tennis_scoreboard.domain.game_states.i_game_state import IGameState
from tennis_scoreboard.domain.players.i_player import IPlayer

class GameState(IGameState):
    def __init__(self, p1: IPlayer, p2: IPlayer):
        self.p1 = p1
        self.p2 = p2
        if self.p1.points > self.p2.points:
            self.leader = self.p1
        elif self.p2.points > self.p1.points:
            self.leader = self.p2
        else:
            self.leader = None

    def _point_text(self, point: int):
        return ["Love", "Fifteen", "Thirty", "Forty"][point]

