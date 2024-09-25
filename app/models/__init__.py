#!/usr/bin/python3

from app.models.engine.db_storage import DBStorage
#from api.v1.app import app


storage = DBStorage()

storage.reload()