from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity < -0.3:
        tone = "Negative"
    elif polarity > 0.3:
        tone = "Positive"
    else:
        tone = "Neutral"

    return {
        "polarity": polarity,
        "tone": tone
    }