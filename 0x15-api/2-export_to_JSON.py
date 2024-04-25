#!/usr/bin/python3
"""
Task 0.Using the REST API to take in a employee ID that would returns
information.
Task 1.Using what you did in the task #0, extend your Python script to
export data in the JSON format.
Records all tasks that are owned by this employee and put it into a json file.
"""

import json
import requests
import sys


def Export_Todo_list(employee_id, url):
    user_id = "users/{}".format(employee_id)
    user_response = requests.get(url + user_id)
    user_data = user_response.json()
    name = user_data.get("username")

    params = {"userId": employee_id}
    list_response = requests.get(url + "todos", params=params)
    todo_list = list_response.json()

    with open("{}.json".format(employee_id), 'w') as file:
        json.dump({employee_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": name}
            for task in todo_list]}, file)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    Export_Todo_list(employee_id, url)
