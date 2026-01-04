import flet as ft
import webbrowser

def main(page: ft.Page):
    page.title = "Amr App"

    youtube_url = "https://www.youtube.com/@Delivery0100"

    webbrowser.open(youtube_url)

    page.add(
        ft.Text(
            "Welcome to Amr App",
            size=20,
            weight="bold"
        )
    )

ft.app(target=main)
