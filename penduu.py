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
    def deviner_lettre():
    while True:
        lettre = input("Devinez une lettre : ").lower()
        if len(lettre) == 1 and lettre.isalpha():
            return lettre
        else:
            print("Veuillez entrer une seule lettre valide.")

def jouer_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    essais_restants = 9

    print("Bienvenue au jeu du pendu !")
    print("Le mot à deviner a", len(mot_a_deviner), "lettres.")
    while essais_restants > 0:
        mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print("Mot actuel :", mot_cache)
        print("Il vous reste", essais_restants, "essais sur 9.")

        lettre = deviner_lettre()

        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre. Essayez une autre.")
        elif lettre in mot_a_deviner:
            print("Bien joué ! La lettre", lettre, "est dans le mot.")
            lettres_trouvees.append(lettre)
        else:
            print("La lettre", lettre, "n'est pas dans le mot.")
            essais_restants -= 1

        if set(lettres_trouvees) == set(mot_a_deviner):
            print("Félicitations ! Vous avez trouvé le mot :", mot_a_deviner)
            break

