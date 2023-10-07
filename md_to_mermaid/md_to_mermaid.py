import copy
from dataclasses import dataclass, field

from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode, Token

@dataclass
class MermaidNode:
    tag: str
    content: str
    children: list["MermaidNode"] = field(default_factory=list)
    format: str = "Flowchart LR"

    # def __str__(self):
    #     return f"{self.format}\n{self.content}"

    @property
    def _tag_value(self):
        return int(self.tag[1])

def bundle_nodes(
        node_list=list[Token|list[Token]],
        parent_node: MermaidNode|None = None
):
    """
    Bundle tokens into a list of MermaidNodes.
    
    Split when the tag value of the next node is less than or equal to the current node.

    """
    
    if not parent_node:
        parent_node = node_list.pop()
    
    return parent_node

    for index, node in reversed(list(enumerate(node_list))):
        
        if parent_node._tag_value == node._tag_value:
            # Nodes are siblings. Return the parent node and the remaining objects
            return parent_node, node_list
        
        if parent_node._tag_value > node._tag_value:
            # Node is a child of the parent node
            parent_node.children.insert(0, node_list.pop(index))

    return parent_node, node_list


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
