#!/usr/bin/python3
import requests
"""api"""


def number_of_subscribers(subreddit):
    """test subs"""
    users = {'User-agent': 'Google Chrome Version 125.0.6422.142'}
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(
            api_url,
            headers=users,
            allow_redirects=False
            )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
