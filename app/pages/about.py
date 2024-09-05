# app/pages/about.py

import solara

@solara.component
def About():
    with solara.VBox():
        solara.Markdown("# About Page")
        solara.Markdown("Learn more about us on this page.")
        solara.Button("Go to Home", on_click=lambda: solara.redirect("/"))
        solara.Button("Go to Contact", on_click=lambda: solara.redirect("/contact"))