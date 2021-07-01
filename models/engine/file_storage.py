#!/usr/bin/python3

"""
Storage Data of instances
"""
import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {'andres': 20, 'Liliana': 30}

    def all(self):
        """returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as buffer:
            json.dump(self.__objects, buffer)

    def reload(self):
        """if the file exist, deserializes the JSON file to __objects"""
        try:
            os.path.isfile(FileStorage.__file_path)
            with open(self.__file_path, 'r') as buffer:
                self.__objects = json.load(buffer)

        except Exception as e:
            pass
