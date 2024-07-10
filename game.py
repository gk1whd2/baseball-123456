class Game:
    def __init__(self):
        pass

    def guess(self, guessNumber: str):
        if guessNumber is None:
            raise TypeError

        if len(guessNumber) != 3:
            raise TypeError

        for ch in guessNumber:
            if not ch.isdigit():
                raise TypeError
            if guessNumber.count(ch) > 1:
                raise TypeError
