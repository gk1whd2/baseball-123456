from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess_number: str):
        self.assert_illegal_value(guess_number)
        if guess_number == self.question:
            return GameResult(True, 3, 0)
        else:
            return GameResult(False, 0,0)

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
