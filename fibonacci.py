import time


def fibonacci_a(x):
	if x <= 0:
		val = 0
	elif x == 1 :
		val = 1
	else :
		val = fibonacci_a(x-1) + fibonacci_a(x-2)
	return val

def fibonacci_b(x):
    if x==1 or x==2:
        return 1
    else:
        a=1
        b=1
        for i in range(3,x+1):
            c = a+b
            b=a
            a=c
        return c
    

x = int(input("Entrer un rang : "))
print()
start = time.time()
# for i in range(x+1) :
# 	if i == 0:
# 		pass
# 	else:
# 		print(f' fibo {i} est {fibonacci_b(i)}')
# 		# print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f' fibo {x} est {fibonacci_b(x)}')
end = time.time()

elapsed = end - start
print(f"Temps d'exécution : {elapsed:.2} ms")
  