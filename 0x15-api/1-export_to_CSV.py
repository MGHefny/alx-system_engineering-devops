#!/usr/bin/python3
"""csv"""
import csv
import requests
import sys
api_url = "https://jsonplaceholder.typicode.com"
if __name__ == '__main__':
    user_id = sys.argv[1]
    user_respo = f'{api_url}/users/{user_id}'
    req = requests.get(url_user)
    u_name = req.json().get('username')
    task = f'{url_user}/todos'
    req = requests.get(task)
    tasks = req.json()

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        for task in tasks:
            comp = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, u_name, comp, title_task))
