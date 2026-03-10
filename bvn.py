# File di benvenuto: Introduzione al comando print in Python
# Il comando print serve per mostrare messaggi o valori sullo schermo.
# È uno dei primi comandi che impari in Python!

# Esempio semplice:
print("hello-world")  # Questo è il tuo print originale

# Altri esempi di print:
print("Benvenuto in Python!")  # Stringa semplice
print(42)  # Numero
print("Il mio nome è", "Mario")  # Più valori separati da virgola
print("2 + 2 =", 2 + 2)  # Calcolo e testo

# Come si usa print correttamente:
# - print(valore) per stampare un valore
# - print("testo") per stampare testo
# - Puoi combinare testo e variabili

nome = "Utente"
print("Ciao", nome, "!")

# Esempi NON corretti (commentati per non dare errori):
# print hello  # Errore: manca parentesi
# print("testo"  # Errore: manca parentesi chiusa

# Per rendere interattivo: chiediamo il nome e salutiamo
nome_utente = input("Come ti chiami? ")
print("Benvenuto,", nome_utente, "! Questo è il tuo primo programma Python.")