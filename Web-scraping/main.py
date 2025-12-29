import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()

web_page = (response.text)

soup = BeautifulSoup(web_page, "html.parser")

all_movies = soup.find_all("h3", class_ = "title")
all_movies.reverse()


for movie in all_movies:
    movienumber = movie.getText()
    with open ("Day 45/movies.txt", "a", encoding="utf-8") as file:
        file.write(movienumber + "\n") 

