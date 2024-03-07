def tabla(n):
    nombretabla = "tabla-{}.txt"
    try:
        archivo = open(nombretabla.format(n), "r")
        print(archivo.read())
    except FileNotFoundError:
        print("¡No existe esa tabla de multiplicar!")
    else:
        archivo.close()
pregunta = int(input("Dame un numero entero del 1 al 10: "))
tabla(pregunta)