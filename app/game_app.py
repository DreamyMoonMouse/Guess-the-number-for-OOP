import flet as ft
from .menu_screen import MenuScreen
from .game_presenter import GamePresenter

class GameApp:

    def __init__(self):
        self._page: ft.Page | None = None
        self._menu_screen: MenuScreen | None = None
        self._game_screen: GamePresenter | None = None

    def build(self, page: ft.Page):
        self._page = page
        self._page.title = "Игра 'Угадай число'"
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self._page.window.width = 480
        self._page.window.height = 720
        self._menu_screen = MenuScreen(on_mode_selected=self._start_game)
        self._game_screen = GamePresenter(
            page=self._page,
            on_back_to_menu=self._show_menu,
        )

        self._show_menu()

    def _show_menu(self):
        self._page.controls.clear()
        self._page.add(self._menu_screen.build())
        self._page.update()

    def _start_game(self, mode: str):
        self._page.controls.clear()
        self._page.add(self._game_screen.build(mode))
        self._page.update()