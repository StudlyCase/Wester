import os
from cleaner import clean

def load_docs(folder="docs"):
    docs = {}
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"[loader] created '{folder}/'; place .txt files there.")
        return docs
    for fname in sorted(os.listdir(folder)):
        if fname.endswith(".txt"):
            path = os.path.join(folder, fname)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                docs[fname] = clean(f.read())
    if not docs:
        print(f"[loader] no .txt files found in '{folder}/'.")
    return docs
