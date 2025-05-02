while True:      #Bucle
    try:
        califs=input("Ingresa tus calificaciones separadas por ','") #Pedir una lista de calificaciones
        valores= califs.split(",")         #Separar la cadena en elementos individuales
        numeros=[]    #Lista vacia para todas las calificaciones
        
        #Recorre cada valor en la lista
        for valor in valores:
            numeros.append(float(valor))   #Convierte cada valor en float
        for calificacion in numeros:       #Recorre las calificaciones para compararlas
            if 60 <= calificacion <= 69:
                print(f"Aprobaste con {calificacion}, sacaste una C, ¡sigue mejorando!")
            elif 70 <= calificacion <= 89:
                print(f"Aprobaste con {calificacion}, sacaste una B, ¡Muy bien!")
            elif 90 <= calificacion <= 100:
                print(f"Aprobaste con {calificacion}, sacaste una A, ¡Excelente!")
            else:
                print(f"Reprobaste con {calificacion}, ¡sigue mejorando!")  
    except ValueError:                    #Si ingresa un valor no valido imprime error
        print("Ingresa un valor numerico")
        
    if len(numeros)>0:     #Mira si hay alguna calificacion valida en la lista
        promedio = sum(numeros)/len (numeros)  #Se calcula el promedio sumando todas y dividiendo por la cantidad
        print (f"Tu promedio es : {promedio:.2f}")  #Se imprime el promedio con solo 2 decimales (el 2.f sirve para que solo sean 2 decimales ejemplo: 2.99999999 con 2.f seria 2.99)
        #Se evalua si aprobo o reprobo en base al promedio
        if promedio >= 60:
            print(f"Aprobaste con un {promedio:.2f} Felicidades!")
        else:
            print(f"Reprobaste con un {promedio:.2f}. Sigue esforzandote!")
        
        #Contador para ver cuantas calificaciones son mas altas que el valor dado
        contador=0
        valor_especif=float(input("Ingresa un valor para medir cuantas calificiones son mayores: "))
        for calificacion in numeros: 
            if valor_especif < calificacion:
                contador+=1        
        print (f"Hay {contador} numeros mayores ")
        #Contador para ver cuantas calificaciones son iguales al valor ingresado
        contador_1=0
        calificacion_especif=float(input("Ingresa un valor para ver cuantas veces aparece en las calificaciones: "))
        for calificacion_1 in numeros:
            if calificacion_especif == calificacion_1:
                contador_1+=1
        print (f"Hay {contador_1} numeros iguales a {calificacion_especif} ")
    # Break para terminar el bucle
    break
