# Auto-generated by easyPyPI: https://github.com/PFython/easypypi
# Preserve current formatting to ensure easyPyPI compatibility.

from pathlib import Path
from setuptools import find_packages
from setuptools import setup

NAME = "whatsappcloud"
GITHUB_USERNAME = "PFython"
VERSION = "0.0.5"
DESCRIPTION = "API wrapper for Whatsapp Cloud"
LICENSE = "MIT License"
AUTHOR = "Peter Fison"
EMAIL = "peter@awsom.solutions"
URL = "https://github.com/PFython/whatsappcloud"
KEYWORDS = "Meta, whatsapp, Pfython, API, cloud, business, messaging, Facebook"
CLASSIFIERS = "Development Status :: 3 - Alpha, Intended Audience :: Developers, Operating System :: OS Independent, Programming Language :: Python :: 3.10, Programming Language :: Python :: 3.6, Programming Language :: Python :: 3.7, Programming Language :: Python :: 3.8, Programming Language :: Python :: 3.9, Topic :: Communications :: Chat, Topic :: Communications :: File Sharing, Topic :: Multimedia, Topic :: Multimedia :: Video, Topic :: Office/Business, Topic :: Office/Business :: Groupware, Topic :: Software Development :: Libraries, Topic :: Software Development :: Libraries :: Application Frameworks, Topic :: Software Development :: Libraries :: Python Modules, Topic :: Utilities, License :: OSI Approved :: MIT License"
REQUIREMENTS = "cleverdict, requests"


def comma_split(text: str):
    """
    Returns a list of strings after splitting original string by commas
    Applied to KEYWORDS, CLASSIFIERS, and REQUIREMENTS
    """
    if type(text) == list:
        return [x.strip() for x in text]
    return [x.strip() for x in text.split(",")]


if __name__ == "__main__":
    setup(
        name=NAME,
        packages=find_packages(),
        version=VERSION,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=(Path(__file__).parent / "README.md").read_text(),
        long_description_content_type="text/markdown",
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        download_url=f"{URL}/archive/{VERSION}.tar.gz",
        keywords=comma_split(KEYWORDS),
        install_requires=comma_split(REQUIREMENTS),
        classifiers=comma_split(CLASSIFIERS),
        package_data={"": ["*.md", "*.json", "*.png", "*.ico"], NAME: ["*.*"]},
    )
