from Funciones import crear, lineas, mostrar, menu, numeros
while True:
    try:
        menu.main()
        opc = numeros.opcion_menu()
        if opc == 4:
            print("Adiós")
            break
        else:
            num = numeros.numero()
            if opc == 1:
                crear.main(num)
            elif opc == 2:
                mostrar.main(num)
            elif opc == 3:
                lineas.main(num)
            else:
                print("Error")
    except ValueError:
        print("DAME NÚMEROS")