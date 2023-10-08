"""Generate headers from markdown"""
import re
from collections import namedtuple

Header = namedtuple('Header', ['level', 'text'])

def generate_header(md_str:str):
    for line in md_str.splitlines():
        if line.startswith('#'):
            line_pattern = re.match(r"(#+)(.+)", line)
            header_level = len(line_pattern.group(1))
            header_text = line_pattern.group(2).strip()
            yield Header(header_level, header_text)
            