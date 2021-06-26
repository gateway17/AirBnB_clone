#!/usr/bin/python3

"""
Storage Data of instances
"""
import json
import os


class FileStorage:


    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns a diccionary of ALL objects """
        return __objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id """
        pass

    def save(self):
        """serializes __objects to the JSON file (path: _file_path)"""
        json.dumps(__objects, __file_path)

    def reload(self):
        """if the file exist, deserializes the JSON file to __objects"""
        if os.path.isfile(__file_path):
            object_json = json.loads(__file_path)
