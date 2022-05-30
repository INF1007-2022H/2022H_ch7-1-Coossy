#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import * 
color('green') 

# TODO: Définissez vos fonction ici
def ellipsoïde(a = 1, b = 2, c = 3, masse_volumique = 4): # m = p * V
    volume = (4/3) * math.pi * a * b * c
    masse = masse_volumique * volume 

    return "Le volume est de {:.2f} unité et la masse de {:.2f} unité." .format(volume, masse)


def dictionnaire_lambda(phrase = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"):
    dictionnaire = dict()
    for char in phrase:
        dictionnaire[char] = phrase.count(char)

    return (sorted(dictionnaire, key=dictionnaire.__getitem__, reverse = True))


def arbre_recursif(n = 4):
    if n>0:
        pensize(5)
        forward(100)
        left(45)
        speed(1)
        arbre_recursif(n-1)





if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(ellipsoïde())
    #print(dictionnaire_lambda())
    print(arbre_recursif())
    
    pass
