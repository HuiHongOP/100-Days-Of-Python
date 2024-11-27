from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/news.ycombinator.com/')
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
titles = soup.find_all(name='a', class_='storylink')
article_name = []
article_link = []

for title in titles:
    article_name.append(title.getText())
    article_link.append(title.get('href'))

titles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_number = max(titles_upvotes)
largest_index = titles_upvotes.index(largest_number)

print(article_link[largest_index])
print(article_name[largest_index])
