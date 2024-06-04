#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def recurse(subreddit, hot_list=[], after="null"):
    """function to query the reddit api"""
    index = len(hot_list)
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    next_page = {"limit": "100", "after": after}
    response = requests.get(URL, timeout=10, allow_redirects=False,
                            params=next_page)
    data = response.json()
    try:
        hot_list.append(data['data']['children'][index]
                        ['data']['title'])
        if index != 0 and index % 100 == 0:
            after = data['data']['after']
        recurse(subreddit, hot_list, after)
    except KeyError:
        if (index == 0):
            return None
        else:
            return hot_list
    except IndexError:
        return hot_list
    return hot_list
