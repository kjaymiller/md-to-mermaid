from file_parser import generate_header, Header

import pytest
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize("md_str, expected_output", [
    (lazy_fixture('header_1'), [(1, "Header1")]),
    (lazy_fixture('header_1_2_3'), [(1, "Header1"), (2, "Header2"), (3, "Header3")]),
])
def test_generate_header(md_str, expected_output):
    assert list(generate_header(md_str)) == expected_output

def test_generate_header_avoids_non_headers(multiple_markdown_headers_with_text):
    md_str = "# Header 1\n## Header 2\n\nSome Text Here\n### Header 3"
    expected_output = [(1, "Header 1"), (2, "Header 2"), (3, "Header 3")]
    assert list(generate_header(md_str)) == expected_output