#!/usr/bin/python3
"""api"""

from requests import get
import sys

def number_of_subscribers(subreddit):
    """test subscriber"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    users = {'User-Agent': 'Google Chrome V 125.0.6422.142'}
    resp = get(api_url, headers=users)
    res = resp.json()
    try:
        return res.get('data').get('subscribers')
    except Exception:
        return 0