import requests
url = "https://official-joke-api.appspot.com/jokes/random"
response = requests.get(url)
joke_data = response.json()
print("�������:")
print(joke_data["setup"])
print(joke_data["punchline"])
