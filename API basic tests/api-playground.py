import requests

def api_playground():
    print("🎮 Welcome to API Playground!\n")
    
    # 1. GitHub API
    print("1️⃣ Getting GitHub user info...")
    github_url = "https://api.github.com/users/octocat"
    github_response = requests.get(github_url)
    
    if github_response.status_code == 200:
        github_data = github_response.json()
        print(f"   GitHub User: {github_data['name']}")
        print(f"   Public Repos: {github_data['public_repos']}")
    else:
        print(f"   ❌ GitHub API failed: {github_response.status_code}")
    
    print()
    
    # 2. Dog API
    print("2️⃣ Getting random dog photo...")
    dog_url = "https://dog.ceo/api/breeds/image/random"
    dog_response = requests.get(dog_url)
    
    if dog_response.status_code == 200:
        dog_data = dog_response.json()
        print(f"   Dog Photo: {dog_data['message']}")
        print(f"   Status: {dog_data['status']}")
    else:
        print(f"   ❌ Dog API failed: {dog_response.status_code}")
    
    print()
    
    # 3. Fun Fact API
    print("3️⃣ Getting fun fact...")
    fact_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    fact_response = requests.get(fact_url)
    
    if fact_response.status_code == 200:
        fact_data = fact_response.json()
        print(f"   Fun Fact: {fact_data['text'][:100]}...")  # First 100 chars
    else:
        print(f"   ❌ Fun Fact API failed: {fact_response.status_code}")

# Test it!
api_playground()