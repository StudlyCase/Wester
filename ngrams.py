from collections import Counter

def ngrams(tokens, n=5):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

def ngram_freq(tokens, n=5):
    return Counter(ngrams(tokens, n))

def top_ngrams(tokens, n=5, top=10):
    freq = ngram_freq(tokens, n)
    return freq.most_common(top)
