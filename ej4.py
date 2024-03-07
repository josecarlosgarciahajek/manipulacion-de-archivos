from Funciones import crear, lineas, mostrar
print("----------Menu-----------")
print("-------------------------")
print("1. Crear una tabla.")
print("2. Ver tabla.")
print("3. Ver fila de una tabla.")
print("4. Salir")
print("-------------------------")
try:
    opc = int(input("Dame un numero entero del 1 al 4: "))
    num= int(input("Dame un numero entero del 1 al 10: "))
    if opc == 1:
        crear.main(num)
    elif opc == 2:
        mostrar.main(num)
    elif opc == 3:
        lineas.main(num)
    elif opc == 4:
        exit
    else:
        print("Error")
except ValueError:
    print("DAME NÚMEROS")