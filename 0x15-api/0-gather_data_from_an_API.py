#!/usr/bin/python3
""" Using the REST API to take in a employee ID that would returns information
about his/her TODO list progress."""


import requests
import sys


def Get_Todo_list(employee_id, url):
    user_id = "users/{}".format(employee_id)
    user_response = requests.get(url + user_id)

    name = user_response.json()

    params = {"userId": employee_id}

    list_response = requests.get(url + "todos", params=params)

    lists = list_response.json()

    completed = []

    for do in lists:
        if do.get("completed") is True:
            completed.append(do.get("title"))

    a = name.get("name")
    b = len(completed)
    c = len(lists)

    print("Employee {} is done with tasks({}/{})".format(a, b, c))

    for complete in completed:
        print("\t {}".format(complete))


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    Get_Todo_list(employee_id, url)
