#!/usr/bin/env python3

""" Coverting CSV Data to JSON Format """

import csv
import json


def convert_csv_to_json(filename):

    """ Coverts CSV Data to JSON Format """

    try:
        with open(filename, mode='r') as csvfile:
            data = list(csv.DictReader(csvfile))
    except FileNotFoundError:
        return False

    with open("data.json", mode="w") as jsonfile:
        json.dump(data, jsonfile)

    return True
