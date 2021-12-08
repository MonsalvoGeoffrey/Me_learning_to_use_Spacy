import spacy
import numpy as np
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")


ruler: spacy.pipeline.entityruler.EntityRuler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "GPE", "pattern": "West Chestertenfieldville"},
    {"label": "FILM", "pattern": "Mr. Deeds"},
]

ruler.add_patterns(patterns)

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

    doc = nlp(text)


text = "West Chestertenfieldville was referenced in Mr. Deeds."
doc1 = nlp(text)

for ent in doc1.ents:
    print(ent.text, ent.label_)