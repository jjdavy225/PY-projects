import random
import copy

def FF(listDesObjets : list, capaciteDesSacs : int)->list:
    listMelangee = copy.deepcopy(listDesObjets)
    random.shuffle(listMelangee)
    sacs = []
    sacs.append([[],0])
    for obj in listMelangee:
        nouveauSac = True
        for sac in sacs:
            if obj+sac[1] <= capaciteDesSacs:
                sac[0].append(obj)
                sac[1] += obj
                nouveauSac = False
                break
        if nouveauSac:
            sacs.append([[obj],obj])       
    return sacs

def voisinage(listDesSacs : list, capaciteDesSacs : int)->list:
    voisins = []
    sacs = copy.deepcopy(listDesSacs)
    for sac in sacs:
        j = 0
        while j <= len(sac[0])-1:
            removed = False
            obj = sac[0][j]
            for i in range(len(sacs)):
                if i == sacs.index(sac):
                    pass
                else:
                    if(obj+sacs[i][1]<= capaciteDesSacs and sacs[i][1]>0):
                        sac[0].remove(obj)
                        
                        sac[1] -= obj
                        sacs[i][0].append(obj)
                        sacs[i][1] += obj
                        a = copy.deepcopy(sacs)
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

def minVoisin(solution : list, listVoisins : list, tabou : list)->list:
    minBins = 99999
    index = None
    if len(listVoisins) == 0 and solution not in tabou:
        return solution
    for sacs in listVoisins:
        if len(sacs) <= minBins and sacs not in tabou:
            minBins = len(sacs)
            index = listVoisins.index(sacs)
    if index is None:
        return None
    else:
        return listVoisins[index]
            

def tabouSearch(listDesObjets : list, capaciteDesSacs : int)->list :
    solutionIni = FF(listDesObjets, capaciteDesSacs)
    minL = copy.deepcopy(solutionIni)
    print(f"-------------------Solution initiale----------------------")
    for bag in minL:
        print(bag)
    print(f"Nombre de sacs utilisé = {len(minL)}")
    print(f"----------------------------------------------------------")
    listTabou = []
    minG = copy.deepcopy(solutionIni)
    i = 0
    while i <= 2*len(solutionIni):
        voisins = voisinage(minL,capaciteDesSacs)
        minL = minVoisin(minL,voisins,listTabou)
        if(minL is None):
            break
        listTabou.append(minL)
        if(len(minL) < len(minG)):
            minG = copy.deepcopy(minL)
        i+=1
    print(f"-------------------Solution finale----------------------")
    for bag in minG:
        print(bag)
    print(f"Nombre de sacs utilisé = {len(minG)} contre {len(solutionIni)} initialement")
    print(f"----------------------------------------------------------")
        
    


listDesObjets = [100, 22, 25, 51, 95, 58, 97, 30, 79, 23, 53, 80, 20, 65, 64, 21, 26, 100 ,81 ,98, 70, 85, 92, 97, 86, 71, 91, 29, 63, 34, 67,
23, 33, 89, 94, 47, 100, 37, 40, 58, 73, 39, 49, 79, 54, 57, 98, 69, 67, 49, 38, 34, 96, 27, 92, 82, 69, 45, 69, 20, 75, 97, 51, 70,
29, 91, 98, 77, 48, 45, 43, 61, 36, 82, 89, 94, 26, 35, 58, 58, 57, 46, 44, 91, 49, 52, 65, 42, 33, 60, 37, 57, 91, 52, 95, 84, 72,
75, 89, 81, 67, 74, 87, 60, 32, 76, 85, 59, 62, 39, 64, 52, 88, 45, 29, 88, 85, 54, 40, 57]

capaciteDesSacs = 150

tabouSearch(listDesObjets,capaciteDesSacs)