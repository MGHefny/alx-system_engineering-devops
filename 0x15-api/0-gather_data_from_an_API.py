#!/usr/bin/python3
"""emp data"""

import requests
import sys
import re

api_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.match(r"^\d+$", sys.argv[1]):
            id = int(sys.argv[1])
            user_respo = requests.get(f"{api_url}/users/{id}").json()
            task_respo = requests.get(f"{api_url}/todos").json()
            name_emplo = user_respo.get("name")
            to_do = [task for task in task_respo if task.get("userId") == id]
            comp_task = [task for task in to_do if task.get("completed")]

            print(
                "Employee {} is done with to_do({}/{}):".format(
                    name_emplo, len(comp_task), len(to_do)
                )
            )
            if comp_task:
                for task in comp_task:
                    print("\t {}".format(task.get("title")))
