#!/usr/bin/python3
#Using the REST API to take in a employee ID that would returns information
#about his/her TODO list progress.
import requests
import sys

#This function Get_todo_list Takes in a argument and url.
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
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(name.get("name"), len(completed), len(lists)))

    for complete in completed:
        print("\t {}".format(complete))

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    Get_Todo_list(employee_id, url)
