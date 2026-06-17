from .base import BaseMode

class HardMode(BaseMode):
    MAX_ATTEMPTS = 7

    def __init__(self):
        super().__init__(max_number=333)

    def generate_number(self) -> None:
        self._secret = self._roll()
        self._attempts = 0

    def check_guess(self, guess: int) -> str:
        self._attempts += 1

        if guess == self._secret:
            return "win"

        if self._attempts >= HardMode.MAX_ATTEMPTS:
            return f"lose:{self._secret}"

        if guess < self._secret:
            return "higher"

        return "lower"