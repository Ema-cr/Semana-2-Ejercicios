import random
numero_ran=random.randint(1,10)
i=3
while i > 0:
    numero=int(input("Adivina el numero: "))
    if numero == numero_ran:
        print ("Adivinaste el numero!")
        break
    elif numero > numero_ran:
        print("El numero es menor")
    elif numero < numero_ran:
        print("El numero es mayor")
        i=i-1
    if i==0:
        print(f"Te quedaste sin intentos el numero era {numero_ran}")
