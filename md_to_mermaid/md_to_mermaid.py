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
        return f"""{self.format}
{self.content}"""


def bundle_nodes(node_list=list[Token]):
    """Bundle tokens into a list of MermaidNodes."""
    nodes = defaultdict(list)


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
