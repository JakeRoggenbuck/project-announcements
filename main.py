import requests
import plrs


class Repo:
    """Repo is an object that represents a github repo

    Contruct:

        # From the username and project name
        repo = Repo("username", "project_name")

        # From the repo's url
        repo = Repo.repo_from_url("https://github.com/username/project_name")

    """

    base_github_url = "https://github.com"
    base_raw_url = "https://raw.githubusercontent.com"

    def __init__(self, username: str, project_name: str):
        self.username = username
        self.project_name = project_name

    def get_github_url(self):
        return f"{self.base_github_url}/{self.username}/{self.project_name}"

    def get_readme_url(self):
        return f"{self.base_raw_url}/{self.username}/{self.project_name}/main/README.md"

    @staticmethod
    def repo_from_url(url: str):
        """Split a github url into a username and a project_name"""
        _, _, username, project_name = [x for x in url.split("/") if x != ""]
        return Repo(username, project_name)

    def get_readme_contents(self):
        return requests.get(self.get_readme_url()).text

    def __repr__(self):
        return f"{self.username}/{self.project_name}"


if __name__ == "__main__":
    repo = Repo.repo_from_url("https://github.com/JakeRoggenbuck/jai")

    contents = repo.get_readme_contents()
    print(contents)
