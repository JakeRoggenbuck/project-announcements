import requests

USER = "JakeRoggenbuck"
NAME = "auto-clock-speed"

URL = "https://github.com/JakeRoggenbuck/auto-clock-speed/"

def split_url(url: str):
    """Split a github url into a username and a project_name"""
    _, _, username, project_name = [x for x in url.split("/") if x != ""]
    return username, project_name


def convert_to_readme_url(username: str, project_name: str):
    return "https://raw.githubusercontent.com/{username}/{project_name}/main/README.md"

if __name__ == "__main__":
    print(split_url(URL))
