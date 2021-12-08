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

doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast Food taste very good.")
doc3 = nlp("The Empire State Building is in New-York.")

print(doc1, "<->", doc2, doc1.similarity(doc2))
print(doc1, "<->", doc3, doc1.similarity(doc3))

doc4 = nlp("I enjoy oranges.")
doc5 = nlp("I enjoy apples.")
doc6 = nlp("I enjoy burgers.")

print(doc4, "<->", doc5, doc4.similarity(doc5))
print(doc4, "<->", doc6, doc4.similarity(doc6))

#my_word = "country"

#ms = nlp.vocab.vectors.most_similar(np.asarray([nlp.vocab.vectors[nlp.vocab.strings[my_word]]]), n = 10)
#words = [nlp.vocab.strings[w] for w in ms[0][0]]

#print(words)