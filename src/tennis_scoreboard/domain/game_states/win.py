from tennis_scoreboard.domain.game_states.game_state import GameState

class Win(GameState):
    def scoreboard_format(self):
        return f"Win for {self.leader.name}"
