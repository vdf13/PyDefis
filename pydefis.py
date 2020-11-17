#!/usr/bin/python3.7

# Code python pour les défis python du site https://pydefis.callicode.fr


class PyDefisSW:
    def SW4_Vitesse(x, y, z):
        list = []
        while 10 * x > y:
            x = (y * z) % 10000
            y = (3 * z) % 10000
            z = (7 * z) % 10000
        list = [x, y, z]
        print(list)
        return list


PyDefisSW.SW4_Vitesse(997, 312, 663)
