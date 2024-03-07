def tabla1(n):
    nombretabla = "TABLAS/tabla-{}.txt"
    archivo = open(nombretabla.format(n), "w")
    for i in range(0,10+1):
        n=n
        i=i
        multi = i*n
        frase = "{} x {} = {} \n"
        archivo.write(frase.format(n,i,multi))
    archivo.close()
def tabla2(n):
    nombretabla = "TABLAS/tabla-{}.txt"
    try:
        archivo = open(nombretabla.format(n), "r")
        print(archivo.read())
    except FileNotFoundError:
        print("¡No existe esa tabla de multiplicar!")
    else:
        archivo.close()
def tabla3(n):
    try:
        nombretabla = "TABLAS/tabla-{}.txt" 
        archivo = open(nombretabla.format(n), "r")
        l = int(input("Dame un numero entero de linea del 0 al 10: "))
        # sacar línea del archivo, poner corchete. TRATAR COMO LISTA
        print(archivo.readlines()[l])
    except FileNotFoundError:
        print("¡No existe esa tabla de multiplicar!")
    else:
        archivo.close()
def main():
    print("----------Menu-----------")
    print("-------------------------")
    print("1. Crear una tabla.")
    print("2. Ver tabla.")
    print("3. Ver fila de una tabla.")
    print("4. Salir")
    print("-------------------------")
    try:
        opc = int(input("Dame un numero entero del 1 al 4: "))
        if opc == 1:
            num= int(input("Dame un numero entero del 1 al 10: "))
            tabla1(num)
        elif opc == 2:
            num= int(input("Dame un numero entero del 1 al 10: "))
            tabla2(num)
        elif opc == 3:
            num= int(input("Dame un numero entero del 1 al 10: "))
            tabla3(num)
        elif opc == 4:
            exit
        else:
            print("Error")
    except ValueError:
        print("DAME NÚMEROS")
if __name__== __name__:
    main()