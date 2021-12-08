import spacy

nlp = spacy.load("en_core_web_sm")

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

    doc = nlp(text)

for token in text[0:10]:
    print(token)

for token in doc[:10]:
    print(token)
