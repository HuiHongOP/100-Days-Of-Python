import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
movie_names = [movie.getText() for movie in soup.find_all(name='h3', class_='title')]
movie_names.reverse()

with open("top_movies.txt", 'w', encoding='utf-8') as file:
    for movie_name in movie_names:
        file.write(movie_name + '\n')
