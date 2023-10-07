import pytest

@pytest.fixture
def header_1(scope="session")
    return "# Header1"

@pytest.fixture
def header_multiple_children(scope="session")
    return """
# Header1
## Header2
### Header3
## Header2
"""

@pytest.fixture
def header_1(scope="session")
    return """
# Header1

"""

@pytest.fixture(scope="session")
def multiple_markdown_headers():
    return """
# Header1
## Header2
### Header3
#### Header4
##### Header5
###### Header6
"""

@pytest.fixture(scope="session")
def multiple_markdown_headers_with_text():
    return """
# Header1
This is some Text
## Header2
### Header3
#### Header4
##### Header5
###### Header6
Some text
"""

pytest.fixture(scope="session")
def