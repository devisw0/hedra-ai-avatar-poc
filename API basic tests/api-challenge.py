import requests

def explore_api():
    # This API gives you info about IP addresses
    url = "https://httpbin.org/ip"
    
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("Response data:")
        print(data)
        # YOUR TURN: Print out what's in the data dictionary
        # Hint: Try print(data) first to see what keys are available
        
explore_api()

if __name__ = __main__:
    explore_api()
    