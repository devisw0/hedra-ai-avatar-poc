import os
import requests
from dotenv import load_dotenv

# Load .env from the parent directory (one level up)
load_dotenv('../.env')

def test_all_avatar_apis():
    print("🧪 Testing all Avatar API keys...\n")
    
    # Test OpenAI
    print("1️⃣ Testing OpenAI...")
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        headers = {"Authorization": f"Bearer {openai_key}"}
        response = requests.get("https://api.openai.com/v1/models", headers=headers)
        if response.status_code == 200:
            print("   ✅ OpenAI API key works!")
        else:
            print(f"   ❌ OpenAI failed: {response.status_code}")
    else:
        print("   ❌ OpenAI API key not found")
    
    # Test ElevenLabs
    print("\n2️⃣ Testing ElevenLabs...")
    elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
    if elevenlabs_key:
        headers = {"xi-api-key": elevenlabs_key}
        response = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers)
        if response.status_code == 200:
            print("   ✅ ElevenLabs API key works!")
        else:
            print(f"   ❌ ElevenLabs failed: {response.status_code}")
    else:
        print("   ❌ ElevenLabs API key not found")
    
    # Test Hedra
    print("\n3️⃣ Testing Hedra...")
    hedra_key = os.getenv('HEDRA_API_KEY')
    if hedra_key:
        headers = {"X-API-Key": hedra_key}
        response = requests.get("https://api.hedra.com/web-app/public/models", headers=headers)
        if response.status_code == 200:
            print("   ✅ Hedra API key works!")
        else:
            print(f"   ❌ Hedra failed: {response.status_code}")
    else:
        print("   ❌ Hedra API key not found")
    
    # Test LiveKit
    print("\n4️⃣ Testing LiveKit...")
    livekit_url = os.getenv('LIVEKIT_URL')
    livekit_key = os.getenv('LIVEKIT_API_KEY')
    livekit_secret = os.getenv('LIVEKIT_API_SECRET')
    
    if all([livekit_url, livekit_key, livekit_secret]):
        print("   ✅ LiveKit credentials found!")
        print(f"   📡 URL: {livekit_url}")
    else:
        print("   ❌ LiveKit credentials incomplete")
    
    print("\n🎯 If all show ✅, you're ready to build your avatar!")

if __name__ == "__main__":
    test_all_avatar_apis()