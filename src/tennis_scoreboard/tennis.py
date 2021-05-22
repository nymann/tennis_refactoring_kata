# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        result = ""
        tempScore=0
        if (self.p1points==self.p2points):
            result = self._equal()
        elif (self.p1points>=4 or self.p2points>=4):
            result = self._get_endgame_result()
        else:
            result = self._get_score()
        return result

    def _equal(self):
        return {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }.get(self.p1points, "Deuce")

    def _get_endgame_result(self):
        minusResult = self.p1points-self.p2points
        if (minusResult==1):
            return "Advantage " + self.player1Name
        elif (minusResult ==-1):
            return "Advantage " + self.player2Name
        elif (minusResult>=2):
            return  "Win for " + self.player1Name
        return "Win for " + self.player2Name

    def _get_score(self):
        result = ""
        for i in range(1,3):
            if (i==1):
                tempScore = self.p1points
            else:
                result+="-"
                tempScore = self.p2points
            result += {
                0 : "Love",
                1 : "Fifteen",
                2 : "Thirty",
                3 : "Forty",
            }[tempScore]
        return result
