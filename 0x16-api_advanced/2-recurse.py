#!/usr/bin/python3
"""function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return None
    else:
        result = response.json()
        data = result['data']['children']
        for a in data:
            hot_list.append(a['data']['title'])
        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list=host_list)
        else:
            return hot_lis
