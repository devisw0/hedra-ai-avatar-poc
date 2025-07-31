import requests

def get_fun_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # headers = {

    # }
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Fun fact: {data['text']}")
    else:
        print(f"Failed to fetch fun fact: {response.status_code}")

get_fun_fact() 



