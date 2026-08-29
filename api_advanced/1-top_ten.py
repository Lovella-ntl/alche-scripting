#!/usr/bin/python3
"""Query the Reddit API for the top hot posts of a given subreddit."""
import requests
import time


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; alche_top_ten/1.0)"
    }
    params = {"limit": 10}

    response = None
    for attempt in range(3):
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 429:
            break
        time.sleep(1)

    if response is None or response.status_code != 200:
        print(None)
        return

    try:
        results = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not results:
        print(None)
        return

    for post in results:
        print(post.get("data", {}).get("title"))
