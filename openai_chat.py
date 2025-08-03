import requests
import os
from dotenv import load_dotenv
import json  # Add this import


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(user_message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
    "messages": [{"role" : "user","content":user_message}]
    }

    chat_response = requests.post(url,headers=headers,json=data)
    if chat_response.status_code == 200:
        print("Success!")
        # print(chat_response.json())
        result = chat_response.json()  # ← This converts Response to dict
        print(json.dumps(chat_response.json(), indent=2))
        ai_response = result['choices'][0]['message']['content']
        print(ai_response)


def main():
    user_message = input("Enter your message: ")
    chat_with_gpt(user_message)



if __name__ == "__main__":
    main()