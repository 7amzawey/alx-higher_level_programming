#!/usr/bin/python3
"""
this module is for class Base
"""

import json


class Base:
    """calss Base will be the base of all other calsses in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initilize an id and manage this attribute in all future classes.
        Args:
            @id: is the id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the json reperesentation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        elif (list_dictionaries):
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of list_objs"""
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of dictionaries"""
        if not json_string or (json_string is None):
            return []
        else:
            return [json.loads(json_string)]

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all the attributes"""
        from models.square import Square
        from models.rectangle import Rectangle
        if cls is Rectangle:
            new = Rectangle(3, 3)
        if cls is Square:
            new = Square(3)
        if cls is None:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        from os import path
        f = "{}.json".format(cls.__name__)
        if not path.isfile(f):
            return []
        with open(f, "r", encoding="utf-8") as f2:
            data = cls.from_json_string(f2.read())
            return [cls.create(**d) for d in data[0]]
