#!/usr/bin/python3

"""print subreddit"""

from requests import get


def top_ten(subreddit):
    """method"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    users = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}
    par = {'limit': 10}
    api_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    resp = get(api_url, headers=users, params=par)
    res = resp.json()

    try:
        inf = res.get('data').get('children')

        for x in inf:
            print(x.get('data').get('title'))

    except Exception:
        return 0
