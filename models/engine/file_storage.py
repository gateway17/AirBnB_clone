#!/usr/bin/python3

"""
Storage Data of instances
"""
import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {'andres':20, 'Liliana':30}

    def all(self): # Que pasa si el diccionario esta vacio, 2) No me pasan un diccionario,
        """returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            self.__objects[obj.__class__.__name__ + "." + obj.id] = obj



objeto = FileStorage()
print(objeto.all())
print("----")
objeto2 = FileStorage()
objeto2. mi_nombre = "Andres"
objeto.new(objeto2)
print(objeto.__objects)
