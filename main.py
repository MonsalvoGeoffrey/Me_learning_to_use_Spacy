import spacy
from spacy.matcher import Matcher
import json
import numpy as np
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")



doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()
    doc = nlp(text)

