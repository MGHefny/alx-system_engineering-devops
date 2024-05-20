#!/usr/bin/python3
"""csv"""
import csv
import requests
import sys

api_url = "https://jsonplaceholder.typicode.com"
if __name__ == "__main__":
    user_id = sys.argv[1]
    user_respo = requests.get(f"{api_url}/users/{id}").json()
    req = requests.get(user_respo)
    u_name = req.json().get("username")
    task_respo = requests.get(f"{api_url}/todos").json()
    req = requests.get(task_respo)
    tks = req.json()

    with open("{}.csv".format(user_id), "w") as csvfile:
        for task_respo in tks:
            comp = task_respo.get("completed")
            title_task = task_respo.get("title")
            csvfile.write(
                '"{}","{}","{}","{}"\n'.format(
                           user_id, u_name, comp, title_task))
