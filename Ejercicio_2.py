while True:
    try:
        nota=float (input("Ingresa tu calificacion: "))  
        if nota >= 0 and nota < 60:
            print("Reprobaste")
            break
        elif nota >= 60 and nota < 100:
            print ("Aprobaste")
            break
        else:
            print ("Ingresa Una nota entre el rango 0-100")
    except ValueError:
        print("Ingresaste un valor no valido")
