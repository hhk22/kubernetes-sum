
import glob
import time
import os
import json
import pymysql
import re
import time
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback
# from dotenv import load_dotenv
# load_dotenv()

def query_openai(prompt, api_key):
    chat = ChatOpenAI(api_key=api_key)

    messages = [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content=prompt)
    ]

    result = None
    price = None
    with get_openai_callback() as cb:
        result = chat.invoke(messages).content
        price = cb.total_cost
    return result, price

def run():

    files = glob.glob("/api/dynamic-vol/sentences/*")
    file_path = files[0]

    text = None
    api_key = os.environ.get("OPENAI_KEY")
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    os.remove(file_path)
    rst, price = query_openai(text, api_key)
    
    basename = os.path.basename(file_path)
    with open(f"/api/dynamic-vol/gpt_results/{basename}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps({
            "price": price,
            "gpt_result": rst
        }, ensure_ascii=False))
    
        conn = pymysql.connect(host="172.16.103.176", user="root", password="root", db="gpt_results")
        now = datetime.now()
        now_date = now.strftime("%Y-%m-%d")
        rst_without_punctuations = re.sub(r'[\'"]', '', rst)
        cur = conn.cursor()
        sql = f"INSERT INTO results VALUES ({int(time.time())}, {os.path.basename(file_path)}, {rst_without_punctuations}, {price}, {now_date})"
        print(sql)
        cur.execute(sql)
        conn.commit()
        conn.close()

    

if __name__ == "__main__":
    while True:
        try:
            print('gpting...')
            run()
            time.sleep(10)
            break
        except Exception as e:
            time.sleep(5)
            print(e)