#!/usr/bin/python3
"""
this module is for class Base
"""

import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """this one seriliazes in CSV which basically means that i am going
        am going to turn this class list of objects to a json-like string
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [
                        [o.id, o.width, o.height, o.x, o.y]
                        for o in list_objs]
            elif cls is Square:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
        classname = cls.__name__
        filename = "{}.csv".format(classname)
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """this file deserilizas in csv so
        it's going to load from a string to make a list"""
        from models.square import Square
        from models.rectangle import Rectangle
        lis = []
        with open("{}.csv".format(cls.__name__), "r") as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {
                        "id": row[0], "width": row[1],
                        "height": row[2],
                        "x": row[3], "y": row[4]
                        }
                elif cls is Square:
                    d = {
                        "id": row[0], "size": row[1], "x": row[2], "y": row[3]
                        }
                lis.append(cls.create(**d))
        return lis
