#!/usr/bin/python3
"""Student module: serialization and deserialization example.
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

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    Defaults to None (include all attributes).

        Returns:
            dict: Dictionary with the student's attributes filtered by attrs.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with the given

        Args:
            json (dict): Dictionary with new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
