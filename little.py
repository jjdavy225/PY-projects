import copy

matrix = [['.',780,320,580,480,660],
          [780,'.',700,460,300,200],
          [320,700,'.',380,820,630],
          [580,460,380,'.',750,310],
          [480,300,820,750,'.',500],
          [660,200,630,310,500,'.']
        ]

def sumMin(matrix:list):
    mat = copy.deepcopy(matrix)
    print('--------------Sum min de la mat suivante----------------')
    for line in mat:
        print(line)
    sumM = 0
    for i in range(len(mat)):
        line = mat[i]
        minimum = 99999999
        found = False
        for j in range(len(mat[i])):
            element = mat[i][j]
            if not isinstance(element,int) :
                pass
            else:
                if element<minimum:
                    minimum = element
                    found = True
        if found:
            sumM += minimum
        for j in range(len(line)):
            if not isinstance(mat[i][j], int): pass
            else: mat[i][j] -= minimum
    for i in range(len(mat)):
        minimum = 999999999
        found = False
        for j in range(len(mat)):
            elementCol = mat[j][i]
            if not isinstance(elementCol, int) :
                pass
            else:
                if elementCol<minimum:
                    minimum = elementCol
                    found = True
        if minimum == 0:
            pass
        else:
            if found : sumM += minimum
            for j in range(len(mat)):
                if not isinstance(mat[j][i], int): pass
                else:
                    mat[j][i] -= minimum
    print('-----------------New nat-----------------------')
    print(sumM)
    for line in mat:
        print(line)
    return sumM,mat

def regret(matrix:list, townListIndex):
    mat = copy.deepcopy(matrix)
    regretList = []
    print('---------------Calcul regret de la mat suivante---------------')
    for line in mat:
        print(line)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0 : pass
            else:
                line = mat[i].copy()
                line.remove(mat[i][j])
                line = [x for x in line if x != '.']
                minLine = min(line)
                col = [mat[a][j] for a in range(len(matrix))]
                col.remove(mat[i][j])
                col = [x for x in col if x!='.']
                minCol = min(col)
                depart = townListIndex[0][i]
                arrivee = townListIndex[1][j]
                print(f"{depart}{arrivee}")
                regretList.append([depart,arrivee,minLine+minCol])
    max = 0
    for element in regretList:
        if element[2] > max:
            regretMax = element
            max = regretMax[2]
    mat[regretMax[1]][regretMax[0]] = '.'
    col = regretMax[1]
    line = regretMax[0]
    for i in range(len(mat[line])):
        mat[line][i] = '.'
    for i in range(len(mat)):
        mat[i][col] = '.'
    print('-----------mat réduite--------------')
    for line in mat:
        print(line)
            
    return regretMax,mat
    
def little(matrix : list,townListIndex, val = 0):
    sumM,newMat = sumMin(matrix)
    regretMax,newMat,townListIndex = regret(newMat,townListIndex)
    print(val)
    racine = sumM+val
    if regretMax[2] != 0:
        gauche = [regretMax[0],regretMax[1],racine+regretMax[2],False]    
        tree = [gauche,racine,[regretMax[0],regretMax[1],little(newMat,townListIndex,racine),True]]
    else:
        pass
    
    print(tree)
    
    # return newMat,tree,val

# def recurLittle(matrix:list)->list:
#     tree = []
#     recurLittle(matrix, tree,0)

townName = ['B','L','N','P','M','D']
townListIndex = [{},{}]
for index in range(len(matrix)):
    townListIndex[0][index] = townName[index]
    townListIndex[1][index] = townName[index]
    
print(townListIndex)
         
little(matrix,townListIndex)

