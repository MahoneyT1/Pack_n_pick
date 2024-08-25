#!/usr/bin/python3
"""Class storage to manage storing data"""
import os
from sqlachemy import create_engine

class DBStorage:
    """Class storage representation """

    def __init__(self):
        """initialize the database connection"""

        connection_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(os.get)

