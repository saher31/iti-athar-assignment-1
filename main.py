import os
from dotenv import load_dotenv
import requests

BASE_URL = "https://www.omdbapi.com/"


class Movie:
    def __init__(self, title, year, genre, director, actors, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
        self.actors = actors
        self.rating = rating

    def display(self):
        print("=" * 40)
        print("Movie Summary")
        print("=" * 40)
        print(f"{'Title':<10}: {self.title}")
        print(f"{'Year':<10}: {self.year}")
        print(f"{'Genre':<10}: {self.genre}")
        print(f"{'Director':<10}: {self.director}")
        print(f"{'Actors':<10}: {self.actors}")
        print(f"{'Rating':<10}: {self.rating}")
        print("=" * 40)


load_dotenv()

api_key=os.getenv("OMDB_API_KEY")

if api_key:
    print("Key loaded: True")
else:
    print("API key not found")
    exit()

response= requests.get(BASE_URL,params={"apikey": api_key, "t": "Inception"})

data = response.json()

if data["Response"] == "False":
    print(data["Error"])
    exit()

movie = Movie(
    data["Title"],
    data["Year"],
    data["Genre"],
    data["Director"],
    data["Actors"],
    data["imdbRating"],
)

movie.display()
