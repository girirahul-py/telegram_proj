# app/core/github_client.py

""" GITHUB API client module."""

import requests
from app.core.config import GITHUB_HEADERS

BASE_URL = "https://api.github.com"

def get(url):
    return requests.get(f"{BASE_URL}{url}", headers=GITHUB_HEADERS)

def post(url, data=None):
    return requests.post(f"{BASE_URL}{url}", json=data, headers=GITHUB_HEADERS)
