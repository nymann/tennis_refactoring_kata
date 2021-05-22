from tennis_scoreboard.domain.game_states.game_state import GameState

class Advantage(GameState):
    def scoreboard_format(self):
        return f"Advantage {self.leader.name}"

