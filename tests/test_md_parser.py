from md_to_mermaid import bundle_nodes, parse_md_headers
# import pytest
# from pathlib import Path

def test_parse_md_headers():
    """Test parse_md_headers function."""
    md_text = """# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
"""
    node_tags = ['h1','h2','h3','h4','h5']
    assert [x.tag for x in parse_md_headers(md_text)] == node_tags

    node_content = ['Header 1','Header 2','Header 3','Header 4','Header 5']
    assert [x.content for x in parse_md_headers(md_text)] == node_content
    
def test_simple_bundle_nodes():
    """Test bundle_nodes function."""
    md_text = """# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
"""
    bundle_nodes(parse_md_headers(md_text))
