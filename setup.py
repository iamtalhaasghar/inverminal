#!/usr/bin/python3

from setuptools import setup

options = dict(
    name="inverminal",
    version="1.0.0",
    description="Use Invidious on Terminal to watch Youtube Videos or play just audio in background.",
    keywords=["video", "music", "audio", "youtube", "stream", "download", "inverminal"],
    author="talha_programmer",
    author_email="talhaasghar.contact@simplelogin.fr",
    url="https://github.com/iamtalhaasghar/inverminal",
    download_url="https://github.com/iamtalhaasghar/inverminal/releases",
    entry_points={'console_scripts': ['inv = inverminal.main.run']},
    install_requires= open("requirements.txt").readlines(),
    long_description=open("README.md").read()
)
setup(**options)