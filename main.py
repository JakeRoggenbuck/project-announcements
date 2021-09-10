class Repo:
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

    def __repr__(self):
        return f"{self.username}/{self.project_name}"


if __name__ == "__main__":
    repo = Repo.repo_from_url("https://github.com/JakeRoggenbuck/jai")
    print(repo)

    print(repo.get_github_url())
    print(repo.get_readme_url())
