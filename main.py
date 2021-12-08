import spacy
from spacy.matcher import Matcher
import numpy as np
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")


matcher: Matcher = Matcher(nlp.vocab)

pattern = [{"POS": "PROPN"}]
matcher.add("PROPER_NOUN", [pattern])

doc = None
doc1 = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()
    doc = nlp(text)

with open("data/wiki_mlk.txt", "r") as f:
    text = f.read()
    doc1 = nlp(text)


matches = matcher(doc1)
print(len(matches))
for match in matches[:10]:
    print(match, doc1[match[1]:match[2]])