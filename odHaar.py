# matrix = [[0, 250, 25, 50, 200, 0, 0, 0],
#           [50, 50, 50, 25, 50, 0, 25, 0],
#           [25, 50, 0, 250, 0, 50, 0, 0],
#           [75, 200, 200, 0, 250, 250, 0, 200],
#           [250, 25, 250, 200, 0, 75, 25, 25],
#           [50, 0, 50, 0, 0, 75, 250, 250],
#           [250, 250, 25, 25, 50, 25, 50, 50],
#           [250, 200, 50, 50, 50, 25, 0, 200]]

matrix = [[[152, 250, 255], [20, 14, 13], [18, 250, 63],[120,40,90]],
          [[25,60,55],[36,19,45],[79,226,224],[230,199,189]],
          [[25, 253, 65], [255, 255, 255], [210, 23, 100],[5,124,166]],
          [[110, 92, 36], [20, 28, 69], [255, 26, 150],[200,215,250]]
          ]
# result = []
# for i in range(len(matrix)):
#     tab1 = []
#     result.append(tab1)
#     for j in range(0, len(matrix[i])-1, 2):
#         tab1.append([round((matrix[i][j]+matrix[i][j+1])/2)])
# print(result)


def listAddition(m1: list, m2: list) -> list:
    if len(m1) != len(m2) or len(m1) == 0:
        return None
    else:
        result = []
        for i in range(len(m1)):
            val = m1[i]+m2[i]
            if val % 2 == 0:
                result.append(int(val/2))
            else:
                val = int(round(val/2))
                result.append(val)
        return result


def listSubstraction(m1: list, m2: list) -> list:
    if len(m1) != len(m2) or len(m1) == 0:
        return None
    else:
        result = []
        for i in range(len(m1)):
            val = m1[i]-m2[i]
            if val % 2 == 0:
                result.append(int(val/2))
            else:
                val = int(round(val/2))
                result.append(val)
        return result


def TO_Haar(matrix):
    matrix1 = []
    matrix2 = []

    for i in range(len(matrix)):
        tab1 = []
        tab2 = []
        matrix1.append(tab1)
        matrix2.append(tab2)
        for j in range(0, len(matrix[i])-1, 2):
            tab1.append(listAddition(matrix[i][j], matrix[i][j+1]))
            tab2.append(listSubstraction(matrix[i][j], matrix[i][j+1]))

    approximation = []
    detail1 = []
    detail2 = []
    detail3 = []
    print(f"En additionnant les colonnes deux à deux")
    print(f"---------------------Mat1---------------------")
    print(matrix1)
    print(f"---------------------Mat2---------------------")
    print(matrix2)
    
    for i in range(0,len(matrix1)-1,2):
        tab1 = []
        tab2 = []
        approximation.append(tab1)
        detail1.append(tab2)
        for j in range(len(matrix1[i])):
            tab1.append(listAddition(matrix1[i][j], matrix1[i+1][j]))
            tab2.append(listSubstraction(matrix1[i][j], matrix1[i+1][j]))

    for i in range(0,len(matrix2)-1,2):
        tab1 = []
        tab2 = []
        detail2.append(tab1)
        detail3.append(tab2)
        for j in range(len(matrix2[i])):
            tab1.append(listAddition(matrix2[i][j], matrix2[i+1][j]))
            tab2.append(listSubstraction(matrix2[i][j], matrix2[i+1][j]))
    
    print(f"En additionnant les lignes deux à deux")
    print(f"---------------------Approximation---------------------")
    print(approximation)
    print(f"---------------------Detail1---------------------")
    print(detail1)
    print(f"---------------------Detail2---------------------")
    print(detail2)
    print(f"---------------------Detail3---------------------")
    print(detail3)
        
    return [approximation,detail1,detail2,detail3]


tab = TO_Haar(matrix)

# for element in tab:
#     print(element)

