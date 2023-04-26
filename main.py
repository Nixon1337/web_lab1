import requests
from flask import Flask

app = Flask(__name__)

term = input("Ключове слово для пошуку в iTunes: ")

@app.route("/")
def home():

    url = f"https://itunes.apple.com/search?term={term}"
    response = requests.get(url)

    data = response.json()
    results = data["results"]
    response_data = []
    for result in results:
        album = result['collectionName']
        artist = result['artistName']
        price = result['collectionPrice']
        response_data.append({'album': album, 'artist': artist, 'price': price})
    response_str = ''
    for result in response_data:
        response_str += f"Альбом: {result['album']}, Виконавець: {result['artist']}, Ціна: {result['price']}<br>"
    return response_str

if __name__ == "__main__":
    app.run()
