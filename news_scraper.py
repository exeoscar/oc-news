import feedparser

class NewsScraper:
    def get_news(self, topic):
        # Parse the RSS feed from BBC News for the given topic.
        feed = feedparser.parse(f'http://feeds.bbci.co.uk/news/{topic}/rss.xml')

        # Extract the title and link from each news article.
        news = [{'title': entry.title, 'link': entry.link} for entry in feed.entries]

        return news
