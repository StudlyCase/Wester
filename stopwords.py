STOPWORDS = set()

def filter_stopwords(tokens):
    return [t for t in tokens if t not in STOPWORDS]
