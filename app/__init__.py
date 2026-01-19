from flask import Flask
from flask_cors import CORS

from app.routes.home import home_bp
from app.routes.admin import admin_bp
from app.routes.user import user_bp
from app.routes.lifeguard import lifeguard_bp


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    CORS(app)

    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(lifeguard_bp, url_prefix='/lifeguard')

    return app
