# main.py

import solara
from app.pages.home import Home
from app.pages.about import About
from app.pages.contact import Contact

@solara.component
def Page():
    with solara.HBox():
        solara.Button("Home", on_click=lambda: solara.redirect("/"))
        solara.Button("About", on_click=lambda: solara.redirect("/about"))
        solara.Button("Contact", on_click=lambda: solara.redirect("/contact"))
    
    solara.Route("/", Home)
    solara.Route("/about", About)
    solara.Route("/contact", Contact)

if __name__ == "_main_":
    solara.run(Page)
# main.py

# import solara
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # Tạo engine và session
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Sử dụng hàm declarative_base() mới từ SQLAlchemy 2.0
# Base = declarative_base()

# # Hàm lấy session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# import solara
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # Tạo engine và session
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Sử dụng hàm declarative_base() mới từ SQLAlchemy 2.0
# Base = declarative_base()

# # Hàm lấy session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Định nghĩa Page hoặc kiểm tra xem bạn có cần nhập khẩu nó từ đâu không
# # Ví dụ: từ solara import Page (nếu Page là một lớp hoặc đối tượng từ Solara)