#!/usr/bin/python3.7

# Code python pour les défis python du site https://pydefis.callicode.fr


class SW4Vitesse:
    ''' Classe définissant l'objet défis SW4 Vitesse Lumière
    - x -y -z sont les coordonnées en entrée
    - fonction qui calcule les nouvelle coordonnées
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def Vitesse(self):
        vitesse = []
        while 10 * self.x > self.y:
            self.x = (self.y * self.z) % 10000
            self.y = (3 * self.z) % 10000
            self.z = (7 * self.z) % 10000
        vitesse = [self.x, self.y, self.z]
        print("SW4 Vitesse : Coordonnées de passage ", vitesse)
        return vitesse


class SW4LunetteAstro:
    ''' Classe définissant l'objet pydéfis SW4 Lunette Astro
    - x -y coordonnées entrée, i nombre d'itération de la fonction '''

    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i

    def Calcul(self):
        astro = []
        for occ in range(self.i):
            x1 = (self.x + 2 * self.y) % 2018
            y1 = (-3 * self.x + self.y) % 2018
            self.x = x1
            self.y = y1
        dec = (self.x - 900) / 10
        asc = (self.y / 150) * 2
        astro = [dec, asc]
        print("SW4 Lunette Astro : Déclinaison, ascension :", astro)
        return astro


class SW7EwokName1:
    ''' Classe définissant l'objet du pydéfis SW7 Ewok Name
    - liste de noms
    - Fonction qui cherche combien on un 'a' ou 'A' '''

    def __init__(self, names):
        self.names = names

    def NombreA(self):
        count = 0
        for name in self.names:
            if "a" in name.lower():
                pass
            else:
                count += 1
        print("SW7 Ewok Name: Nombre de Ewok sans lettre 'a', 'A' :", count)
        return(count)


class SW7EwokName2:
    ''' Classe définissant l'objet du pydéfis Ewok Name 2
    - liste de noms en entrée
    - Fonction qui compte combien on 2 *+ de consonnes que voyelles '''

    def __init__(self, names):
        self.names = names

    def Double_Voyelle(self):
        count = 0
        for name in self.names:
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
resultat = SW4Vitesse(997, 312, 663)
print(resultat.Vitesse())

# SW4 Lunette Astro
resultat = SW4LunetteAstro(1694, 1546, 50)
print(resultat.Calcul())

# SW7 Ewok names I
file_to_open = "fichiers_source//ewok_names.txt"
with open(file_to_open, "r") as file:
    names = file.readlines()
resultat = SW7EwokName1(names)
print(resultat.NombreA())

# SW7 Ewok names 2
file_to_open = "fichiers_source//ewok_names2.txt"
with open(file_to_open, "r") as file:
    names = file.readlines()
resultat = SW7EwokName2(names)
print(resultat.Double_Voyelle())
