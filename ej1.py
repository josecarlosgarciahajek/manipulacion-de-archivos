def tabla(n):
    nombretabla = "tabla-{}.txt"
    archivo = open(nombretabla.format(n), "w")
    for i in range(0,10+1):
        n=n
        i=i
        multi = i*n
        frase = "{} x {} = {} \n"
        archivo.write(frase.format(n,i,multi))
    archivo.close()
pregunta = int(input("Dame un numero entero del 1 al 10: "))
tabla(pregunta)