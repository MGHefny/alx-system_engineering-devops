#!/usr/bin/python3
"""API return list"""
import requests


def recurse(subreddit, hot_list=[], x=0, after=None):
    """method"""
    api_url = "https://www.reddit.com/res/{}/hot.json".format(subreddit)
    head = {
        "user-agent":
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)"
    }
    res = requests.get(api_url, headers=head, allow_redirects=False)
    if res.status_code == 200:
        res = res.json()
        for y in res.get("data").get("children"):
            hot_list.append(y.get("data").get("title"))
        if res.get("data").get("after"):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
