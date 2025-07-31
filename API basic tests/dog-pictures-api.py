import requests

def get_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = request.get(url)

    if response.status_code == 200:
        data = response.json()
        if response.status_code == 200:
            data = response.json()
        print(f"🐕 Dog photo: {data['message']}")
        print(f"Status: {data['status']}")
    else:
        print(f"❌ Error: {response.status_code}")

# Try it!
get_random_dog()