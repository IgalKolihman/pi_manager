# The purpose of the project commands is to easily browse the projects that i have for the raspberry pi in github,
# install them and other management actions.
import re
from pathlib import Path

import git
from git import Repo
from github import Github
from github.Repository import Repository

from pi_manager.consts import GITHUB_TOKEN, PROJECT_REGEX, PROJECTS_DIR


def list_projects():
    """Lists all available os projects for the raspberry."""
    github = Github(GITHUB_TOKEN)
    available_os = []
    for repo in github.get_user().get_repos():
        if re.match(PROJECT_REGEX, repo.name):
            available_os.append(repo.name[len(PROJECT_REGEX) - 1:])

    print(*available_os, sep=" \t")


def download_project(repository: Repository, repo_dir: Path):
    """Download a git repository

    Args:
        repository (Repository): repository instance
        repo_dir (Path): where to install the repository
    """
    print(f"Cloning {repository.clone_url} to {str(repo_dir)}")
    Repo.clone_from(repository.clone_url,
                    str(repo_dir),
                    env={'GIT_SSL_NO_VERIFY': '1'})
    print(f"Cloned {repository.name} successfully!")


def activate_project():
    # TODO: add a bash file for every project with the installation process inside it.
    #       if the installation finished successfully then return a success code, otherwise a failure code
    pass


def install_project(project_name: str):
    """Downloads and installs a project.

    Args:
        project_name (str): name of the project repo
    """
    github = Github(GITHUB_TOKEN)
    project_repo = github.get_user().get_repo(project_name)
    download_project(project_repo, Path(f"{PROJECTS_DIR}\\{project_name}"))


def uninstall_project():
    pass


def remove_project(project_name: str):
    """Uninstall and remove the project from the device.

    Args:
        project_name (str): name of the project repo
    """
    # TODO: uninstall the project first (if installed of course)
    print(f"Removing {project_name}")
    git.rmtree(Path(f"{PROJECTS_DIR}\\{project_name}"))
    print(f"Removed {project_name} successfully")
