from pathlib import Path
from flask import Flask

PROJECT_DIR = Path(__file__).resolve().parent

def create_app():
    app = Flask(
        __name__,
        template_folder=str(PROJECT_DIR / "src" / "templates"),
        static_folder=str(PROJECT_DIR / "src" / "static"),
    )

    # Configuración
    app.config.from_object("config.Config")

    # Registrar rutas / blueprints
    from src.controllers.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app

if __name__ == "__main__":
    app_run = create_app()
    app_run.run()