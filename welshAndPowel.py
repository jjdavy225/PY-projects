def colorGraph(matrix : list)-> dict:
    sommets = list(range(len(matrix)))
    sommetsRanges = sorted(sommets,key = lambda x: sum(matrix[x]), reverse=True)
    colors = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # print(sommetsRanges)
    colored = {}
    color = 0
    for sommet in sommetsRanges:
        if sommet not in colored:
            colored[sommet] = colors[color]
            for element in sommetsRanges:
                if (sommet != element) and (matrix[sommet][element] == 0) and (element not in colored):
                    colored[element] = colors[color]
            color += 1
    return colored
            
    
matrix = [
    [0,1,0,0,0,1,1],
    [1,0,1,0,0,0,1],
    [0,1,0,0,0,0,1],
    [0,0,0,0,1,0,0],
    [0,0,0,1,0,1,1],
    [1,0,0,0,1,0,1],
    [1,1,1,0,1,1,0]
]

print(colorGraph(matrix=matrix))