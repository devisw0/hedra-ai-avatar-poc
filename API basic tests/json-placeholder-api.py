import requests

def json_placeholder_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    authentication = {
        "access_key": "devan"
    }
    response = requests.get(url, headers = authentication)
    response_dictionary = response.json()
    print(response_dictionary)


if __name__ == "__main__":
    json_placeholder_api()