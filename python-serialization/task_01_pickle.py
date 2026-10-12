#!/usr/bin/env python3

""" This module handles creates and prints CustomObject class """

import pickle


class CustomObject:

    """ CustomObject class """

    def __init__(self, name, age, is_student):

        """ Initialises with name, age and is_student """

        self.name = name
        self.age = age
        self.is_student = is_student
        self.dict = {
            "Name": self.name,
            "Age": self.age,
            "Is Student": self.is_student
        }

    def display(self):

        """ Prints information about itself """

        for key, value in self.dict.items():
            print(f"{key}: {value}")

    def serialize(self, filename):

        """ Serializes data of self with pickle """

        with open(filename, "wb") as f:
            pickle.dump(self.dict, f)

    @classmethod
    def deserialize(cls, filename):

        """ Deserializes with pickle and creates new CustomObject """

        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
            if not isinstance(data, dict):
                return None
            if isinstance(data["Name"], str):
                if isinstance(data["Age"], int):
                    if isinstance(data["Is Student"], bool):
                        return cls(
                            data["Name"],
                            data["Age"],
                            data["Is Student"])
            return None
        except (
            OSError,
            pickle.UnpicklingError,
            EOFError,
            AttributeError,
            ImportError,
            IndexError,
            TypeError,
            ValueError,
        ):
            return None
