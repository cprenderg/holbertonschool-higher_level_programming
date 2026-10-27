#!/usr/bin/env python3

"""
Praciting API calls
"""

import requests
import csv


def fetch_and_print_posts():

    URL = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(URL)

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        try:
            data = r.json()
            for post in data:
                print(post["title"])
        except:
            print("Got 200 but no data")


def fetch_and_save_posts():
    URL = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(URL)
    data_list = []

    if r.status_code == 200:
        try:
            data = r.json()
            for post in data:
                data_list.append({
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                    })
        except:
            print("Got 200 but no data")
    
    columns = ["id", "title", "body"]


    with open ("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)

        writer.writeheader()
        writer.writerows(data_list)


