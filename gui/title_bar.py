import flet as ft


class Titlebar(ft.UserControl):
    def __init__(
        self,
        window_title: str = "",
        closable: bool = True,
        hidden: bool = False,
        visible: bool = True,
        current_version: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.window_title = window_title
        self.visible = visible
        self.closable = closable
        self.hidden = hidden
        self.version = current_version

    def minimize(self):
        self.page.window_minimized = True
        self.page.update()

    def build(self):
        if self.hidden:
            return ft.Row(
                [
                    ft.WindowDragArea(
                        ft.Container(
                            bgcolor=ft.colors.TRANSPARENT, padding=10, margin=0
                        ),
                        expand=True,
                    ),
                ]
            )
        else:
            return ft.Row(
                [
                    ft.WindowDragArea(
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(f"{self.window_title}"),
                                    ft.Text(
                                        f"{self.version}", color=ft.colors.BLUE_GREY
                                    ),
                                ]
                            ),
                            bgcolor=ft.colors.TRANSPARENT,
                            padding=10,
                            margin=0,
                        ),
                        expand=True,
                    ),
                    ft.IconButton(
                        ft.icons.PHOTO_SIZE_SELECT_SMALL,
                        on_click=lambda _: self.minimize(),
                        tooltip="Minimize",
                    ),
                    ft.IconButton(
                        ft.icons.CLOSE,
                        on_click=lambda _: self.page.window_close(),
                        tooltip="Close",
                    )
                    if self.closable
                    else ft.Container(),
                ],
                visible=self.visible,
            )
