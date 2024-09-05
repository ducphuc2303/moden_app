# app/pages/admin.py

import solara

@solara.component
def Admin():
    users = [
        {"username": "admin", "email": "admin@example.com"},
        {"username": "user1", "email": "user1@example.com"},
        {"username": "user2", "email": "user2@example.com"},
    ]

    with solara.VBox():
        solara.Markdown("# User Management")
        for user in users:
            with solara.HBox():
                solara.Text(user["username"])
                solara.Text(user["email"])
                solara.Button("Edit", on_click=lambda: solara.notify(f"Edit {user['username']}"))
                solara.Button("Delete", on_click=lambda: solara.notify(f"Deleted {user['username']}"))

# Thêm route này vào trong cấu hình route của bạn nếu người dùng là admin