from .base import BaseMode

class ClassicMode(BaseMode):

    def __init__(self):
        super().__init__(max_number=100)

    def generate_number(self) -> None:
        self._secret = self._roll()
        self._attempts = 0

    def check_guess(self, guess: int) -> str:

        self._attempts += 1

        if guess < self._secret:
            return "higher"
        elif guess > self._secret:
            return "lower"
        else:
            return "win"