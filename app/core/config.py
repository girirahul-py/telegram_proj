# app/core/config.py

"""Configuration module for GitHub API integration."""

import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is not set.")