import subprocess


def get_diff(base_branch, feature_branch, project_folder="."):
    """Capture git diff between branches"""
    return subprocess.check_output(
        ["git", "diff", f"{base_branch}..{feature_branch}"],
        text=True,
        cwd=project_folder,
    )


def check_in_git_dir(project_folder="."):
    try:
        in_git_dir = subprocess.check_output(
            ["git", "rev-parse", "--is-inside-work-tree"],
            text=True,
            cwd=project_folder,
        ).strip()
        if in_git_dir != "true":
            raise EnvironmentError("Not inside a Git directory")
    except subprocess.CalledProcessError:
        raise EnvironmentError("Not inside a Git directory")


def get_current_branch(project_folder="."):
    return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True, cwd=project_folder).strip()
