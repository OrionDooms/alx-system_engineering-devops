#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list=host_list)
        else:
            return hot_list
    else:
        return None
