#!/usr/bin/python3
"""csv"""
import csv
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

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        for tsk in tsks:
            comp = tsk.get('completed')
            t_tsk = tsk.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, u_name, comp, t_tsk))
