#!/bin/usr/python3

# Défis tirés de C0d1ngUP 2014

import codingUp2014 as script


class TestCodingup2014:
    ''' Classe définissant les objets des défis du codingUP 2014
    - Méli Mélo de Nombre
    '''

    def test_meliMelo(self):
        ''' Trouver un nombre après plusieurs itération n en applicant
        la formule somme 2 par 2 ex 34 et 56 puis *188 +188)%9973
        - afficher le nombre '''
        self.nombre = "3456"
        n = 5
        resultat = script.MeliMelo(self.nombre, n)
        assert '3742' == resultat.nombre

    def test_meliMeloBinaire(self):
        ''' Construire une suite de nombre
        - le convertir en binaire
        - Compter le nombre de 1 ++++
        - test 5 en entrée , 4 itérations == 5871 '''
        self.nombre = 5
        n = 4
        resultat = script.MeliMeloBinaire(self.nombre, n)
        assert 5871 == resultat.nombre

    def test_NombreRiche(self):
        ''' Test de l'ojet NombreRiche et de la méthode calcul() '''
        self.lim_basse = 66
        self.lim_haute = 70
        resultat = script.NombreRiche(self.lim_basse, self.lim_haute)
        assert [69] == resultat.nombre
