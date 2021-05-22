from tennis_scoreboard.domain.game_states.game_state import GameState

class EarlyGameLead(GameState):
    def scoreboard_format(self):
        p1_point_text = self._point_text(self.p1.points)
        p2_point_text = self._point_text(self.p2.points)
        return f"{p1_point_text}-{p2_point_text}"
