from .mode import GameMode

class HardMode(GameMode):
    MAX_ATTEMPTS = 7
    MAX_NUMBER = 333

    def __init__(self):
        super().__init__(max_number=HardMode.MAX_NUMBER)

    def generate_number(self):
        self._secret_number = self._roll()
        self._attempts = 0

    def check_guess(self, guess: int) -> str:
        self._attempts += 1

        if guess == self._secret_number:
            return GameMode.WIN

        if self._attempts >= HardMode.MAX_ATTEMPTS:
            return GameMode.LOSE

        if guess < self._secret_number:
            return GameMode.HIGHER

        return GameMode.LOWER

    def get_display_name(self):
        return f"Hard (макс. {HardMode.MAX_ATTEMPTS} попыток)"