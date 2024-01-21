
import glob
import os
from bs4 import BeautifulSoup

print(glob.glob("./html/*"))

files = glob.glob("./html/*")
file_path = files[0]

bs = None
with open(file_path, encoding="utf-8") as f:
    html = f.read()
    bs = BeautifulSoup(html, "lxml")

print(bs)
product_name = bs.select('fieldset')
print(product_name)



# os.remove(file_path)