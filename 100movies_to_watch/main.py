from bs4 import BeautifulSoup
import requests

URL = 'https://empireonline.com/movies/features/best-movies-2'

response = requests.get(URL)
webpage = response.text

# soup = BeautifulSoup(yc_webpage, 'html.parser')
# article_tag = soup.find(name='span', class_='titleline')
# article_text = article_tag.get_text()
# article_link = article_tag('a')
# article_upvote = soup.find(name='span', class_='score').getText()

soup = BeautifulSoup(webpage, 'html.parser')
movies_list = soup.find_all(name='h3', class_='c-title')
movies_list.reverse()
movie_titles = [movie.getText() for movie in movies_list]

with open('top-movies.txt', mode='w') as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")