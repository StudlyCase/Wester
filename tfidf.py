import math
from collections import Counter

def tf(tokens):
    count = Counter(tokens)
    total = len(tokens)
    return {w: c / total for w, c in count.items()}

def idf(docs):
    n = len(docs)
    freq = {}
    for doc in docs:
        for word in set(doc):
            freq[word] = freq.get(word, 0) + 1
    return {w: math.log(n / f) for w, f in freq.items()}

def tfidf(tokens, all_docs_tokens):
    tf_scores = tf(tokens)
    idf_scores = idf(all_docs_tokens)
    return {w: tf_scores[w] * idf_scores.get(w, 0) for w in tf_scores}

def top_tfidf(tokens, all_docs_tokens, top=10):
    scores = tfidf(tokens, all_docs_tokens)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top]
