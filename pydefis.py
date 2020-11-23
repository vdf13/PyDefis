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

    def vitesse(self):
        resultat = []
        while 10 * self.x > self.y:
            self.x = (self.y * self.z) % 10000
            self.y = (3 * self.z) % 10000
            self.z = (7 * self.z) % 10000
        resultat = [self.x, self.y, self.z]
        print("SW4 Vitesse : Coordonnées de passage ", resultat)
        return resultat


class SW4LunetteAstro:
    ''' Classe définissant l'objet pydéfis SW4 Lunette Astro
    - x -y coordonnées entrée, i nombre d'itération de la fonction '''

    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i

    def calcul(self):
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

    def nombre_A(self):
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

    def double_voyelle(self):
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
        print("SW7 Ewok Name 2 :Nombre de Ewoks avec \
le double de consonnes dans le nom :", count)
        return count


class SW1Porte:
    ''' Classe définissant l'ojet du pydéfis A l'assaut de Gunray, découpage porte
    - E = épaisseur que le sabre perce durant 1 seconde
    - Volume métal en fusion V = 8*E en cm3 : initial V=0
    - E = 3-0.005*V Epaisseur après 1 seconde: initial E=0:
    - 1s E=3 V=24 : 2s E=5.88 V=47.04 : 3s E=8.6448 V=69.1584
    - Epaisseur de la porte = 70 cm
    - Temps pour percer la moitié de la porte ?
    - Temps pour percer la porte entièrement ?
    - Réponse 2 nombres entiers ex: 10, 24
    '''
    def __init__(self):
        self.epaisseur_porte = 70
        self.volume_metal = 0
        self.metal = 0
        self.profondeur_percage = 0
        self.perce = 0

    def percage(self):
        ''' Formule E = 3 - 0.005 * V '''
        secondes = 0
        resultat = []
        moitie = False
        while self.profondeur_percage < self.epaisseur_porte:
            self.perce = 3 - 0.005 * self.volume_metal
            self.metal = 8 * self.perce
            self.volume_metal += self.metal
            self.profondeur_percage += self.perce
            secondes += 1
            if self.profondeur_percage > self.epaisseur_porte / 2:
                if moitie is True:
                    pass
                else:
                    # Nombre de secondes pour la moitié de la porte
                    resultat.append(secondes)
                    moitie = True
        # On obtient le nombre de secondes pour la port entière
        resultat.append(secondes)
        print("SW1 Percage de la porte : \
moitié / complet en secondes :", resultat)
        return resultat


# ##### Partie Principale, appel des objets #####

# SW4 Vitesse lumière
resultat = SW4Vitesse(997, 312, 663)
print(resultat.vitesse())

# SW4 Lunette Astro
resultat = SW4LunetteAstro(1694, 1546, 50)
print(resultat.calcul())

# SW7 Ewok names I
file_to_open = "fichiers_source//ewok_names.txt"
with open(file_to_open, "r") as file:
    names = file.readlines()
resultat = SW7EwokName1(names)
print(resultat.nombre_A())

# SW7 Ewok names 2
file_to_open = "fichiers_source//ewok_names2.txt"
with open(file_to_open, "r") as file:
    names = file.readlines()
resultat = SW7EwokName2(names)
print(resultat.double_voyelle())

# SW1 Percage Porte Gunray
resultat = SW1Porte()
print(resultat.percage())
