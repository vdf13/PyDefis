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


class MeliMeloBinaire:
    ''' Construire une suite de nombre après transformation binaire
    - 34 = 100010 , compter nombre de 1 = 10, ajouter à la fin 10001010 = 138
    - renouveler 'n' fois
    - donner le nombre final sous la forme base 10 '''

    def __init__(self, entree, iteration):
        self.nombre = entree
        self.n = iteration
        self.binaire()

    def binaire(self):
        conv_bin = str(bin(self.nombre))
        conv_bin = conv_bin[2:]
        while self.n > 0:
            count = ''
            count = conv_bin.count('1')
            conv_bin1 = (str(bin(count)))[2:]
            conv_bin += conv_bin1
            self.n -= 1
        self.nombre = int(conv_bin, 2)
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
        nb = lim_basse
        self.nombre = []
        while nb <= lim_haute:
            res = set(str(nb**2) + str(nb**3))
            if len(res) == 10:
                if len(self.nombre) < qte:
                    self.nombre.append(nb)
            nb += 1
        return self.nombre


class Einstein:
    ''' Code de l'objet Einstein et formule E = m*c**2
    - m et c doivent être des nombres premiers
    - Trouver 4 nombres impairs consécutif (diff de 2 entre nombres)
    '''
    def __init__(self):
        self.nombre = self.calcul(300)

    def premier(self, nb):
        ''' Détermine si le nombre fournit en entrée est premier '''
        for i in range(2, nb):
            if (nb % i == 0):
                return False
        return True

    def calcul(self, fin):
        ''' Crée la liste des nombres premiers en 'm'
        et effectue une copie de cette liste en 'c' '''
        m = []
        for i in range(2, fin):
            if self.premier(i):
                m.append(i)
        c = m.copy()
        # Créer la liste des nombres suivant la formule E = m * c**2
        liste_e = []
        for i in m:
            for j in c:
                e = i*j**2
                liste_e.append(e)
        liste_e.sort()   # On ordonne la liste par ordre croissant
        # Boucle pour trouver des nombres impairs qui se suivent
        for i in liste_e:
            if i + 2 in liste_e and i + 4 in liste_e and i + 6 in liste_e:
                m = (i, i + 2, i + 4, i + 6)
        return m


# #### Lancement des instances #####

# Méli Mélo de nombres
resultat = MeliMelo(2963, 105)
print("Défi Méli Mélo :", resultat.nombre)

# Meli Melo Binair
resultat = MeliMeloBinaire(53, 21)
print("Défi Méli Mélo Binaire : ", resultat.nombre)

# Nombre Riche
resultat = NombreRiche()
resultat.calcul(5300, 5500, 13)
print("Défi Nombre Riche : ", resultat.nombre)

# Nombre de Einstein
resultat = Einstein()
print("Défi Einstein : ", resultat.nombre)
