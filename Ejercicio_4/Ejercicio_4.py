# calcular el factorial de un numero
print("------------------------------------")
print("----------FACTORIAL--------------")
print("------------------------------------")

n=int(input("Ingresa el numero para calcular su factorial: "))

fact=1

for i in range(1,n+1):
    fact=fact*i
print("El factorial del numero:"+str(fact))