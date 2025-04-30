while True:
    try:
        califs= input("Ingresa tus calificaciones separadas por ','") #Pedir una lista de calificaciones
        valores= califs.split(",")         #Separar la cadena en elementos individuales
        numeros=[]    #Lista vacia para todas las calificaciones
        
        #Convertir cada valor en un float
        for valor in valores:
            numeros.append(float(valor))
        for calificacion in numeros:
            if 60 <= calificacion <= 69:
                print(f"Aprobaste con {calificacion}, sacaste una C, ¡sigue mejorando!")
            elif 70 <= calificacion <= 89:
                print(f"Aprobaste con {calificacion}, sacaste una B, ¡Muy bien!")
            elif 90 <= calificacion <= 100:
                print(f"Aprobaste con {calificacion}, sacaste una A, ¡Excelente!")
            else:
                print(f"Reprobaste con {calificacion}, ¡sigue mejorando!")
    except ValueError:
        print("Ingresa un valor numerico")
    if len(numeros)>0:
        promedio= sum(numeros)/len (numeros)
        print (f"Tu promedio es : {promedio:.2f}")

        if promedio >= 60:
            print(f"Aprobaste con un {promedio:.2f} Felicidades!")
        else:
            print(f"Reprobaste con un {promedio:.2f}. Sigue esforzandote!")
