import spacy

nlp = spacy.load("en_core_web_sm")

with open("data/wiki_us.txt", "r") as f:
    text = f.read()
    print(text)