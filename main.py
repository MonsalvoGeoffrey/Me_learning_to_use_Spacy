import spacy
from spacy.matcher import Matcher
import numpy as np
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")


matcher: Matcher = Matcher(nlp.vocab)

pattern = [{"LIKE_EMAIL": True}]
matcher.add("EMAIL_ADDRESS", [pattern])

doc = None
doc1 = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()
    doc = nlp(text)

with open("data/wiki_mlk.txt", "r") as f:
    text = f.read()
    doc1 = nlp(text)

doc2 = nlp("This is my email address: example@example.com")
matches = matcher(doc2)
print(matches)
print(nlp.vocab[matches[0][0]].text)
