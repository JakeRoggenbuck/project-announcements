import requests
from plrs import Lexer, EMPTY_TOKEN, Settings, Tokens
from typing import List, Union


class Repo:
    """Repo is an object that represents a github repo

    Contruct:

        # From the username and project name
        repo = Repo("username", "project_name")

        # From the repo's url
        repo = Repo.repo_from_url("https://github.com/username/project_name")

        announcements = repo.get_announcements()

    """

    base_github_url = "https://github.com"
    base_raw_url = "https://raw.githubusercontent.com"

    def __init__(self, username: str, project_name: str):
        self.username = username
        self.project_name = project_name

    def get_github_url(self) -> str:
        return f"{self.base_github_url}/{self.username}/{self.project_name}"

    def get_announcements_url(self) -> str:
        return f"{self.base_raw_url}/{self.username}/{self.project_name}/main/announcements.json"

    @staticmethod
    def repo_from_url(url: str):
        """Split a github url into a username and a project_name"""
        _, _, username, project_name = [x for x in url.split("/") if x != ""]
        return Repo(username, project_name)

    def get_announcements(self) -> List[Union[str, None]]:
        return requests.get(self.get_announcements_url()).json()

    def __repr__(self) -> str:
        return f"{self.username}/{self.project_name}"
