# Ejercicio 1
print("----------------------------------")
print("-----NUMERO PAR E IMPAR---------- ")
print("----------------------------------")

N=int(input("Digite un numero: "))

Numero_par=0
Numero_impar=0
while N!=0:
  
  for i in range(1):
    
    if N%2==0:
        print("El numero es par")
        Numero_par=Numero_par+1 
    else:
        print("El numero es impar")
        Numero_impar=Numero_impar+1
    N=int(input("Ingresa un numero: "))
print("Los numero pares son: "+str(Numero_par))
print("Los numeros impares son: "+ str(Numero_impar))   
