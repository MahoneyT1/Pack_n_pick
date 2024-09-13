#!/usr/bin/python3
"""Basemodel structure representation
views/models inherits from basemodel and initialize new objects
"""

from uuid import uuid4
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import json


Base = declarative_base()


class BaseModel:
    """BaseModel representaton"""

    id = Column(String(60), primary_key=True, unique=True,
                default=lambda: str(uuid4()),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize new instance with args"""

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                            if isinstance(value, str) else value)

            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()

    def to_dict(self):
        """converts basemodel instance to a dict"""

        new_dict = {}
        new_dict = {
            'id': self.id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        new_dict.update({key: value for key, value in self.__dict__.items() 
                            if not key in ['id', 'created_at', 'updated_at']})
        
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']

        return new_dict

    def __str__(self) -> str:
        """Return only the class name and class id"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
