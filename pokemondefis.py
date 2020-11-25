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
                    poke[cc[0]] = (cc[1], cc[2], cc[3] + 1)
                else:
                    poke[cc[0]] = (cc[1], cc[2], cc[3])
        for key, value in poke.items():
            if 0 in value:
                self.result = key, value
        return self.result


fichier = 'https://pydefis.callicode.fr/defis/PokePlusRare/input'
poke_rare = Pokemon(fichier)
print(poke_rare.result)
