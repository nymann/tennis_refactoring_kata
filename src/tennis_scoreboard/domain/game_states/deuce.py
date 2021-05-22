from tennis_scoreboard.domain.game_states.game_state import GameState

class Deuce(GameState):
    def scoreboard_format(self):
        return "Deuce"
    
