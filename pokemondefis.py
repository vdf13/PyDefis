#!/bin/usr/python3

# Défis pydéfis POKEMON unique trouver le seul de la liste
# https://pydefis.callicode/PokePlusRare/input

import requests


class Pokemon:
    # Défis Pokemon c0d1ngUP 2017

    def __init__(self, fichier):
        self.fichier = fichier
        self.result = ""
        self.ouverture()
        self.nettoyage()

    def ouverture(self):
        r = requests.get(self.fichier)
        if r.status_code == 200:
            print('Success ! ')
        elif r.status_code == 404:
            print('Not Found. ')
        print(r.status_code)
        # récupérer la partie texte de la page web
        self.contenu = r.text.splitlines()
        return self.contenu

    def nettoyage(self):
        # nettoyage enlève les marques html  </body> <pre>....
        liste_propre = []
        for mot in self.contenu:
            if "<" not in mot:
                liste_propre.append(mot)
        poke = {}
        # faire une boucle en ne prenant que
        # le nom en key et position en valeurs
        for mot in liste_propre:
            if ' ' not in mot:
                cc = mot.split(",")
                cc.append(0)
                if cc[0] in poke.keys():
                    val = poke[cc[0]]
                    val[2] += 1
                    poke[cc[0]] = val
                else:
                    poke[cc[0]] = [cc[1], cc[2], cc[3]]
        poke1 = sorted(poke.items(), key=lambda t: t[1][2])
        self.result = poke1[0]
        return self.result


fichier1 = 'https://pydefis.callicode.fr/defis/PokePlusRare/input'
poke_rare = Pokemon(fichier1)
print(poke_rare.result)

fichier2 = 'https://pydefis.callicode.fr/defis/PokePlusRare2/input'
poke_plus_rare = Pokemon(fichier2)
print(poke_plus_rare.result)
