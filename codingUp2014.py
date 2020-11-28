#!/bin/usr/python3

# Fichier code des défis python tiré du c0d1ngUP 2014

class CodingUp2014:
    pass


class MeliMelo:
    ''' Trouver un nombre après plusieurs itération "n" en applicant
    la formule : somme 2 par 2 ex (34+56 * 188 + 188)%9973
    - afficher nombre  '''
    def __init__(self, nombre, n):
        self.nombre = str(nombre)
        self.n = n
        self.calcul()

    def calcul(self):
        while self.n > 0:
            self.n += -1
            b = self.nombre[-2:]
            c = self.nombre.replace(b, '')
            self.nombre = str(((int(b) + int(c)) * 188 + 188) % 9973)
        return self.nombre


class NombreRiche:
    ''' Trouver les nombres riches (ayant 1 fois chaque chiffre)
    entre 2 série de nombre
    - formule nb**2 + nb**3 doit avoir 10 chiffres
    '''
    def __init__(self, limite_basse=68, limite_haute=69, qte=1):
        self.lim_basse = limite_basse
        self.lim_haute = limite_haute
        self.calcul(self.lim_basse, self.lim_haute)

    def calcul(self, lim_basse, lim_haute, qte=5):
        ''' 3 paramètres : limite basse, limite haute,quantité '''
        dix = '0123456789'
        nb = lim_basse
        self.nombre = []
        while nb <= lim_haute:
            res = sorted(str(nb**2) + str(nb**3))
            taille = len(res)
            try:
                for i in dix:
                    res.remove(i)
                if len(res) == taille - 10:
                    if len(self.nombre) < qte:
                        self.nombre.append(nb)
            except ValueError:
                next
            nb += 1
        return self.nombre


# #### Lancement des instances #####

# Méli Mélo de nombres
resultat = MeliMelo(2963, 105)
print(resultat.nombre)

# Nombre Riche
resultat = NombreRiche()
resultat.calcul(5300, 5500, 13)
print(resultat.nombre)
