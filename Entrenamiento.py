while True:
    try:
        califs=input("Ingresa tus calificaciones separadas por ','") #Pedir una lista de calificaciones
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
        

        contador=0
        valor_especif=float(input("Ingresa un valor para medir cuantas calificiones son mayores: "))
        for calificacion in numeros: 
            if valor_especif < calificacion:
                contador+=1        
        print (f"Hay {contador} numeros mayores ")

        contador_1=0
        calificacion_especif=float(input("Ingresa un valor para ver cuantas veces aparece en las calificaciones: "))
        for calificacion_1 in numeros:
            if calificacion_especif == calificacion_1:
                contador_1+=1
        print (f"Hay {contador_1} numeros iguales a {calificacion_especif} ")



    break