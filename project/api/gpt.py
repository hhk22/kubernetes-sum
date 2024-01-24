
import glob
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

def run():

    # files = glob.glob("./sentences/*")
    files = glob.glob("/api/dynamic-vol/sentences/*")
    file_path = files[0]

    print(file_path)

    text = None
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    # os.remove(file_path)
    print(text)

    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
        "Content-Type": 'application/json'
    }

    data = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a shopping mall administrator. You have sell products to customer. Use the information below to make useful sentences"},
            {"role": "user", "content": text}
        ],
        "temperature": 0.7
    })
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=data)
    json_response = json.loads(response.text)
    print(json_response['choices'][0]['message']['content'])

    
    # basename = os.path.basename(file_path)
    # with open(f"/api/dynamic-vol/sentences/{basename}", "w", encoding="utf-8") as f:
    #     f.write(sentences)

    # print(sentences)

if __name__ == "__main__":
    run()
    # while True:
    #     try:
    #         print('scraping...')
    #         run()
    #         time.sleep(10)
    #         break
    #     except Exception as e:
    #         time.sleep(5)
    #         print(e)