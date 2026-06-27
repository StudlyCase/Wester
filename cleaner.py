import re

def clean(text):
    lines = [l for l in text.splitlines() if '//' not in l]
    text = '\n'.join(lines)
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
