#Determinar si un número dado es primo
#Eduardo Caleb Castillo Llanas
#Daniel Maldonado Delgado
#Larisa Carolina Alvarez Gonzales
#Ximena Castro Flores
#10/Octubre/25
#entrdas
numero = int(input("Dame un numero: "))
primo = False
#desarrollo
for n in range(2,numero):
  if numero % n == 0:
    print("el numero",numero, "no es primo")#Salida
    break
else:
  primo =True
  print("el numero",numero, "sí es primo")#Salida
