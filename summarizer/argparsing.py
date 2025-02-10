import argparse
import os

from summarizer.git_cli import check_in_git_dir, get_current_branch


def check_args(args):
    if args.base_branch == args.feature_branch:
        raise ValueError(f"Base and feature branches must be different, found both being {args.base_branch}")
    check_in_git_dir(args.project_folder)


def parse_args(arg_list=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_branch", default="main")
    parser.add_argument("--feature_branch", default="use current branch")
    parser.add_argument("--project_folder", default="~/connectedbrewery/terraform-aws-uc-d06a/.")
    parser.add_argument("--log-level", default="INFO")

    args = parser.parse_args(arg_list)
    args.project_folder = os.path.expanduser(args.project_folder)

    if args.feature_branch == "use current branch":
        args.feature_branch = get_current_branch(args.project_folder)
    return args
