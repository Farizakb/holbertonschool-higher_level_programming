#!/usr/bin/python3
"""Student module
Defines a Student class with public attributes and JSON representation.
"""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary with the student's attributes.
        """
        return self.__dict__.copy()
