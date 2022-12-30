x = int(input("Entrer une valeur : "))
def McCarthy(x):
    if x > 100:
        print(x-10)
        return x-10
    else:
        print(f"McCarthy(McCarthy({x+11}))")
        return McCarthy(McCarthy(x+11))
    
print(McCarthy(x))