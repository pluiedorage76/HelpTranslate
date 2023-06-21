import os
os.system("pip install importlib")
os.system("pip install nltk")
from nltk.corpus import words

# Charger le dictionnaire anglais
english_words = words.words()

# Vérifier si un mot est dans le dictionnaire
if 'apple' in english_words:
    print("Le mot 'apple' est dans le dictionnaire anglais.")
