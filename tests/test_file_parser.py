from file_parser import generate_header

def test_generate_header():
    md_str = "# Header 1\n## Header 2\n### Header 3"
    expected_output = [(1, "Header 1"), (2, "Header 2"), (3, "Header 3")]
    assert list(generate_header(md_str)) == expected_output

def test_generate_header_avoids_non_headers():
    md_str = "# Header 1\n## Header 2\n\nSome Text Here\n### Header 3"
    expected_output = [(1, "Header 1"), (2, "Header 2"), (3, "Header 3")]
    assert list(generate_header(md_str)) == expected_output