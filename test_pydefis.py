#!/usr/bin/python3.7

# SW IV : On passe en vitesse lumière
import pydefis as script


class TestPyDefisSW:
    def test_SW4_Vitesse(self):
        x = 997
        y = 312
        z = 663
        assert [501, 9461, 3] == script.PyDefisSW.SW4_Vitesse(x, y, z)
