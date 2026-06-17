from abc import ABC, abstractmethod
import random

class GameMode(ABC):
    WIN = "win"
    LOSE = "lose"
    HIGHER = "higher"
    LOWER = "lower"

    def __init__(self, max_number):
        self._secret_number: int = 0
        self._attempts: int = 0
        self._max_number: int = max_number
        self.generate_number()

    def generate_number(self):
        self._secret_number = self._roll()
        self._attempts = 0

    @abstractmethod
    def check_guess(self, guess: int):
        ...

    @abstractmethod
    def get_display_name(self):
        ...

    def get_attempts(self):
        return self._attempts

    def get_max_number(self):
        return self._max_number

    def get_secret(self):
        return self._secret_number

    def _roll(self):
        return random.randint(1, self._max_number)

    def is_in_range(self, number):
        return 1 <= number <= self._max_number