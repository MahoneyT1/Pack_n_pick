#!/usr/bin/python3
"""File storage for pick n pack,basically for code testing"""
import json


class FileStorage:
    """Serializes object and write to .json file"""

    __filename = "storage.json"
    __object = {} # object that act as the in-memory

    def all_data(self, obj=None):
        """collects all the data from the file"""

        if obj is not None:
            all_data = {}

            for key, value in self.__object.items():
                if isinstance(value, type(obj)):
                    print(value)

            # return all_data

    def new(self, obj):
        """puts object in the in-memory/session """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__object[key] = obj.to_dict() 

    def save(self):
        """saves json object to file
        use the .method to access the method"""
        
        with open(FileStorage.__filename, 'w') as write1:
            json.dump(self.__object, write1, indent=4)
            print("successfully saved")

    def reload(self):
        """reloads the written json file"""

        with open(FileStorage.__filename, 'r') as reload1:
            data = json.load(fp=reload1)

            for key, value in data.items():
                self.__object[key] = value

        return self.__object

