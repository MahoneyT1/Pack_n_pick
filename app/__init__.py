#!/usr/bin/python3
"""Flask app instance instantiation"""

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_migrate import Migrate


from app.api.v1.views import app_views
from app.PacknPick_Frontend.routes.login import login_view
from app.PacknPick_Frontend.routes.logout import logout_view
from app.PacknPick_Frontend.routes.homepage import home_page_view
from app.PacknPick_Frontend.routes.registration import register_user
from app.PacknPick_Frontend.routes.add_to_cart import views
from app.PacknPick_Frontend.routes.admin import admin
login = LoginManager()

@login.user_loader
def user_loader(customer_id):
    from app.models.customers import Customer
    from app.models import storage
    from app.models.engine.db_storage import DBStorage

    return storage.get(Customer, customer_id)

def create_app():
    from app.models import storage
    from app.models.engine.db_storage import DBStorage

    app = Flask(__name__, static_folder='PacknPick_Frontend/static', template_folder='PacknPick_Frontend/templates')
    app.config['SECRET_KEY'] = 'you-will-never-guess'
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing purposes
    csrf = CSRFProtect(app)

    login.init_app(app)
    login.login_view = 'login'

    csrf.init_app(app)
    app.register_blueprint(app_views)
    app.register_blueprint(login_view)
    app.register_blueprint(home_page_view)
    app.register_blueprint(logout_view)
    app.register_blueprint(register_user)
    app.register_blueprint(views)
    app.register_blueprint(admin)

    db_storage = DBStorage()

    migrate = Migrate(app, db_storage.get_engine())

    #from PacknPick_Frontend.views.login import home

    return app

app = create_app()
for rule in app.url_map.iter_rules():
    print(f"Endpoint: {rule.endpoint} - Route: {rule.rule}")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
