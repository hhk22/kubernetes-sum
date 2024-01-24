
import glob
import time
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback


def query_openai(prompt, api_key):
    chat = ChatOpenAI(api_key=api_key)

    messages = [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content=prompt)
    ]

    result = None
    with get_openai_callback() as cb:
        result = chat.invoke(messages).content
        print(cb)
    return result

def run():

    files = glob.glob("/api/dynamic-vol/sentences/*")
    file_path = files[0]

    text = None
    api_key = os.environ.get("OPENAI_KEY")
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    # os.remove(file_path)
    rst = query_openai(text, api_key)
    print(rst)
    
    # basename = os.path.basename(file_path)
    # with open(f"/api/dynamic-vol/sentences/{basename}", "w", encoding="utf-8") as f:
    #     f.write(sentences)

    # print(sentences)

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