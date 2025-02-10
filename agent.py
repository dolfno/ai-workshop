from math import log

import dspy

from summarizer.github_tools import read_github_file, search_github
from summarizer.main import generate_summary
from summarizer.main import main as get_diff


def main():
    instructions = "Find all code references that might be impacted by the code change in the code_diff."
    signature = dspy.Signature("code_diff -> code_references: list[str]", instructions)
    react = dspy.ReAct(signature, tools=[generate_summary, search_github, read_github_file], max_iters=20)

    diff = get_diff(
        project_folder="~/connectedbrewery/terraform-aws-uc-d06a/.",
        summarize=False,
        log_level="DEBUG",
    )

    react(code_diff=diff)


if __name__ == "__main__":
    main()
