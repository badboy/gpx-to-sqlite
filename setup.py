from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="gpx-to-sqlite",
    description="Convert GPX files to a a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Jan-Erik Rediger",
    url="https://github.com/badboy/gpx-to-sqlite",
    project_urls={
        "Issues": "https://github.com/badboy/gpx-to-sqlite/issues",
        "CI": "https://github.com/badboy/gpx-to-sqlite/actions",
        "Changelog": "https://github.com/badboy/gpx-to-sqlite/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["gpx_to_sqlite"],
    entry_points="""
        [console_scripts]
        gpx-to-sqlite=gpx_to_sqlite.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    tests_require=["gpx-to-sqlite[test]"],
    python_requires=">=3.6",
)
