import flet as ft
from app import GameApp

def main(page: ft.Page):
    game_app = GameApp()
    game_app.build(page)


if __name__ == "__main__":
    ft.run(main)