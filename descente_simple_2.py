## AMION OKOUE JEAN JAURES DAVY M1INFO ##

import random
import statistics


def voisins(tab, index, range):
    ## Les voisins d'un élément sont les éléments de la liste appartenant à l'intervalle [valeur-rang,valeur+rang].
    ## La fonction retourne les index des éléments du tableau voisins avec l'élément d'indice index.
    listVoisins = []
    for element in tab:
        if element < tab[index]-range or element > tab[index]+range:
            pass
        else:
            listVoisins.append(tab.index(element))
    return listVoisins


def indexMaxVoisins(tab, voisins):
    for element in voisins:
        if voisins.index(element) == 0:
            max = element
        elif tab[max] < tab[element]:
            max = element
    return max


def descente_simple(tab, range):
    index = random.randrange(len(tab))
    index_max = indexMaxVoisins(tab, voisins(tab, index, range))
    print(f"La solution initiale est {tab[index]}")
    print(f"index = {index} et {index_max}")
    while index != index_max:
        index = index_max
        index_max = indexMaxVoisins(tab, voisins(tab, index, range))
        print(f"index = {index} et {index_max}")
    return tab[index_max]


listS = [15, 18, 21, 17, 14, 23]
rang = round(statistics.pstdev(listS))
# le rang de l'intervalle de voisinnage représente l'écart type de la liste, c'est à dire l'espacement moyen des
# différentes valeurs de la liste. On aura ainsi un intervalle permettant toujours de trouver le maximum global.
print(f"Le rang de l'intervalle sera {rang}")
print(f"Le maximum global est {descente_simple(listS,rang)}")
