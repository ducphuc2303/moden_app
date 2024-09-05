# app/pages/login.py

import solara

@solara.component
def Login():
    username, set_username = solara.use_state("")
    password, set_password = solara.use_state("")
    error_message, set_error_message = solara.use_state("")

    def handle_login():
        if username == "admin" and password == "password":
            solara.notify("Login successful!")
            set_logged_in(True)
            solara.redirect("/")
        else:
            set_error_message("Invalid username or password")

    with solara.VBox():
        solara.Markdown("## Login")
        solara.Text("Username", value=username, on_value=set_username)
        solara.Password("Password", value=password, on_value=set_password)
        if error_message:
            solara.Alert(error_message, type="error")
        solara.Button("Login", on_click=handle_login)
        solara.Markdown("[Forgot Password?](#)")

# Thêm các component khác như Register, ForgotPassword...