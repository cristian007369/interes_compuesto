#Programa para calcular los meses que tarda un capital en duplicarse con una tasa de interés n
#Input

capital=float(input("Dígite el valor del capital: "))
interes=float(input("Dígite la tasa de interés, en decimales: "))
meses=0
d=capital*2
#Procesing

while capital<=d:
    meses=meses+1
    intt=capital*interes
    capital=capital + intt
    print("mes: "+str(meses) + " Capital: " +str(capital)  )


