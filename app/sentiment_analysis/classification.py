from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_sentiment(comment_text):
        analysis = TextBlob(comment_text)
        polarity = analysis.polarity
        classification = "positive" if polarity >= 0 else "negative"
        return polarity,classification
