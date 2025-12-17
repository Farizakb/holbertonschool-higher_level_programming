#!/usr/bin/env python3
"""
Pickling custom classes module.
"""

import pickle


class CustomObject:
    """
    CustomObject class for serialization using pickle.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display object attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file.

        Args:
            filename (str): File to save the object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): File to load the object from.

        Returns:
            CustomObject or None
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except (OSError, pickle.PickleError, EOFError):
            return None
