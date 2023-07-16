from rss_feed_parser import RSSFeedParser
from text_summarizer import Summarizer

class Chatbot:
    def __init__(self):
        self.rss_feed_parser = RSSFeedParser()
        self.summarizer = Summarizer()

    def search_news(self, keywords):
        return self.rss_feed_parser.search_news(keywords)

    def summarize_news(self, full_text):
        return self.summarizer.summarize(full_text)
