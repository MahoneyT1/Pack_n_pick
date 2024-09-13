#!/usr/bin/python3
"""Flask app instance instantiation"""

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_migrate import Migrate


from api.v1.views import app_views

login = LoginManager()

@login.user_loader
def user_loader(user_id):
    from models.user import User
    from models import storage
    from models.engine.db_storage import DBStorage
    session = storage.__session
    return session.query(User).filter_by(id=user_id).first()

def create_app():
    from models import storage
    from models.engine.db_storage import DBStorage

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing purposes
    csrf = CSRFProtect(app)

    login.init_app(app)
    csrf.init_app(app)
    app.register_blueprint(app_views)

    db_storage = DBStorage()

    migrate = Migrate(app, db_storage.get_engine())

    return app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
