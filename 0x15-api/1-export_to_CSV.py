#!/usr/bin/python3
"""Task 0.Using the REST API to take in a employee ID that would returns
information.
Task 1.Using what you did in the task #0, extend your Python script to
export data in the CSV format."""

import csv
import requests
import sys


def Get_Todo_list(employee_id, url):
    user_id = "users/{}".format(employee_id)
    user_response = requests.get(url + user_id)
    user_data = user_response.json()
    username = user_data.get("username")

    params = {"userId": employee_id}
    list_response = requests.get(url + "todos", params=params)
    lists = list_response.json()

    with open("{}.csv".format(employee_id), "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        e = employee_id
        u = username
        for data in lists:
            writer.writerow([e, u, data.get("completed"), data.get("title")])


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    Get_Todo_list(employee_id, url)
