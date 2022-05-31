#!/usr/bin/python3
""" Module holds function that queries the Reddit API
and returns the number of subs """
from requests import request


def number_of_subscribers(subreddit):
    """ function that returns the number of subs in Reddit API """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        subs = response['data']['subscribers']
        return subs
    except Exception:
        return 0
