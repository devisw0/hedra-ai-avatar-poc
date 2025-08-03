import requests
import random

def dog_breed_random_image():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)

    dictionary_format = response.json()
    print(dictionary_format)

    message_key = dictionary_format['message']
    listify = list(message_key.keys())
    random_breed = random.choice(listify)
    print(f"\nselected random breed is: {random_breed}")

    prebuilt_url = f"https://dog.ceo/api/breed/{random_breed}/images/random"

    image_request = requests.get(prebuilt_url)
    print(image_request.text)
    image_request_dictionary = image_request.json()

    response_image_url = image_request_dictionary['message']
    print(f"\n your image url is: {response_image_url}")



if __name__ == "__main__":
    dog_breed_random_image()