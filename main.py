import streamlit as st
from rss_feed_parser import RSSFeedParser, Article
from text_summarizer import summarize_text

rss_parser = RSSFeedParser()

st.title("News AI Chatbot")

user_input = st.text_input("Please input keywords about what news you want.")

if user_input:
    articles = rss_parser.search_news(user_input)

    if articles:
        article_titles = [f'{index + 1}. {article.title}' for index, article in enumerate(articles)]
        selected_article_index = st.selectbox('Please select a news article:', options=article_titles, index=0)
        
        selected_article = articles[int(selected_article_index.split(".")[0]) - 1]
        
        if st.button("Summarize this news article"):
            summary = summarize_text(selected_article.full_text)
            st.write(summary)
    else:
        st.write("No articles found. Please try different keywords.")
