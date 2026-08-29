#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "reddit-api-project/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    for post in data["data"]["children"][:10]:
        print(post["data"]["title"])
