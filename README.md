# gpx-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/gpx-to-sqlite.svg)](https://pypi.org/project/gpx-to-sqlite/)
[![Changelog](https://img.shields.io/github/v/release/badboy/gpx-to-sqlite?include_prereleases&label=changelog)](https://github.com/badboy/gpx-to-sqlite/releases)
[![Tests](https://github.com/badboy/gpx-to-sqlite/workflows/Test/badge.svg)](https://github.com/badboy/gpx-to-sqlite/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/badboy/gpx-to-sqlite/blob/master/LICENSE)

Convert GPX files to a a SQLite database

## Installation

Install this tool using `pip`:

    $ pip install gpx-to-sqlite

## Usage

Usage instructions go here.

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd gpx-to-sqlite
    python -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
