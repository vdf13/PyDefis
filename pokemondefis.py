#!/bin/usr/python3

# Défis pydéfis POKEMON unique trouver le seul de la liste
# https://pydefis.callicode/PokePlusRare/input

import requests

r = requests.get('https://pydefis.callicode.fr/defis/PokePlusRare/input')
if r.status_code == 200:
    print('Success ! ')
elif r.status_code == 404:
    print('Not Found. ')
print(r.status_code)

# récupérer la partie texte de la page web
contenu = r.text.splitlines()

# nettoyage enlève les marques html  </body> <pre>....
liste_propre = []
for mot in contenu:
    if "<" not in mot:
        liste_propre.append(mot)

poke = {}
# faire une boucle en ne prenant que le nom en key et position en valeurs
for mot in liste_propre:
    if ' ' not in mot:
        cc = mot.split(",")
        if cc[0] in poke.keys():
            poke[cc[0]] = (cc[1], cc[2], "multiple")
        else:
            poke[cc[0]] = (cc[1], cc[2])

for key, value in poke.items():
    if "multiple" not in value:
        print("voici le pokemon unique :", key, value)
