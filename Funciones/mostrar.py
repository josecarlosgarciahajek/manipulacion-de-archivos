def main(n):
    nombretabla = "Tablas/tabla-{}.txt"
    try:
        archivo = open(nombretabla.format(n), "r")
        print(archivo.read())
    except FileNotFoundError:
        print("¡No existe esa tabla de multiplicar!")
    else:
        archivo.close()
if __name__ == "__main__":
    main()