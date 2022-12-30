import random
import statistics
import copy

# def voisinsNonTabou(tab:list, index:int, tabou:list) -> list:
#     listVoisins = []
#     rang = round(statistics.pstdev(tab))
#     for element in tab:
#         if element < tab[index]-rang or element > tab[index]+rang:
#             pass
#         elif(tab.index(element) not in tabou):
#             listVoisins.append(tab.index(element))
    
#     return listVoisins

def voisinsNonTabou(tab:list ,index:int ,tabou:list) -> list:
    listVoisins = []
    tabs = copy.copy(tab)
    listIndex = [-2,-1,1,2]
    for element in tabou:
        for i in range(tab.count(tab[element])):
            tabs.remove(tab[element])
    if len(tabs) == 0:
        return listVoisins
    else:
        for element in listIndex:
            try:
                value = tabs[(index+element)%len(tabs)]
                listVoisins.append(tab.index(value))
            except IndexError:
                pass
        if index not in tabou:
            listVoisins.insert(0,index)
        return listVoisins
        
        
def printTab(tab:list ,tabValue:list) -> list:
    arr = []
    for element in tab:
        arr.append(tabValue[element])
    return arr


def indexMinVoisins(tab:list, voisins:list) -> int:
    if len(voisins) > 0:
        for element in voisins:
            if voisins.index(element) == 0:
                min = element
            elif tab[min] > tab[element]:
                min = element
    else:
        min = None
    return min


def rechercheTabou(tab:list):
    # indexMinG = random.randrange(len(tab)-1)
    indexMinG = 4
    print(f"Solution initiale = {tab[indexMinG]}")
    indexMinL = indexMinG
    listTabou = []
    end = 1
    while end <= round(len(tab)/2):
        print(f"-----------------------------[Itération N°{end}]------------------------------------")
        print()
        listVoisins = voisinsNonTabou(tab,indexMinL, listTabou)
        print(f"Les voisins non tabou de {tab[indexMinL]} sont {printTab(listVoisins,tab)}")
        if len(listVoisins) == 0:
            print(f"La liste des voisins non tabou est vide.")
            break
        a = indexMinL
        indexMinL = indexMinVoisins(tab,listVoisins)
        print(f"Le minimum local des voisins non tabou de {tab[a]} est {tab[indexMinL]}")
        if tab[indexMinL] < tab[indexMinG]:
            indexMinG = indexMinL
        listTabou.append(indexMinL)
        print(f"On ajoute {tab[indexMinL]} dans la liste tabou. On obtient listTabou = {printTab(listTabou,tab)}")
        print()
        end += 1
    print("--------------------------------------------------------------------------------")
    print(f"Le minimum gloal est donc {tab[indexMinG]}")
        


# tab = [15, 18, 21, 17, 14, 23, 19, 12, 5, 7, 28, 30, 88, 27, 5, 31, 55, 16, 231]
tab = [random.randrange(1, 8000, 1) for i in range(100)]
rechercheTabou(tab)
print(len(tab))
print(min(tab))