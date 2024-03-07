def main(n):
    nombretabla = "Tablas/tabla-{}.txt"
    archivo = open(nombretabla.format(n), "w")
    for i in range(0,10+1):
        n=n
        i=i
        multi = i*n
        frase = "{} x {} = {} \n"
        archivo.write(frase.format(n,i,multi))
    archivo.close()
    print("Tabla creada!!")
if __name__ == "__main__":
    main()