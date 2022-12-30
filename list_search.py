def facteur(word, longWord):
    verif = False
    for j in range(len(longWord)):
        if word[0] == longWord[j]:
            verif = True
            a,b = 1,j+1
            while verif and a <= len(word) - 1 :
                if b > len(longWord)-1 or longWord[b] != word[a] :
                    verif = False    
                a+=1
                b+=1
    return(verif)

