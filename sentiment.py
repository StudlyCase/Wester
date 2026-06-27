POS = set()
NEG = set()

def sentiment(tokens):
    pos = sum(1 for t in tokens if t in POS)
    neg = sum(1 for t in tokens if t in NEG)
    score = pos - neg
    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"
    return {"positive": pos, "negative": neg, "score": score, "label": label}
