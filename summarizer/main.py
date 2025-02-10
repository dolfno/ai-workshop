import logging
import os

import requests
from argparsing import parse_args
from dotenv import load_dotenv
from prompts import (
    CREATE_PR_DESCRIPTION_PROMPT,
    CREATE_PR_DESCRIPTION_PROMPT_COPY_PASTE_READY,
    YOUR_PROMPT,
)

from summarizer.git_cli import get_diff

load_dotenv()

LLM_HOST = os.getenv("LLM_HOST", "http://localhost:11434")


def validate_response(response):
    logging.debug(f"Response: {response.json()}")
    if response.status_code != 200:
        raise ValueError(f"Error from Ollama: {response.json()}")


def generate_summary(diff, model="llama3.2"):
    """Send diff to LLM for processing"""
    logging.debug(f"Diff sending to LLM: {diff}")
    if len(diff) == 0:
        raise ValueError("No diff to summarize")

    if len(diff) > 4000:
        logging.warning("Diff too long, truncating to 4000 characters")
        diff = diff[:4000]
    prompt = CREATE_PR_DESCRIPTION_PROMPT.format(diff=diff)

    messages = [{"role": "user", "content": prompt}]
    response = requests.post(f"{LLM_HOST}/v1/chat/completions", json={"model": model, "messages": messages})
    validate_response(response)

    # return only the LLM answer
    return response.json()["completions"][0]["content"]


def main(args_list=None, summarize=True):
    args = parse_args(args_list)
    logging.basicConfig(level=args.log_level)
    logging.info(f"Using args: {args}")

    diff = get_diff(
        args.base_branch,
        args.feature_branch,
        args.project_folder,
    )

    # used for Agent tooling in chapter build Agents.
    if not summarize:
        return diff

    summary = generate_summary(diff)
    print(f"Results:\n{summary}")
    return summary


if __name__ == "__main__":
    main()
