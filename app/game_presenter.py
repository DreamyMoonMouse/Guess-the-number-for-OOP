from .game_view import GameView
from game import ClassicMode, HardMode, GameMode

class GamePresenter:

    def __init__(self, page, on_back_to_menu):
        self._page = page
        self._on_back_to_menu = on_back_to_menu
        self._game = None
        self._view = GameView(
            page=page,
            on_guess=self._on_guess,
            on_restart=self._on_restart,
            on_menu=self._on_menu,
        )

    def build(self, mode):

        if mode == "classic":
            self._game = ClassicMode()
        else:
            self._game = HardMode()

        return self._view.build(
            title=self._game.get_display_name(),
            max_number=self._game.get_max_number(),
        )

    def _on_guess(self, raw_value):
        guess = self._parse_input(raw_value)

        if guess is None:
            self._view.update()
            return

        result = self._game.check_guess(guess)
        self._view.set_attempts(self._game.get_attempts())
        self._view.clear_input()
        self._dispatch(result, guess)
        self._view.update()

    def _parse_input(self, raw):

        def invalid():
            self._view.mark_input_invalid()
            return None

        if raw is None or not raw.strip():
            return invalid()
        try:
            number = int(raw.strip())
        except ValueError:
            return invalid()

        if not self._game.is_in_range(number):
            return invalid()

        self._view.mark_input_valid()
        return number

    def _dispatch(self, result, guess):

        if result == GameMode.WIN:
            self._view.append_history(f"{guess} — Угадал!")
            self._view.show_game_over(
                f"Ты угадал за {self._game.get_attempts()} попыток!"
            )
        elif result == GameMode.LOSE:
            self._view.append_history(f"{guess} — Не угадал")
            self._view.show_game_over(
                f"Проигрыш! Число было {self._game.get_secret()}"
            )
        elif result == GameMode.HIGHER:
            self._view.append_history(f"{guess} — Больше")
            self._view.set_hint("Загаданное число больше")
        elif result == GameMode.LOWER:
            self._view.append_history(f"{guess} — Меньше")
            self._view.set_hint("Загаданное число меньше")

    def _on_restart(self):
        self._view.close_dialog()
        self._game.generate_number()
        self._view.reset()
        self._view.update()

    def _on_menu(self):
        self._view.close_dialog()
        self._on_back_to_menu()