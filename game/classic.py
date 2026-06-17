from .mode import GameMode

class ClassicMode(GameMode):

    MAX_NUMBER = 100

    def __init__(self):
        super().__init__(max_number=ClassicMode.MAX_NUMBER)

    def generate_number(self):
        self._secret_number = self._roll()
        self._attempts = 0

    def check_guess(self, guess):

        self._attempts += 1

        if guess == self._secret_number:
            return GameMode.WIN
        if guess < self._secret_number:
            return GameMode.HIGHER
        return GameMode.LOWER

    def get_display_name(self):
        return "Classic"