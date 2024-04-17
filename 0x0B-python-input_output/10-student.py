#!/usr/bin/python3
"""
This module is for a class student
"""


class Student:
    """defining class Student"""
    def __init__(self, first_name, last_name, age):
        """intiliaze the student class with three public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dict representation of the class"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dic[key] = value
        return my_dic
