#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redircts=False)
    if response.status_code == 200:
        results = response.json().get("data")
        
