import spacy
from spacy.language import Language
from spacy.matcher import Matcher
import json
import numpy as np
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")

@Language.component("remove_gpe")
def remove_gpe(doc):
    original_ents = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            original_ents.remove(ent)
    doc.ents = original_ents
    return doc

nlp.add_pipe("remove_gpe")

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()
    doc = nlp(text)

doc1 = nlp("Britain is a place. January is a doctor.")

for ent in doc1.ents:
    print(ent.text, ent.label_)

print("test")