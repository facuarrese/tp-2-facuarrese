def change():
    expense = 23.75
    money = 100
print("Ingresar gasto:")
expense =float(input())
print("Dinero recibido")
money=int(input())
vuelto=(money-expense)
print()
print("Vuelto")
print()
print("Pesos:")
print(int(vuelto))
print("Centavos:")
print(int((vuelto-(int(vuelto)))*100))
