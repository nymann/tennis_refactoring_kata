from tennis_scoreboard.domain.game_states.advantage import Advantage
from tennis_scoreboard.domain.game_states.deuce import Deuce
from tennis_scoreboard.domain.game_states.early_game_lead import EarlyGameLead
from tennis_scoreboard.domain.game_states.game_state import GameState
from tennis_scoreboard.domain.game_states.i_game_state import IGameState
from tennis_scoreboard.domain.game_states.tie import Tie
from tennis_scoreboard.domain.game_states.win import Win
from tennis_scoreboard.domain.i_game_state_factory import IGameStateFactory
from tennis_scoreboard.domain.players.i_player import IPlayer


class GameStateFromTwoPlayersFactory(IGameStateFactory):
    game_states: list[GameState] = [EarlyGameLead(), Tie(), Deuce(), Advantage(), Win()]

    @classmethod
    def create_game_state(cls, p1: IPlayer, p2: IPlayer) -> IGameState:
        for game_state in cls.game_states:
            if game_state.is_in_game_state(p1, p2):
                return game_state
        raise Exception("No valid game state found")
