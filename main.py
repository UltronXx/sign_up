import flet as ft
from anyio.abc import value
from flet import (
    Page,
    Container,
    Row, Column,
    Card,
    Image,
    MainAxisAlignment,
    CrossAxisAlignment,
    Text,
    TextField
)

from pathlib import Path

assets = f"{Path(__file__).parent}/scr/assets"

def main(page: Page) -> None:
    page.title = "Sign Up"

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.window.height = 900
    page.window.width = 650

    page.theme_mode = "light"
    page.bgcolor = "#EBECF1"

    page.fonts = {
        "bold": "fonts/MonaSans-Bold.ttf",
        "regular": "fonts/MonaSans-Regular.ttf",
        "medium": "fonts/MonaSans-Medium.ttf",
        "semi bold": "fonts/MonaSans-SemiBold.ttf",
    }

    def check_box(e: ft.ControlEvent) -> None:
        icon = e.control.content.controls[0]
        icon.src = "icons/uncheck.svg" if icon.src == "icons/check.svg" else "icons/check.svg"
        keep_me_signed_in.update()

    def password_reveal(e: ft.ControlEvent) -> None:
        icon = e.control.content
        icon.src = "icons/see.svg" if icon.src == "icons/hide.svg" else "icons/hide.svg"
        password_input.password = False if password_input.password == True else True
        password_suffix_icon.update()
        password_input.update()

    keep_me_signed_in = Container(
        content=Row(
            spacing=5,
            controls=[
                Image(
                    src="icons/uncheck.svg",
                    scale=0.8,
                    color="#355CE0"
                ),
                Text(
                    value="Keep me signed in",
                    font_family="medium",
                ),
            ]
        ),
        on_click=lambda e: check_box(e)
    )

    password_suffix_icon = Container(
            Image(
            src="icons/hide.svg",
            scale=0.5,
            color="#616772"
        ),
        on_click=lambda e: password_reveal(e)
    )

    password_input = TextField(
        border_radius=9,
        border_width=1.5,
        password=True,
        # can_reveal_password=True,
        suffix_icon=password_suffix_icon,
        border_color="#CECECE",
        focused_border_color="#355CE0",
        focused_border_width=2,
        text_style=ft.TextStyle(
            font_family="medium"
        )
    )

    def change_bgcolor(e) -> None:
        google_sign_in.bgcolor = "#F3F8FE" if google_sign_in.bgcolor is None else None
        google_sign_in.update()

    google_sign_in = Container(
        height=50,
        border_radius=9,
        on_hover=change_bgcolor,
        on_click=lambda _: print(),
        border=ft.border.all(
            width=1.5,
            color="#CECECE"
        ),
        content=Row(
            alignment=MainAxisAlignment.CENTER,
            spacing=5,
            controls=[
                Image(
                    src="icons/google_icon.png",
                    scale=0.8
                ),
                Text(
                    value="Sign in with Google",
                    font_family="medium",
                    size=16, color="#1D1D1F"
                ),
            ]
        )
    )

    page.add(
        Card(
            height=640,
            width=400,
            color="#ffffff",
            elevation=20,
            shadow_color="#EBECF1",
            content=Container(
                padding=ft.padding.only(left=25, top=30, right=25, bottom=20),
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Container(
                            height=50,
                            width=50,
                            border_radius=30,
                            bgcolor="#F3F8FE",
                            content=Image(
                                src="icons/user.svg",
                                scale=0.5,
                                color="#355CE0"
                            )
                        ),
                        Container(
                            padding=ft.padding.only(top=10, bottom=20),
                            content=Column(
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    Text(
                                        value="Welcome back!",
                                        font_family="medium",
                                        color="#1D1D1F",
                                        size=22
                                    ),
                                    Text(
                                        value="Sign In to access your dashboard,\n"
                                              "settings and projects.",
                                        font_family="regular",
                                        text_align=ft.TextAlign.CENTER,
                                        color="#616772",
                                        size=16
                                    ),
                                ]
                            )
                        ),
                        google_sign_in,
                        Container(
                            padding=ft.padding.only(top=10, bottom=10),
                            content=Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Container(height=1.5, width=135, bgcolor="#CECECE"),
                                    Text(
                                        value="or", size=16,
                                        font_family="medium",
                                        color="#616772"
                                    ),
                                    Container(height=1.5, width=135, bgcolor="#CECECE"),
                                ]
                            ),
                        ),
                        Container(
                            content=Column(
                                spacing=20,
                                controls=[
                                    TextField(
                                        border_radius=9,
                                        border_width=1.5,
                                        border_color="#CECECE",
                                        focused_border_color="#355CE0",
                                        focused_border_width=2,
                                        text_style=ft.TextStyle(
                                            font_family="medium"
                                        )
                                    ),
                                    password_input,
                                ]
                            )
                        ),
                        Container(
                            padding=ft.padding.only(top=15, bottom=15),
                            content=Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    keep_me_signed_in,
                                    Text(
                                        value="Forgot password?",
                                        font_family="medium",
                                        color="#355CE0"
                                    ),
                                ]
                            ),
                        ),
                        Container(
                            height=50,
                            bgcolor="#355CE0",
                            border_radius=9,
                            alignment=ft.alignment.center,
                            content=Text(
                                value="Sign In",
                                font_family="regular",
                                size=16,
                                color="#F5F5F7"
                            ),
                        ),
                        Container(
                            padding=ft.padding.only(top=15),
                            content=Row(
                                alignment=MainAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    Text(
                                        value="Don't have an account?",
                                        font_family="regular",
                                        color="#616772"
                                    ),
                                    Text(
                                        value="Sign Up",
                                        font_family="medium",
                                        color="#355CE0"
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )
        )
    )
    page.update()

if __name__ == '__main__':
    ft.app(target=main, assets_dir=assets)
