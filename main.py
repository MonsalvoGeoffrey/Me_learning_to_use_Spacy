import spacy
import numpy as np
from spacy import displacy

#nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_trf")

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

    doc = nlp(text)


setence = list(doc.sents)[0]

my_word = "country"

ms = nlp.vocab.vectors.most_similar(np.asarray([nlp.vocab.vectors[nlp.vocab.strings[my_word]]]), n = 10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]

print(words)