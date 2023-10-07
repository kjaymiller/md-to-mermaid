from more_itertools import split_when

from collections import defaultdict
from dataclasses import dataclass, field

from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode, Token


@dataclass
class MermaidNode:
    tag: str
    content: str
    children: list["MermaidNode"] = field(default_factory=list)
    format: str = "Flowchart LR"

    def __str__(self):
        return f"{self.format}\n{self.content}"

    @property
    def _tag_value(self):
        return int(self.tag[1])

def bundle_nodes(node_list=list[Token|list[Token]]):
    """
    Bundle tokens into a list of MermaidNodes.
    
    Split when the tag value of the next node is less than or equal to the current node.

    """
    if all((isinstance(x, MermaidNode) for x in node_list)):
        print("All MermaidNodes")
        node_bundle = list(
            split_when(node_list, lambda x,y: x._tag_value >= y._tag_value)
        )
    elif all((isinstance(x, list) for x in node_list)):
        print("All Lists")
        print("Root_nodes")
        print([node[0].tag for node in node_list])
        node_bundle = list(
            split_when(node_list, lambda x,y: x[0]._tag_value >= y[0]._tag_value)
        )


    print("results:")
    print(node_bundle)
    print("----")
    while len(node_bundle) > 1:
        bundle_nodes(node_bundle)
    return node_bundle

def evaluate_root_nodes(node_lists: list[list[MermaidNode]])-> bool:
    """Check the first node of each list.
    And return if all the roots are the same
    """
    root_nodes = [node_list[0] for node_list in node_lists]
    return all((node.tag == root_nodes[0].tag for node in root_nodes))


def parse_md_headers(md_text:str)  -> list[SyntaxTreeNode]:
    """Parse markdown text and return a tree of headers."""
    md = MarkdownIt("zero", {"maxNesting": 1})
    md.enable(["heading",])
    tokens = md.parse(md_text)
    nodes = SyntaxTreeNode(tokens)
    return [
        MermaidNode(
            tag=node.tag,
            content=node.children[0].children[0].content
        ) for node in nodes.children
    ]
