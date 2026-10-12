#!/usr/bin/env python3

""" This module handles creates and prints CustomObject class """

import pickle


class CustomObject:

    """ CustomObject class """

    def __init__(self, name="", age=0, is_student=True):

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

        with open(filename, "rb") as f:
            data = pickle.load(f)
        return cls(data["Name"], data["Age"], data["Is Student"])
