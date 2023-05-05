from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_title = [title.getText() for title in all_movies]
movies = movie_title[::-1]
# for n in range(len(movie_title)-1, -1, -1):
#     print(movie_title[n])

with open("movies.txt", mode="w") as file:
    # for movie in movies:
    #     file.write(f"{movie}\n")
    movie = [file.write(f"{movie}\n") for movie in movies]