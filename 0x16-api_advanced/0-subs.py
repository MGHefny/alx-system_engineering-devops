#!/usr/bin/python3
"""api"""
import requests


def number_of_subscribers(subreddit):
    """test"""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    head = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}

    try:
        resp = requests.get(api_url, headers=head)
        if resp.status_code == 200:
            inf = resp.json()
            return inf['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print("error", e)
        return 0