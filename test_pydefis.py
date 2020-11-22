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
        assert [501, 9461, 5409] == script.PyDefisSW.SW4_Vitesse(x, y, z)

    # SW IV : LunetteAstro . Il a mit son mot de passe sur un post-it
    def test_SW4_LunetteAstro(self):
        x = 1694
        y = 1546
        i = 50
        assert [44, 4] == script.PyDefisSW.SW4_LunetteAstro(x, y, i)

    # SW VII le noms de Ewoks !
    # Combien ne contiennent pas de a ou A ?
    def test_SW7_EwokName(self):
        names = ["Albert", "Barnabé", "Chris"]
        assert 1 == script.PyDefisSW.SW7_EwokName(names)
