# scrape site and find the article with the most votes.
from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')
yc_page = res.text

print(yc_page)

soup = BeautifulSoup(yc_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
top_voted = article_upvotes.index(max(article_upvotes))
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

print(f'Top Article:: {article_texts[top_voted]}\nLink: {article_links[top_voted]}\n'
      f'With {article_upvotes[top_voted]} votes.')