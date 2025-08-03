import requests


def github_chain():
    url = "https://api.github.com/users/octocat"
    response = requests.get(url)
    dictionary_response = response.json()
    print(dictionary_response)
    username = dictionary_response['login']
    print(f"\n username chosen is: {username}")


    url2 = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(url2)
    dictionary_format_repos = repos_response.json()
    first_repo = dictionary_format_repos[0]['name']
    print(f"\n the first repo was: {first_repo}")


    repo_info_url = f"https://api.github.com/repos/{username}/{first_repo}"

    first_repo_info = requests.get(repo_info_url)
    dictionary_format_first_repo_info = first_repo_info.json()
    stargazers_count = dictionary_format_first_repo_info['stargazers_count']
    description = dictionary_format_first_repo_info['description']
    language = dictionary_format_first_repo_info['language']
    print(f"\n {username}'s first repo is {first_repo} and has {stargazers_count} stars, is written in {language} and has the following description: {description}")

if __name__ == "__main__":
    github_chain()


    