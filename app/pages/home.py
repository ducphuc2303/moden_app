# app/pages/home.py

import solara
# from app.components.chart import LineChart, BarChart

@solara.component
def Home():
    search_term, set_search_term = solara.use_state("")
    data = ["Product A", "Product B", "Product C"]

    def handle_search():
        solara.notify(f"Searching for {search_term}")

    with solara.VBox():
        solara.Markdown("# Home Page")
        solara.Text("Search", value=search_term, on_value=set_search_term)
        solara.Button("Search", on_click=handle_search)

        solara.Markdown("### Sales Over Years")
        LineChart()
        
        solara.Markdown("### Sales by Product")
        BarChart()
        
        solara.Button("Go to About", on_click=lambda: solara.redirect("/about"))
        solara.Button("Go to Contact", on_click=lambda: solara.redirect("/contact"))
# app/pages/home.py

# import solara

# @solara.component
# def Home():
#     with solara.VBox():
#         solara.Markdown("# Home Page")
#         solara.Button("Go to About", on_click=lambda: solara.redirect("/about"))
#         solara.Button("Go to Contact", on_click=lambda: solara.redirect("/contact"))