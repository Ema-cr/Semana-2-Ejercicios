# Solicitar una calificacion
# ingresar una lista de calificaciones y otro valor para comparar
# mostrar si aprueba if elif else mostrar mensajes aprueba etc
# un ciclo para recorrer las calificaciones y calcular promedio
# un ciclo para contar calificaciones mayores al valor solicitado
# evalua si una calificacion esta presente en la lista y cuenta cuantas veces aparece


calificacion_soli=int(input("Ingresa tu calificacion entre 0 y 100: ")) #Solicitar una calificacion numerica
if calificacion_soli >= 60:  #Evaluar si esta aprobada o reprobada
    print("Aprobaste")
else: print ("Reprobaste")

califs= input("Ingresa tus calificaciones separadas por ','") #Pedir una lista de calificaciones
valores= califs.split(",")         #Separar la cadena en elementos individuales
numeros=[int(valor) for valor in valores]    #Convertimos cada valor a numeros int
print("Lista de numeros: ", numeros)

# 1. hacer un ciclo para recorrer la lista (iterador y range (creo))
# 2. Un ciclo for o while para contar cuantas calificaciones fueron mas altas que el numero
# 3. Evalúa si una calificación específica está presente en la lista cuenta cuántas veces aparece, utilizando break y otras estructuras para controlar el flujo.
# 
