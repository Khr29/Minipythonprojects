import requests

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        return []
    except requests.exceptions.RequestException:
        print("Network error. please check your connection")
        return []
