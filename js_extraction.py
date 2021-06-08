from bs4 import BeautifulSoup as bs
import esprima
import glob

def extract_script_from_html(html: str):
    soup = bs(html, "html.parser")
    for script in soup.find_all("script"):
        yield script

def tokenize_html(html: str):
    for script in extract_script_from_html(html):
        for program in script:
            yield esprima.tokenize(program)

def is_valid_malicious_path(path):
    ignore_files_pattern = ['misc', 'ignore']
    return all(ignore_pattern not in path for ignore_pattern in ignore_files_pattern)

def get_all_malicious_js_token():
    for html_file_path in glob.iglob("*MALICOUS/**/*.html", recursive=True):
        print(html_file_path)
        if is_valid_malicious_path(html_file_path):
            with open(html_file_path, "r", errors='surrogateescape') as html:
                yield from tokenize_html(html.read())
    
    for js_file_path in glob.iglob("*MALICOUS/**/*.js", recursive=True):
        print(js_file_path)
        if is_valid_malicious_path(js_file_path):
            with open(js_file_path, "r", errors='surrogateescape') as js:
                    yield esprima.tokenize(js.read())

