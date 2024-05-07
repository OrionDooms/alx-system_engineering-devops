#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts """
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redircts=False)

    if response.status_code == 200:
        print("None")
    else:
        result = response.json()
        data = result['data']['children']
        for a in data:
            print(a['data']['title'])
