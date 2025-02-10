from setuptools import setup

setup(
    name="diff-summarizer",
    version="0.1",
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "diff-summarizer=summarizer.main:main",
        ],
    },
)
