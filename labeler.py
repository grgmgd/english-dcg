import nltk

tags_dict = {
    "DT": "det",
    "VB": "verb",
    "VBZ": "verb",
    "VBD": "verb",
    "VBN": "verb",
    "NN": "noun",
    "NNS": "noun",
    "JJ": "adj",
    "WP": "pronoun",
    "CC": "conjunction",
    "IN": "preposition",
    "PRP": "pronoun",
    "RB": "abverb"
}

labels_file = open("labels.pl", "w")

sentences = ["The young boy who worked for the old man pushed and stored a big box in the large empty room after school",
             "The old woman and the old man gave the poor young man whom they liked a white envelope in the shed behind the building",
             "Every boy quickly climbed some big tree while every girl secretly watched some boy",
             "Some brilliant students and many professors watched and admired talented lecturers and appreciated bright scientists and researchers"]

output = []

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    result = nltk.pos_tag(tokens)
    for word, tag in result:
        predicate = f'{tags_dict[tag]}({tags_dict[tag]}({word.lower()})) --> [{word.lower()}].\n'
        output.append(predicate)

output = list(set(output))
output.sort()
labels_file.write('\n'.join(output))
labels_file.close()
