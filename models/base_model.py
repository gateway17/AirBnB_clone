#!/usr/bin/python3

"""
This is the Base class
"""

class BaseModel:

    def __init__(self, id, created_at, updated_at):
        """
        Inicialize first values for
        atributes: id, created_at, updated_at
        """

        self.id = id.uuid
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """
        returns string type representation of object instance
        """
        Base_Model.__name__
        return "[{}] ({}) {}".format(self., self.id, self.__dict__)

[<class name>] (<self.id>) <self.__dict__>