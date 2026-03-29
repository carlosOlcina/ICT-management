from pathlib import Path
from flask import Flask
from .extensions import db, migrate
from .controllers.auth import auth_bp
from .models.user import User
from .models.company import Company
from .models.equipment import Equipment
from .models.software import Software

PROJECT_DIR = Path(__file__).resolve().parent

def create_app():
  app = Flask(
    __name__,
    template_folder=str(PROJECT_DIR / "templates"),
    static_folder=str(PROJECT_DIR / "static"),
  )

  app.config.from_object("src.config.Config")

  db.init_app(app)
  migrate.init_app(app, db)

  app.register_blueprint(auth_bp)

  return app

if __name__ == "__main__":
  app_run = create_app()
  app_run.run()
