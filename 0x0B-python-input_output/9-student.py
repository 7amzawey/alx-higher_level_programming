#!/usr/bin/python3
"""
This module is for a class student
"""

class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """defining class Student"""
    def __init__(self, first_name, last_name, age):
        """intiliaze the student class with three public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dict representation of the class"""
        return (class_to_json(self))
