#!/usr/bin/python3
"""API convert to Json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    u_uesr = 'https://jsonplaceholder.typicode.com/users/' + user_id
    reqq = requests.get(u_uesr)
    u_name = reqq.json().get('username')
    tsk = u_uesr + '/todos'
    reqq = requests.get(tsk)
    tsks = reqq.json()

    all_data = {user_id: []}
    for t in tsks:
        TASK_COMPLETED_STATUS = t.get('completed')
        TASK_TITLE = t.get('title')
        all_data[user_id].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": u_name})
    with open('{}.json'.format(user_id), 'w') as x:
        json.dump(all_data, x)
