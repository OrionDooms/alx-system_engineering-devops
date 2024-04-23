#!/usr/bin/python3
""" Using the REST API to take in a employee ID that would returns information
about his/her TODO list progress."""


import requests
import sys


def Todo_list(employee_id, url):
    user_id = "users/{}".format(employee_id)
    user_response = requests.get(url + user_id)
    name = user_response.json()
    params = {"userId": employee_id}
    list_response = requests.get(url + "todos", params=params)
    lists = list_response.json()

    data = []

    for do in lists:
        if do.get("completed") is True:
            data.append(do.get("title"))

    a = name.get("name")
    b = len(data)
    c = len(lists)
    print("Employee {} is done with tasks({}/{}):".format(a, b, c))

    for d in data:
        print("\t {}".format(d))


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    Todo_list(employee_id, url)
