from flask import Flask
from app.models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    def before_request():
        app.jinja_env.cache={}
    app.before_request(before_request)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
