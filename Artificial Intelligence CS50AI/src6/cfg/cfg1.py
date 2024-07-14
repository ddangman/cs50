import nltk

# Sentence -> Noun Phrase + Verb Phrase
# Adjective Phrase -> Adjective | Adjective + Adjective Phrase
# Noun Phrase -> Noun | Determiner + Noun | Adjective Phrase + Noun Phrase| Noun + Prepositional Phrase
# Prepositional Phrase -> Preposition + Noun Phrase
grammar = nltk.CFG.fromstring("""
    S -> NP VP

    AP -> A | A AP
    NP -> N | D NP | AP NP | N PP
    PP -> P NP
    VP -> V | V NP | V NP PP

    A -> "big" | "blue" | "small" | "dry" | "wide"
    D -> "the" | "a" | "an"
    N -> "she" | "city" | "car" | "street" | "dog" | "binoculars"
    P -> "on" | "over" | "before" | "below" | "with"
    V -> "saw" | "walked"
""")

parser = nltk.ChartParser(grammar)

sentence = input("Sentence: ").split()
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
except ValueError:
    print("No parse tree possible.")

# python cfg1.py
# Sentence: she saw the wide street
# Sentence: she saw the dog with the binoculars
# ambiguous. has two interpretation trees:
# she saw Verb_Phrase(with the binoculars)
# dog Prepositional_Phrase(with the binoculars)