#!/usr/bin/python3
"""API todo lists employee"""
import json
import requests
import sys


if __name__ == '__main__':
    u_uesr = "https://jsonplaceholder.typicode.com/users"
    reqq = requests.get(u_uesr)
    u = reqq.json()
    all_user = {}
    for user in u:
        user_id = user.get('id')
        USERNAME = user.get('username')
        u_uesr = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                 user_id)
        u_uesr = u_uesr + '/todos/'
        reqq = requests.get(u_uesr)
        tsks = reqq.json()
        all_user[user_id] = []
        for tsk in tsks:
            TASK_COMPLETED_STATUS = tsk.get('completed')
            TASK_TITLE = tsk.get('title')
            all_user[user_id].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
    with open('todo_all_employees.json', 'w') as x:
        json.dump(all_user, x)
