import flet as ft

class GameView:

    def __init__(self, page, on_guess, on_restart, on_menu):
        self._page = page
        self._on_guess = on_guess
        self._on_restart = on_restart
        self._on_menu = on_menu

        self._title = ft.Text("", size=24, weight=ft.FontWeight.BOLD)
        self._range = ft.Text("", size=16)
        self._input = ft.TextField(
            label="Введи число",
            keyboard_type=ft.KeyboardType.NUMBER,
            on_submit=lambda e: self._on_guess(self._input.value),
        )

        self._hint = ft.Text("", size=18)
        self._attempts = ft.Text("Попыток: 0", size=16)
        self._history = ft.Column(
            scroll=ft.ScrollMode.AUTO, height=200, spacing=5
        )

        self._dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Игра окончена"),
            content=ft.Text(""),
            actions=[
                ft.TextButton(
                    "Играть снова", on_click=lambda e: self._on_restart()
                ),
                ft.TextButton("В меню", on_click=lambda e: self._on_menu()),
            ],
        )

    def build(self, title, max_number):
        self._title.value = f"Режим: {title}"
        self._range.value = f"Диапазон: 1 – {max_number}"
        self.reset()
        return ft.SafeArea(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self._title,
                    self._range,
                    self._input,
                    ft.ElevatedButton(
                        content=ft.Text("Угадать"),
                        on_click=lambda e: self._on_guess(self._input.value),
                    ),
                    self._attempts,
                    self._hint,
                    self._history,
                ],
            )
        )

    def set_attempts(self, n):
        self._attempts.value = f"Попыток: {n}"

    def set_hint(self, text):
        self._hint.value = text

    def clear_input(self):
        self._input.value = ""
        self._input.border_color = None

    def mark_input_invalid(self):
        self._input.border_color = ft.Colors.RED

    def mark_input_valid(self):
        self._input.border_color = None

    def append_history(self, text, color=None):
        self._history.controls.append(ft.Text(text, color=color))

    def reset(self):
        self._history.controls.clear()
        self._hint.value = ""
        self._attempts.value = "Попыток: 0"
        self.clear_input()

    def show_game_over(self, message):
        self._dialog.content.value = message
        self._page.show_dialog(self._dialog)
        self._page.update()

    def close_dialog(self):
        self._page.pop_dialog()
        self._page.update()

    def update(self):
        self._page.update()