#Programa para calcular el capital en n meses con una tasa de interes N
#Input

capital=float(input("Dígite el valor del capital: "))
interes=float(input("Dígite la tasa de interés, en decimales: "))
meses=int(input("¿Cuantos meses lo quieres calcular?: "))
cont=0

#Procesing

while cont!=meses:
    cont=cont+1
    intt=capital*interes
    capital=round(capital + intt,3)

#Output

print(capital)