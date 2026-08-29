#!/usr/bin/python3
"""Query the Reddit API for the top hot posts of a given subreddit."""
import requests
 
 
def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.
 
    Args:
        subreddit (str): The name of the subreddit to query.
 
    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alche.top_ten:v1.0 (by /u/alche_student)"}
    params = {"limit": 10}
 
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
 
    if response.status_code != 200:
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
