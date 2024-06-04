#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit):
    """function to query the reddit api"""
    posts = []
    URL = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    response = requests.get(URL, timeout=1, allow_redirects=False)
    data = response.json()
    try:
        for i in range(10):
            posts.append(data['data']['children'][i]['data']['title'])
        for i in range(10):
            print(posts[i])
    except KeyError:
        print("None")
