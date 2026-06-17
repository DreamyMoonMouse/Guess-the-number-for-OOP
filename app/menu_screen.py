import flet as ft
from typing import Callable
from game import ClassicMode, HardMode

class MenuScreen:

    def __init__(self, on_mode_selected: Callable[[str], None]):
        self._on_mode_selected = on_mode_selected

    def build(self) -> ft.SafeArea:
        return ft.SafeArea(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Угадай число",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text("Выбери режим игры:", size=18),
                    ft.Text(f"без лимита, до {ClassicMode.MAX_NUMBER}", size=16),
                    ft.Button(
                        content=ft.Text("Classic"),
                        on_click=lambda e: self._on_mode_selected("classic"),
                    ),
                    ft.Text(f"{HardMode.MAX_ATTEMPTS} попыток, до {HardMode.MAX_NUMBER}", size=16),
                    ft.Button(
                        content=ft.Text("Hard"),
                        on_click=lambda e: self._on_mode_selected("hard"),
                    ),
                ],
            )
        )