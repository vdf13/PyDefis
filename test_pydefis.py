#!/usr/bin/python3.7

# Tests unitaires des défis Python du site https://pydefis.callicode.fr

import pydefis as script


# Définition de la class pour les projets SW4
class TestPyDefisSW:
    # SW IV : On passe en vitesse lumière
    def test_SW4_Vitesse(self):
        x = 997
        y = 312
        z = 663
        # On crée une instance de l'objet avec les valeurs a tester
        resultat_vitesse = script.SW4Vitesse(x, y, z)
        assert [501, 9461, 5409] == resultat_vitesse.Vitesse()

    # SW IV : LunetteAstro . Il a mit son mot de passe sur un post-it
    def test_SW4_LunetteAstro(self):
        x = 1694
        y = 1546
        i = 50
        # On crée une instance de l'objet avec les valeurs a tester
        resultat_lunette = script.SW4LunetteAstro(x, y, i)
        assert [44, 4] == resultat_lunette.Calcul()

    # SW VII : le nom de Ewoks !
    # Combien ne contiennent pas de a ou A ?
    def test_SW7_EwokName(self):
        names = ["Albert", "Barnabé", "Chris"]
        resultat_ewok1 = script.SW7EwokName1(names)
        assert 1 == resultat_ewok1.NombreA()

    # SW VII : Le nom des Ewoks 2 !
    # Combien contiennent 2 fois plus de consonnes que de voyelles ?
    def test_SW7_EwokName2(self):
        names = ["Albert", "Barnabé", "Chris"]
        resultat_ewok2 = script.SW7EwokName2(names)
        assert 1 == resultat_ewok2.Double_Voyelle()
