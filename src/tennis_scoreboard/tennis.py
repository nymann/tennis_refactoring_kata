from tennis_scoreboard.presentation.scoreboard import Scoreboard

class TennisGame(object):
    def __init__(self, player1_name: str, player2_name: str):
        self.scoreboard = Scoreboard(player1_name, player2_name) 

    def won_point(self, player_name: str):
        self.scoreboard.add_point(player_name)

    def score(self) -> str:
        return str(self.scoreboard)
