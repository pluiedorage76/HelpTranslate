"""
import os
os.system("pip install importlib")
os.system("pip install nltk")
import nltk
nltk.download('words')
from nltk.corpus import words

# Charger le dictionnaire anglais
import nltk
nltk.download('fr')
english_words = words.words()

# Vérifier si un mot est dans le dictionnaire
if 'apple' in english_words:
    print("Le mot 'apple' e

import nltk
nltk.download('fr')

from nltk.corpus import words
from nltk.translate import Translator

english_words = words.words()

# Créer un traducteur pour traduire de l'anglais vers le français
translator = Translator(from_lang="english", to_lang="french")

# Ouvrir un fichier pour écrire les mots anglais et leurs traductions
with open("mots_anglais_et_traductions.txt", "w", encoding="utf-8") as file:
    for word in english_words:
        # Traduire le mot anglais en français
        translation = translator.translate(word)
        
        # Écrire le mot anglais et sa traduction dans le fichier
        file.write(f"{word}: {translation}\n")

"""

from nltk.corpus import words
from translate import Translator

english_words = words.words()

# Créer un traducteur pour traduire de l'anglais vers le français
translator = Translator(to_lang="fr")

# Ouvrir un fichier pour écrire les mots anglais et leurs traductions
with open("mots_anglais_et_traductions.txt", "w", encoding="utf-8") as file:
    for word in english_words:
        # Traduire le mot anglais en français
        translation = translator.translate(word)
        
        # Écrire le mot anglais et sa traduction dans le fichier
        file.write(f"{word}: {translation}\n")
