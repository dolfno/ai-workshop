import logging
import os
from turtle import st

import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN not set in environment")


def search_github(query: str) -> list:
    NUM_RESULTS = 5
    # https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-code
    search_url = f"https://api.github.com/search/code?q={query}?per_page={NUM_RESULTS}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Error from GitHub: {response.json()}")

    results = []
    for item in response.json()["items"]:
        results.append(
            {
                "name": item["name"],
                "url": item["url"],
                "html_url": item["html_url"],
            }
        )
    logging.info(f"Found {len(results)} github results")
    return results


def read_github_file(url: str) -> str:
    # https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#get-repository-content
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Error from GitHub get contents: {response.json()}")

    return response.json()["content"]
