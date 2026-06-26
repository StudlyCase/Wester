from collections import Counter

def word_freq(tokens, top=20):
    return Counter(tokens).most_common(top)

def char_freq(text, top=10):
    return Counter(c for c in text.lower() if c.isalpha()).most_common(top)
