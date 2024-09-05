# app/pages/contact.py

import solara

@solara.component
def Contact():
    with solara.VBox():
        solara.Markdown("# Contact Page")
        solara.Markdown("Get in touch with us through this page.")
        solara.Button("Go to Home", on_click=lambda: solara.redirect("/"))
        solara.Button("Go to About", on_click=lambda: solara.redirect("/about"))