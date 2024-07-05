#!/usr/bin/python3
"""
Fetches 10 most recent commits from GitHub repo using the GitHub API.
Usage: ./100-github_commits.py <repository name> <owner name>
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {'per_page': 10}  # Limiting to 10 most recent commits

    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
