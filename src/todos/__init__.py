from flask import Blueprint

todos_bp = Blueprint(
    "todos_bp", __name__,
    static_folder="static",
    static_url_path="/todos/static",
    template_folder="templates"
)

from src.todos import todos
