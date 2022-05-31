#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit.
If no results are found for the given subreddit,
the function should return None. """

from requests import request


def recurse(subreddit, hot_list=[], after=""):
    """ recursive function that returns a list
    with all hot articles for a given subreddit """
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        top = response['data']['children']
        _after = response['data']['after']
        for i in top:
            hot_list.append(i['data']['title'])
        if _after is not None:
            recurse(subreddit, hot_list, _after)
        return hot_list
    except Exception:
        return None
