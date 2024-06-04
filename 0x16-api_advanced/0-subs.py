#!/usr/bin/python3
"""api"""
import requests


def number_of_subscribers(subreddit):
    """test"""
    api_inf = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-agent": "agent_browser"},
        allow_redirects=False,
    )
    if api_inf.status_code != 200:
        return 0


return api_inf.json().get("data").get("subscribers")
