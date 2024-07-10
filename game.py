from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess_number: str):
        self.assert_illegal_value(guess_number)
        if self.is_solved(guess_number):
            return self.get_success_game_result()
        else:
            return self.get_unsolved_game_result(guess_number)

    def get_unsolved_game_result(self, guess_number):
        strikes = 0
        balls = 0
        for i in range(len(self.question)):
            if self.question.find(guess_number[i]) == i:
                strikes += 1
            elif self.question.find(guess_number[i]) > -1:
                balls += 1
        return GameResult(False, strikes, balls)

    def get_success_game_result(self):
        return GameResult(True, 3, 0)

    def is_solved(self, guess_number):
        return guess_number == self.question

    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError
        if len(guess_number) != 3:
            raise TypeError
        for ch in guess_number:
            if not ch.isdigit():
                raise TypeError
            if guess_number.count(ch) > 1:
                raise TypeError
