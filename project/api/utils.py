
import re

def encode_url(url):
    return re.sub(r"[\.\,\/:]", "", url)
