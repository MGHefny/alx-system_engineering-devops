#!/usr/bin/python3
"""emp data"""

import requests
import re
import sys

api_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.match(r"^\d+$", sys.argv[1]):
            id = int(sys.argv[1])
            user_respo = requests.get(f"{api_url}/users/{id}").json()
            task_respo = requests.get(f"{api_url}/todos").json()
            name_emplo = user_respo.get("name")
            to_do = list(filter(lambda i: i.get("userId") == id, task_respo))
            comp_task = list(filter(lambda i: i.get("completed"), to_do))
            print(
                "Employee {} is done with tasks({}/{}):".format(
                    name_emplo, len(comp_task), len(to_do)
                )
            )
            if comp_task:
                for task in comp_task:
                    print("\t {}".format(task.get("title")))
