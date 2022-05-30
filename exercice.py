#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def ellipsoïde(a = 1, b = 2, c = 3, masse_volumique = 4): # m = p * V
    volume = (4/3) * math.pi * a * b * c
    masse = masse_volumique * volume 

    return "Le volume est de {:.2f} unité et la masse de {:.2f} unité." .format(volume, masse)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(ellipsoïde())
    pass
