from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
response.raise_for_status()

yc_web_page = (response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")

all_articles = soup.find_all("a", class_= "storylink")

article_texts = []
article_links = []

for article in all_articles:
    text = article.getText()
    article_texts.append(text)

    link = article.get("href")
    article_links.append(link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all ("span", class_= "score")]

print(article_links)
print(article_texts)
print(article_scores)

max_score = max(article_scores)
max_index = article_scores.index(max_score)

print(article_texts[max_index])
print(article_links[max_index])
print(max_score)
