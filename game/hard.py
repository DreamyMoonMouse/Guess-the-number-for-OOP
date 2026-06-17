from .base import BaseMode

class HardMode(BaseMode):

    def __init__(self):
        super().__init__(max_number=333)

    def generate_number(self) -> None:
        self._secret = self._roll()
        self._attempts = 0