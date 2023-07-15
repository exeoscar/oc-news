from transformers import pipeline
from news_scraper import NewsScraper

class ChatBot:
    def __init__(self):
        self.model = pipeline('text-generation', model='gpt-2')
        self.ner_model = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')
        self.news_scraper = NewsScraper()

    def get_response(self, message):
        # If the message starts with "news about", extract the topic and get news articles related to it.
        if message.lower().startswith('news about '):
            topic = message[11:]
            news = self.news_scraper.get_news(topic)
            return "\n".join([f"Title: {article['title']}\nLink: {article['link']}" for article in news])

        # Otherwise, generate a response using the model.
        else:
            response = self.model(message, max_length=50, do_sample=True, temperature=0.7)[0]['generated_text']
            return response
