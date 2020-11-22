#!/usr/bin/python3.7

# Code python pour les défis python du site https://pydefis.callicode.fr


class PyDefisSW:
    def SW4_Vitesse(x, y, z):
        vitesse = []
        while 10 * x > y:
            x = (y * z) % 10000
            y = (3 * z) % 10000
            z = (7 * z) % 10000
        vitesse = [x, y, z]
        print("Coordonnées de passage en vitesse lumière", vitesse)
        return vitesse

    def SW4_LunetteAstro(x, y, i):
        astro = []
        for occ in range(i):
            x1 = (x + 2 * y) % 2018
            y1 = (-3 * x + y) % 2018
            x = x1
            y = y1
        dec = (x - 900) / 10
        asc = (y / 150) * 2
        astro = [dec, asc]
        print("Déclinaison, ascension :", astro)
        return astro

    def SW7_EwokName(names):
        count = 0
        for name in names:
            if "a" in name.lower():
                pass
            else:
                count += 1
        print("Nombre de Ewok sans lettre 'a' ou 'A' :", count)
        return(count)

    def SW7_EwokName2(names):
        count = 0
        for name in names:
            # compter les voyelles
            voyelle = 0
            for lettre in name.lower():
                if lettre == "a" \
                        or lettre == "e" \
                        or lettre == "i" \
                        or lettre == "o" \
                        or lettre == "u" \
                        or lettre == "y":
                    voyelle += 1
            if ((len(name) - 1) - voyelle) / voyelle == 2:
                count += 1
        print("Nombre de Ewoks avec \
                le double de consonnes dans le nom :", count)
        return count


# SW4 Vitesse lumière
PyDefisSW.SW4_Vitesse(997, 312, 663)

# SW4 Lunette Astro
PyDefisSW.SW4_LunetteAstro(1694, 1546, 50)

# SW7 Ewok names
file_to_open = "fichiers_source//ewok_names.txt"
with open(file_to_open, "r") as file:
    names = file.readlines()
PyDefisSW.SW7_EwokName(names)

# SW7 Ewok names 2
file_to_open = "fichiers_source//ewok_names2.txt"
with open(file_to_open, "r") as file:
    names = file.readlines()
PyDefisSW.SW7_EwokName2(names)
