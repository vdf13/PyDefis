#!/bin/usr/python

import pokemondefis as script

# Définition de la classe de test du fichier pokemondefis.py


class Test_Pokemon:
    # Pokemon le plus rare
    def test_PokeRare(self):
        # On crée une instance de l'objet
        fichier = 'https://pydefis.callicode.fr/defis/PokePlusRare/input'
        resultat = script.Pokemon(fichier)
        assert ("aflamanoir", ('47', '-115', 0)) == resultat.result
