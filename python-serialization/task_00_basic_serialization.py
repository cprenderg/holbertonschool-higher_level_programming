#!/usr/bin/env python3

""" This module handles Python dictionaries and JSON files """

import json


def serialize_and_save_to_file(data, filename):

    """ Serialises a Python dictory and saves to a JSON file """

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):

    """ Deserialises a JSON file and prints it as a Python dictionary """

    with open(filename, "r") as f:
        loaded_data = json.load(f)
    return loaded_data
