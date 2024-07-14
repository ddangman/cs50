import nltk

# Sentence -> Noun Phrase + Verb Phrase
# Noun Phrase -> Determiner + Noun | Noun
# Verb Phrase -> Verb | Verb + Noun Phrase
# Determiner -> "the" | "a"
# Noun -> "she" | "city" | "car"
# Verb -> "saw" | "walked"
grammar = nltk.CFG.fromstring("""
    S -> NP VP

    NP -> D N | N
    VP -> V | V NP

    D -> "the" | "a"
    N -> "she" | "city" | "car"
    V -> "saw" | "walked"
""")

parser = nltk.ChartParser(grammar)

sentence = input("Sentence: ").split()
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
except ValueError:
    print("No parse tree possible.")

# python cfg0.py
# Sentence: she walked
# Sentence: she saw the city

