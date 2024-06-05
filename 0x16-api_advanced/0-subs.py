#!/usr/bin/python3
"""api"""
import requests


def number_of_subscribers(subreddit):
    """test"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    res = requests.get(
        url,
        headers=head,
        allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0