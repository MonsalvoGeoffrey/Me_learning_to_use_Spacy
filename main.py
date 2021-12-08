import spacy

nlp = spacy.load("en_core_web_sm")

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

    doc = nlp(text)


sentence = list(doc.sents)[0]
token3 = sentence[2]
print(sentence)
print(token3)
print(token3.text)
print(token3.left_edge)
print(token3.right_edge)
print(token3.ent_type)
print(token3.ent_type_)
print(token3.ent_iob)
print(token3.ent_iob_)
print(token3.lemma)
print(token3.lemma_)
print(sentence[12].lemma)
print(sentence[12].lemma_)
print(token3.morph)
print(token3.pos_)
print(sentence[12].pos_)
print(token3.dep_)
print(sentence[12].dep_)
print(token3.lang_)