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
        self.updated_at 
