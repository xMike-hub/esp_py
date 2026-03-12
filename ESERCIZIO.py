import math


print("Scegli una figura geometrica:")
print("1. Quadrato")
print("2. Cerchio")
print("3. Rettangolo")

scelta = int(input("Inserisci il numero della figura: "))

if scelta == 1:
    lato = int(input("Inserisci il lato del quadrato: "))
    perimetro = lato * 4
    print("Il perimetro del quadrato e': ", perimetro)

elif scelta == 2:
    raggio = int(input("Inserire il raggio: "))
    circonferenza = 2* math.pi * raggio
    print("La circonferza del cerchio e': ", circonferenza)

elif scelta == 3:
    base = int(input("Inserisci la base del rettangolo: "))
    altezza = int(input("Inserisci l'altezza del rettangolo: "))
    perimetro = (base*2) + (altezza*2) 
    print("Il perimetro del rettangolo e': ", perimetro)

else : 
    print("scelta non valida")     


                         
                         

