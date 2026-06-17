from abc import ABC, abstractmethod
import random

class BaseMode(ABC):

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

        @property
        def attempts(self) -> int:
            return self._attempts

        @property
        def max_number(self) -> int:
            return self._max_number

        def _roll(self) -> int:
            return random.randint(1, self._max_number)