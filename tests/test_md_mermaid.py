import pytest
from pytest_lazyfixture import lazy_fixture
from md_to_mermaid import build_MermaidNode_from_md_string


def test_root_level(header_1):
    tree = build_MermaidNode_from_md_string(header_1)
    assert tree.header_level == 0

@pytest.mark.parametrize("md_str, header_level, header_text", [
    (lazy_fixture('header_1'), 1, "Header1"),
    (lazy_fixture('header_1_2_3'), 1, "Header1"),
])
def test_python_level_one(md_str, header_level, header_text):
    tree = build_MermaidNode_from_md_string(md_str)
    assert tree.children[0].header_level == header_level
    assert tree.children[0].header_text == header_text

@pytest.mark.parametrize("md_str, header_level, header_text", [
    (lazy_fixture('header_1_2_3'), 2, "Header2"),
])
def test_python_level_nested_children(md_str, header_level, header_text):
    tree = build_MermaidNode_from_md_string(md_str)
    level_2 = tree.children[0].children[0]
    assert level_2.header_level == header_level
    assert level_2.header_text == header_text


def test_multiple_level_children(header_multiple_children):
    tree = build_MermaidNode_from_md_string(header_multiple_children)
    assert len(tree.children) == 1
    assert len(tree.children[0].children) == 2
    assert len(tree.children[0].children[0].children) == 1
    assert all([x.header_level == 2 for x in tree.children[0].children])