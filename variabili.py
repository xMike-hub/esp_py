# Spiegazione delle variabili in Python per principianti
# Le variabili sono come scatole dove mettiamo i nostri dati.
# In Python, creiamo una variabile assegnandole un nome e un valore.

# Esempi di variabili corrette:
nome = "Mario"  # Stringa
eta = 25        # Numero intero
altezza = 1.75  # Numero decimale (float)
is_studente = True  # Booleano

print("Nome:", nome)
print("Età:", eta)
print("Altezza:", altezza)
print("È studente?", is_studente)

# Come si scrivono i nomi delle variabili:
# - Devono iniziare con una lettera o un underscore (_)
# - Possono contenere lettere, numeri e underscore
# - Non possono iniziare con un numero
# - Sono case-sensitive (maiuscole e minuscole sono diverse)

# Esempi corretti:
mia_variabile = 10
_variabile = 20
Variabile123 = 30

# Esempi NON corretti (commentati per non dare errori):
# 123variabile = 40  # Errore: inizia con numero
# mia-variabile = 50  # Errore: trattino non permesso
# mia variabile = 60  # Errore: spazio non permesso

# Per prendere input dall'utente:
nome_utente = input("Inserisci il tuo nome: ")
eta_utente = int(input("Inserisci la tua età: "))

print("Ciao", nome_utente, "hai", eta_utente, "anni!")