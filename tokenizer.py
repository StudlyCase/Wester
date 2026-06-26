import re

def tokenize(text):
    return re.findall(r"\b[a-zA-Z']+\b", text.lower())

def sentences(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())
