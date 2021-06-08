from bs4 import BeautifulSoup as bs
import esprima


def extract_script_from_html(html: str):
    soup = bs(html, "html.parser")
    for script in soup.find_all("script"):
        yield script

def tokenize_html(html: str):
    tokens = []
    for script in extract_script_from_html(html):
        for program in script:
            tokens += esprima.tokenize(program)
    
    return tokens

print(tokenize_html("<head>blah</head><script>var x = 1;</script>"))
