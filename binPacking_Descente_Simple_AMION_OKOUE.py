from triFusionDesc import *
import random
import copy

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

def FFD(objList : list, binsCap : int)->list:
    objListOrdered = tri_fusion(objList)
    bins = []
    bins.append([[],0])
    for obj in objListOrdered:
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

def neighborhoodSBins(binsList : list, binsCap : int)->list:
    neighbors = []
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
                        neighbors.append(a)
                        removed = True
                        break
            if removed:
                pass
            else:
                j+=1         
    return neighbors

def minVoisin2(solution : list, neighborsList : list)->list:
    minBins = 99999
    index = None
    if len(neighborsList) == 0:
        return solution
    for bins in neighborsList:
        if len(bins) < minBins:
            minBins = len(bins)
            index = neighborsList.index(bins)
    if index is None:
        return None
    else:
        return neighborsList[index]
            

def simpleDesc (objList : list, binsCap : int)->list :
    solutionIni = FF(objList,binsCap)
    print(f"-------------------Solution initiale----------------------")
    for bag in solutionIni:
        print(bag)
    print(f"Nombre de sacs utilis?? = {len(solutionIni)}")
    print(f"----------------------------------------------------------")
    a = copy.deepcopy(solutionIni)
    neighbors = neighborhoodSBins(solutionIni, binsCap)
    minL = minVoisin2(solutionIni,neighbors)
    print(f"{solutionIni} et ----------------------------------------------{minL}")
    while len(solutionIni) != len(minL):
        solutionIni = copy.deepcopy(minL)
        neighbors = neighborhoodSBins(solutionIni, binsCap)
        minL = minVoisin2(solutionIni,neighbors)
    print(f"-------------------Solution finale----------------------")
    for bag in minL:
        print(bag)
    print(f"Nombre de sacs utilis?? = {len(minL)} contre {len(a)} initialement")
    print(f"----------------------------------------------------------")
    


objList = [100, 22, 25, 51, 95, 58, 97, 30, 79, 23, 53, 80, 20, 65, 64, 21, 26, 100 ,81 ,98, 70, 85, 92, 97, 86, 71, 91, 29, 63, 34, 67,
23, 33, 89, 94, 47, 100, 37, 40, 58, 73, 39, 49, 79, 54, 57, 98, 69, 67, 49, 38, 34, 96, 27, 92, 82, 69, 45, 69, 20, 75, 97, 51, 70,
29, 91, 98, 77, 48, 45, 43, 61, 36, 82, 89, 94, 26, 35, 58, 58, 57, 46, 44, 91, 49, 52, 65, 42, 33, 60, 37, 57, 91, 52, 95, 84, 72,
75, 89, 81, 67, 74, 87, 60, 32, 76, 85, 59, 62, 39, 64, 52, 88, 45, 29, 88, 85, 54, 40, 57]
binsCap = 150

simpleDesc(objList,binsCap)