from tennis_scoreboard.domain.game_states.game_state import GameState

class Tie(GameState):
    def scoreboard_format(self):
        point_text = self._point_text(self.p1.points)
        return f"{point_text}-All"

