#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function to query the reddit api"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(URL, timeout=1, allow_redirects=False)
    data = response.json()
    try:
        return data['data']['subscribers']
    except KeyError:
        return 0
