#!/usr/bin/env python3


import pickle


class CustomObject:
    def __init__(self, name="", age=0, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.dict = {
            "Name": self.name,
            "Age": self.age,
            "Is Student": self.is_student
        }

    def display(self):
        for key, value in self.dict.items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.dict, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            data = pickle.load(f)
        return cls(data["Name"], data["Age"], data["Is Student"])
