CREATE_PR_DESCRIPTION_PROMPT = """
    Summarize these code changes for a pull request description.
    Focus on key changes and their impact. Use markdown formatting.

    Diff: 
    {diff}
    """

CREATE_PR_DESCRIPTION_PROMPT_COPY_PASTE_READY = """
    Summarize these code changes for a pull request description.
    Focus on key changes and their impact. Use markdown formatting.
    ONLY answer with pr description, so its ready to copy paste.

    Diff:
    {diff}
    """

YOUR_PROMPT = """
    Your prompt here
    """
