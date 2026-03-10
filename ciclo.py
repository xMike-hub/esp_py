
# Appunti sui cicli in Python per principianti
# I cicli (loops) servono per ripetere delle istruzioni più volte.
# In Python ci sono due tipi principali: for e while.

# Esempio semplice di ciclo while (come quello che hai fatto tu):
# prima variabile
var = 10

# primo ciclo
while var < 20:
    print(var)
    var = var + 1

print("Fine del ciclo while")

# Il ciclo for è utile per ripetere su una lista o un range:
# Esempio con for:
print("Ciclo for con range:")
for i in range(5):  # Ripete 5 volte, i va da 0 a 4
    print("Numero:", i)

# Esempio con lista:
frutti = ["mela", "banana", "arancia"]
print("Ciclo for con lista:")
for frutto in frutti:
    print("Frutto:", frutto)

# Come si scrivono i cicli correttamente:
# - While: while condizione: (la condizione deve diventare falsa per fermarsi)
# - For: for variabile in sequenza:

# Esempi NON corretti (commentati per non dare errori):
# while True:  # Ciclo infinito, non si ferma mai!
#     print("Questo non finisce")

# for i in 10:  # Errore: 10 non è una sequenza
#     print(i)

# Per rendere interattivo: chiediamo quanti numeri stampare
quanti = int(input("Quanti numeri vuoi stampare? "))
for num in range(quanti):
    print("Numero", num + 1)    