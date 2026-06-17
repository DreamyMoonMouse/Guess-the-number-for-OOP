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

    @abstractmethod
    def generate_number(self) -> None:
        ...

    @abstractmethod
    def check_guess(self, guess: int) -> str:
        ...

    @abstractmethod
    def get_display_name(self):
        ...

    def get_attempts(self) -> int:
        return self._attempts

    def get_max_number(self) -> int:
        return self._max_number

    def get_secret(self)-> int:
        return self._secret_number

    def _roll(self) -> int:
        return random.randint(1, self._max_number)

    def is_in_range(self, number):
        return 1 <= number <= self._max_number