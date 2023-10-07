from dataclasses import dataclass, field
from file_parser import generate_header, Header

@dataclass
class MermaidNode:
    """
    A Single markdown string produces a single mermaid diagram block
    children: [[Level1, Level2], [Level1a, Level2a]]
    """
    header_level : int
    header_text : str
    parent: "MermaidNode" = None
    children: list["MermaidNode"] = field(default_factory=list)
    format: str = "Flowchart LR"




def iterate_through_header(md_str: str)-> list[MermaidNode]:
    parent = MermaidNode(
        header_level=0,
        header_text="I am (G)Root"

    )
    
    # header = next(headers)
    # parent = MermaidNode(
    #     header_level=header.level,
    #     header_text=header.text,
    #     parent=parent
    # )
    mermaid_tree_root = parent

    for header in generate_header(md_str):
        node = MermaidNode(
            header_level=header.level,
            header_text=header.text,
        )

        if header.level > parent.header_level:
            # this header is a child
            node.parent = parent
            parent.children.append(node)

        if header.level <= parent.header_level:
            # these objects are siblings
            grandparent = parent.parent 
            
            while header.level <= grandparent.header_level:
                # keep checking grandparents to find your level
                grandparent = grandparent.parent
            
            node.parent = grandparent
            grandparent.children.append(node)

        parent = node
        
    return mermaid_tree_root
        

def mermaid_file_build():
    """
    Diagram starts with the first header and links all of the children nodes.

    If there is subsequent header 1, 
    """