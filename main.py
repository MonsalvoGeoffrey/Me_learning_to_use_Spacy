import spacy

nlp = spacy.load("en_core_web_sm")

doc = None

with open("data/wiki_us.txt", "r") as f:
    text = f.read()

    doc = nlp(text)

for token in text[0:10]:
    print(token)

for token in doc[:10]:
    print(token)

for sent in doc.sents:
    print(sent)

sentence1 = list(doc.sents)[0]
print(sentence1)
sentence5 = list(doc.sents)[4]
print(sentence5)
print(len(list(doc.sents)))
for token in sentence5:
    print(token)