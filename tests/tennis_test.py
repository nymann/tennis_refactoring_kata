import pytest
from tennis_scoreboard.presentation import scoreboard

from tests.tennis_unittest import test_cases, play_game

class TestTennis:

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game1(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(scoreboard.Scoreboard, p1Points, p2Points, p1Name, p2Name)
        assert score == str(game)
