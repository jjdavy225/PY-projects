import random
import copy
import math

def FF(objList : list, binsCap : int)->list:
    objListShuffled = copy.deepcopy(objList)
    random.shuffle(objListShuffled)
    bins = []
    bins.append([[],0])
    for obj in objListShuffled:
        newBinEnable = True
        for bin in bins:
            if obj+bin[1] <= binsCap:
                bin[0].append(obj)
                bin[1] += obj
                newBinEnable = False
                break
        if newBinEnable:
            bins.append([[obj],obj])       
    return bins

def listVoisins(binsList : list, binsCap : int)->list:
    voisins = []
    bins = copy.deepcopy(binsList)
    for bin in bins:
        j = 0
        while j <= len(bin[0])-1:
            removed = False
            obj = bin[0][j]
            for i in range(len(bins)):
                if i == bins.index(bin):
                    pass
                else:
                    if(obj+bins[i][1]<= binsCap and bins[i][1]>0):
                        bin[0].remove(obj)
                        bin[1] -= obj
                        bins[i][0].append(obj)
                        bins[i][1] += obj
                        a = copy.deepcopy(bins)
                        for element in a:
                            if(element[1]==0):
                                a.remove(element)
                        voisins.append(a)
                        removed = True
                        break
            if removed:
                pass
            else:
                j+=1         
    return voisins

def minVoisin2(solution : list, listVoisins : list)->list:
    minBins = 99999
    index = None
    if len(listVoisins) == 0:
        return solution
    for bins in listVoisins:
        if len(bins) < minBins:
            minBins = len(bins)
            index = listVoisins.index(bins)
    if index is None:
        return None
    else:
        return listVoisins[index]
    
def recuitSimule(objList : list, binsCap : int)->list:
    solutionIni = FF(objList,binsCap)
    minG = copy.deepcopy(solutionIni)
    minL = copy.deepcopy(solutionIni)
    print(f"-------------------Solution initiale----------------------")
    for bag in solutionIni:
        print(bag)
    print(f"Nombre de sacs utilisé = {len(solutionIni)}")
    print(f"----------------------------------------------------------")
    temp = len(solutionIni)
    i = 0
    while i <= 4*len(objList):
        voisins = listVoisins(minL, binsCap)
        if len(voisins) == 0 :
            break
        solutionS = random.choice(voisins)
        r = random.uniform(0,1)
        p = math.exp((len(minL)-len(solutionS))/temp)
        if(r < p) :
            minL = copy.deepcopy(solutionS)
            temp = len(minL)
        if len(minL) < len(minG):
            minG = copy.deepcopy(minL)
        i+=1
    print(f"-------------------Solution finale----------------------")
    for bag in minG:
        print(bag)
    print(f"Nombre de sacs utilisé = {len(minG)} contre {len(solutionIni)} initialement")
    print(f"----------------------------------------------------------")


objList = [100, 22, 25, 51, 95, 58, 97, 30, 79, 23, 53, 80, 20, 65, 64, 21, 26, 100 ,81 ,98, 70, 85, 92, 97, 86, 71, 91, 29, 63, 34, 67,
23, 33, 89, 94, 47, 100, 37, 40, 58, 73, 39, 49, 79, 54, 57, 98, 69, 67, 49, 38, 34, 96, 27, 92, 82, 69, 45, 69, 20, 75, 97, 51, 70,
29, 91, 98, 77, 48, 45, 43, 61, 36, 82, 89, 94, 26, 35, 58, 58, 57, 46, 44, 91, 49, 52, 65, 42, 33, 60, 37, 57, 91, 52, 95, 84, 72,
75, 89, 81, 67, 74, 87, 60, 32, 76, 85, 59, 62, 39, 64, 52, 88, 45, 29, 88, 85, 54, 40, 57]
binsCap = 150

recuitSimule(objList,binsCap)