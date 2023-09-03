from flask import render_template, redirect, url_for
from . import todos_bp


todos = [
    {"id": 1, "label": "Walk a dog"},
]


@todos_bp.route("/")
def home():
    return render_template("todos.html", todos=todos)


@todos_bp.route("/edit/<id>")
def edit_todo(id):
    current_todo = None
    for todo in todos:
        if todo["id"] == int(id):
            current_todo = todo
            break
    return render_template("edit.html", todo=current_todo)


@todos_bp.route("/todo/<id>")
def delete_todo(id):
    for todo in todos:
        if todo['id'] == int(id):
            todos.remove(todo)
            break

    return redirect(url_for("home"))
