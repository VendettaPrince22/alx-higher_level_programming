#!/usr/bin/python3
"""Contains a class Student"""


class Student:
    """Defines a student object
    Args:
        first_name: student first name
        last_name: student last name
        age: student age
    """
    def __inti__(self, first_name, last_name, age):
        """Initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Retrieves a dict representation of a Student instance"""
        return self.__dict__
