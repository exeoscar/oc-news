from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=2000, min_length=300, do_sample=False)
    return summary[0]['summary_text']
