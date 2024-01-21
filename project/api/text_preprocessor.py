
import glob
import os
from bs4 import BeautifulSoup

# print(glob.glob("./html/*"))

files = glob.glob("./html/*")
file_path = files[0]

bs = None
with open(file_path, encoding="utf-8") as f:
    html = f.read()
    bs = BeautifulSoup(html, "lxml")
os.remove(file_path)

product_name = bs.select_one('#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div._1eddO7u4UC > h3').text
original_price = bs.select_one('#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > del > span._1LY7DqCnwR').text
sale_price = bs.select_one('#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div.WrkQhIlUY0 > div > strong > span._1LY7DqCnwR').text
title = bs.select_one('title').text
meta_desc = bs.select_one('meta[name="description"]').get('content')
meta_twitter_desc = bs.select_one('meta[name="twitter:title"]').get('content')

setences = f"""
    This is my preprocessed information from scraped website. 
    Make some useful sentences to sell these products to customers.

    product_name={product_name}
    original_price={original_price}
    sale_price={sale_price}
    title={title}
    meta_description={meta_desc}
    meta_twitter_description={meta_twitter_desc}

"""

print(setences)