import random

def choisir_mot():
    mots = ["python", "codage", "enfant", "jeu", "informatique", "objet"]
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache