#!/usr/bin/python3
"""Task 0.Using the REST API to take in a employee ID that would returns
information.
Task 1.Using what you did in the task #0, extend your Python script to
export data in the JSON format.
Records all tasks that are owned by this employee and put it into a json file.
"""

import json
import requests


def employee_Todo_list(Id, url):
    user_id = "users/{}".format(Id)
    user_response = requests.get(url + user_id)
    user_data = user_response.json()
    name = user_data.get("username")

    params = {"userId": Id}
    list_response = requests.get(url + "todos", params=params)
    todo_list = list_response.json()

    return {"username": name, "tasks":
            [{"task": task.get("title"), "completed": task.get("completed")}
                for task in todo_list]}


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    all_data = {}

    for Id in range(1, 11):
        all_data[Id] = employee_Todo_list(Id, url)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file, indent=4)
