from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():  # RuntimeError: Working outside of application context.
        from . import todos

        app.register_blueprint(todos.todos_bp)

        return app
