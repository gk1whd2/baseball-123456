class Game:
    def __init__(self):
        pass

    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError

        if len(guessNumber) != 3:
            raise TypeError
