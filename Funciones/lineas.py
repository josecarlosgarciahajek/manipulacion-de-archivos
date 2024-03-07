def main(n):
    try:
        nombretabla = "Tablas/tabla-{}.txt" 
        archivo = open(nombretabla.format(n), "r")
        l = int(input("Dame un numero entero de linea del 0 al 10: "))
        # sacar línea del archivo, poner corchete. TRATAR COMO LISTA
        print(archivo.readlines()[l])
    except FileNotFoundError:
        print("¡No existe esa tabla de multiplicar!")
    else:
        archivo.close()
    
if __name__ == "__main__":
    main()