import spacy
from spacy.matcher import Matcher
import json
import numpy as np
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")


ruler: spacy.pipeline.entityruler.EntityRuler = nlp.add_pipe("entity_ruler", before="ner")

speak_lemmas = ["think", "say"]
patterns = [
        {"ORTH": "'"},
        {"IS_ALPHA": True, "OP": "+"},
        {"IS_PUNCT": True, "OP": "*"},
        {"ORTH": "'"},
        {"POS": "VERB", "LEMMA": {"IN": speak_lemmas}},
        {"POS": "PROPN", "OP": "+"},
        {"ORTH": "'"},
        {"IS_ALPHA": True, "OP": "+"},
        {"IS_PUNCT": True, "OP": "*"},
        {"ORTH": "'"}
    ]
#matcher.add("PROPER_NOUN", patterns, greedy="LONGEST")
ruler.add_patterns([{"label": "MY_ENTITY", "pattern": patterns}])

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

displacy.serve(doc2, style="ent")