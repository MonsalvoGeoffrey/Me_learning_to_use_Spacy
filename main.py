import spacy
from spacy.matcher import Matcher
import json
import numpy as np
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")


matcher: Matcher = Matcher(nlp.vocab)

speak_lemmas = ["think", "say"]
pattern = [
    {"ORTH": "'"},
    {"IS_ALPHA": True, "OP":"+"},
    {"IS_PUNCT": True, "OP":"*"},
    {"ORTH": "'"},
    {"POS": "VERB", "LEMMA": {"IN": speak_lemmas}},
    {"POS": "PROPN", "OP": "+"},
    {"ORTH": "'"},
    {"IS_ALPHA": True, "OP":"+"},
    {"IS_PUNCT": True, "OP":"*"},
    {"ORTH": "'"}
]
matcher.add("PROPER_NOUN", [pattern], greedy="LONGEST")

doc = None
doc1 = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()
    doc = nlp(text)

with open("data/wiki_mlk.txt", "r") as f:
    text = f.read()
    doc1 = nlp(text)

with open("data/alice.json", "r") as f:
    data = json.load(f)
    text: str = data[0][2][0]
    text = text.replace("`", "'")
    print(text)
    doc2 = nlp(text)

matches = matcher(doc2)
matches.sort(key= lambda x:  x[1])
print(len(matches))
for match in matches[:10]:
    print(match, doc2[match[1]:match[2]])