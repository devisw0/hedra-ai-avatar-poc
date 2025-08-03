import requests
import os
from dotenv import load_dotenv
import openai_chat
load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel's voice


def elevenlabs_request(chatgpt_response):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,  # "I'm a VIP member"
        "Content-Type": "application/json"    # "Please speak to me in English"
    }
    
    data = {
        "text":chatgpt_response
    }

    response = requests.post(url,headers=headers, json=data)

    if response.status_code == 200:    
        with open("eleven_labs_audio.mp3", "wb") as f:
            f.write(response.content)
            print("Audio saved successfully")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def voice_chat(user_message):
        user_message = openai_chat.chat_with_gpt(user_message)
        elevenlabs_request(user_message)
        print("🎤 AI has spoken! Check the audio file!")



if __name__ == "__main__":
    # elevenlabs_request("Hello, how are you?")
    user_input = input("Enter your message: ")
    voice_chat(user_input)