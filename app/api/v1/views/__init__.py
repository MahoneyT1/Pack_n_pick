from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/')


from app.api.v1.views.orders import *
from app.api.v1.views.users import *
from app.api.v1.views.products import *
from app.api.v1.views.suppliers import *
#from PacknPick_Frontend.views.homepage import *