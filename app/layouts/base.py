# app/layouts/base.py

import solara
import solara.lab as lab
from typing import List, Any

@solara.component
def BaseLayout(is_logged_in: bool, children: List[Any] = []):
    with solara.AppLayout() as layout:
        with solara.AppBar():  # Thanh trên cùng với công tắc chủ đề
            lab.ThemeToggle()
            if is_logged_in:
                solara.Button("Logout", on_click=lambda: solara.redirect("/logout"))
        with solara.Sidebar():  # Thanh bên với các nút điều hướng
            if is_logged_in:
                solara.Button("Home", on_click=lambda: solara.redirect("/"))
                solara.Button("About", on_click=lambda: solara.redirect("/about"))
                solara.Button("Contact", on_click=lambda: solara.redirect("/contact"))
        with solara.Div():  # Nội dung chính của ứng dụng
            solara.App(children)
    return layout