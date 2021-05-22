class Player(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.points: int = 0

    def point_text(self):
        return ["Love", "Fifteen", "Thirty", "Forty"][self.points]
