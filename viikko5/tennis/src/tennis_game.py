from score import Score

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def _get_equal_score(self):
        if self.player1_score is Score.LOVE.value:
            return "Love-All"
        elif self.player1_score is Score.FIFTEEN.value:
            return "Fifteen-All"
        elif self.player1_score is Score.THIRTY.value:
            return "Thirty-All"
        else:
            return "Deuce"

    def _get_winner(self):
        if self.player1_score > self.player2_score:
            return "Win for player1"
        return "Win for player2"

    def _get_advantage(self):
        if self.player1_score > self.player2_score:
            return "Advantage player1"
        return "Advantage player2"

    def _get_player1_score(self):
        if self.player1_score is Score.LOVE.value:
            return "Love"
        elif self.player1_score is Score.FIFTEEN.value:
            return "Fifteen"
        elif self.player1_score is Score.THIRTY.value:
            return "Thirty"
        else:
            return "Forty"

    def _get_player2_score(self):
        if self.player2_score is Score.LOVE.value:
            return "Love"
        elif self.player2_score is Score.FIFTEEN.value:
            return "Fifteen"
        elif self.player2_score is Score.THIRTY.value:
            return "Thirty"
        else:
            return "Forty"

    def get_score(self):
        if self.player1_score == self.player2_score:
            score = self._get_equal_score()

        elif max(self.player1_score, self.player2_score) > Score.FORTY.value:
            score_diff = self.player1_score - self.player2_score
            if abs(score_diff) > 1:
                score = self._get_winner()
            else:
                score = self._get_advantage()

        else:
            score = f"{self._get_player1_score()}-{self._get_player2_score()}"

        return score
