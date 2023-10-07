from md_to_mermaid import bundle_nodes, parse_md_headers, MermaidNode
import pytest
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

pytest.mark.parametrize(
    "nodes, check",
    [
        ([MermaidNode("h1", "Test1"), MermaidNode("h1", "Test2"), MermaidNode("h1", "Test3")], True),
        ([MermaidNode("h2", "Test1"), MermaidNode("h1", "Test2"), MermaidNode("h1", "Test3")], False),
    ]
)
def test_check_root_nodes(nodes: list[MermaidNode], check: bool):]):
    """Test evaluate_root_nodes function."""
    assert evaluate_root_nodes(nodes) == check


def test_simple_bundle_nodes():
    """Test bundle_nodes function."""
    md_text = """# Header 1
## Header 2
### Header 3
# Header 1
### Header 3
# Header 2
"""
    nodes = bundle_nodes(parse_md_headers(md_text))
    assert len(nodes) == 3
