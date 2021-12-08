import spacy
import numpy as np
from spacy import displacy

#nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")

nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

    doc = nlp(text)


#displacy.serve(doc, style="ent")
print(nlp.analyze_pipes())