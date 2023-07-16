import feedparser
from dateutil.parser import parse
from bs4 import BeautifulSoup
import requests
from typing import List
from dataclasses import dataclass

@dataclass
class Article:
    title: str
    link: str
    published: str
    summary: str
    full_text: str

class RSSFeedParser:
    def __init__(self, feed_url='http://feeds.bbci.co.uk/news/world/rss.xml'):
        self.feed_url = feed_url

    def get_full_text(self, link: str) -> str:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        text_container = soup.find('article', {'class': 'ssrcss-pv1rh6-ArticleWrapper e1nh2i2l6'})
        if text_container is None:
            return ""
        else:
            paragraphs = text_container.find_all('p')
            return '\n'.join([p.get_text() for p in paragraphs])

    def search_news(self, keywords: str) -> List[Article]:
        feed = feedparser.parse(self.feed_url)

        results = []
        for entry in feed.entries:
            if keywords.lower() in entry.title.lower():
                entry['full_text'] = self.get_full_text(entry.link)
                article = Article(entry.title, entry.link, entry.published, entry.summary, entry['full_text'])
                results.append(article)

        # Sort the results by date of publication and limit to the 10 most recent ones
        results.sort(key=lambda article: parse(article.published), reverse=True)
        return results[:10]
