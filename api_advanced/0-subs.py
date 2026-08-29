#!/usr/bin/python3
"""Query the Reddit API for a subreddit's subscriber count.

Contains a single function, number_of_subscribers, that returns
the total number of subscribers for a given subreddit, or 0 if
the subreddit is invalid.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit
            is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "0-subs:reddit.api.request:v1.0.0"}

    response = requests.get(
        url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
    except ValueError:
        return 0

    return data.get("data", {}).get("subscribers", 0)
