#!/usr/bin/python3
"""api"""

import requests
from requests import get


def number_of_subscribers(subreddit):
    """test subscriber"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    users = {
        "User-Agent":
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)"
    }
    resp = get(api_url, headers=users)
    res = resp.json()
    try:
        return res.get("data").get("subscribers")
    except Exception:
        return 0
