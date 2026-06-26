from loader import load_docs
from tokenizer import tokenize, sentences
from stopwords import filter_stopwords
from frequency import word_freq
from sentiment import sentiment
from ngrams import top_ngrams
from tfidf import top_tfidf

def analyze_doc(name, text, all_filtered):
    tokens = tokenize(text)
    filtered = filter_stopwords(tokens)
    sents = sentences(text)

    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")
    print(f"  chars: {len(text)}  |  tokens: {len(tokens)}  |  unique: {len(set(tokens))}  |  sentences: {len(sents)}")

    print(f"\n  top words")
    for word, count in word_freq(filtered, top=10):
        print(f"    {word}: {count}")

    print(f"\n  sentiment")
    s = sentiment(filtered)
    print(f"    {s['label']} (score: {s['score']}, pos: {s['positive']}, neg: {s['negative']})")

    if len(tokens) >= 5:
        print(f"\n  top 5-grams")
        for i, (gram, count) in enumerate(top_ngrams(tokens, n=5, top=3), 1):
            preview = " ".join(gram[:8]) + " ..."
            print(f"    [{i}] ({count}x) {preview}")
    else:
        print(f"\n  [50-gram skipped: only {len(tokens)} tokens, need 5]")

    print(f"\n  tf-idf top terms")
    for word, score in top_tfidf(filtered, all_filtered, top=10):
        print(f"    {word}: {score:.4f}")

    return filtered

def run():
    print("- Wester: The Community driven NLP. -")
    docs = load_docs("docs")
    if not docs:
        return

    print(f"\nloaded {len(docs)} document(s): {', '.join(docs.keys())}")

    all_tokens = {name: filter_stopwords(tokenize(text)) for name, text in docs.items()}
    all_filtered = list(all_tokens.values())

    for name, text in docs.items():
        analyze_doc(name, text, all_filtered)

    print(f"\n{'='*60}")
    print(f"  corpus summary")
    print(f"{'='*60}")
    combined = [t for tokens in all_filtered for t in tokens]
    print(f"  total tokens (filtered): {len(combined)}")
    print(f"  total unique terms: {len(set(combined))}")
    print(f"\n  CORPUS TOP WORDS")
    for word, count in word_freq(combined, top=15):
        print(f"    {word}: {count}")
