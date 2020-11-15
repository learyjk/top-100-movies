from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_titles = soup.find_all(name="h3", class_="title")[::-1]

with open("movies.txt", mode="w") as file:
    for movie in all_titles:
        file.write(f"{movie.getText()}\n")