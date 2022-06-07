# Local Application Imports
from license_markdown_table import __version__, build_markdown_table


def test_version():
    assert __version__ == "0.1.0"


def test_build_markdown_table():
    assert build_markdown_table()
