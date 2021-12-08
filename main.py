import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

    doc = nlp(text)


for ent in doc.ents:
    print(ent.text, ent.label_)

displacy.serve(doc, style="ent")