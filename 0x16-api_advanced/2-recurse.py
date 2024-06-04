#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Base URL for the subreddit's hot posts """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Add the titles of the posts to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Get the 'after' value for the next page of results
        after = data['data']['after']

        if after is not None:
            # Recursive call to get the next page of results
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
