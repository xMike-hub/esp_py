# Appunti su input e output in Python per principianti
# Input: dati che l'UTENTE inserisce (da tastiera)
# Output: dati che il programma MOSTRA (sullo schermo)

# Output con print() - Mostra dati sullo schermo:
print("=== OUTPUT CON PRINT() ===")
print("Ciao! Questo è un messaggio di output.")
print("Il programma lo mostra su schermo per te.")

# Puoi stampare stringhe:
print("Benvenuto in Python!")

# Puoi stampare numeri:
print(42)
print(3.14)

# Puoi stampare risultati di operazioni:
print(10 + 5)
print("2 più 2 = ", 2 + 2)

# Input con input() - L'utente inserisce dati:
print("\n=== INPUT CON INPUT() ===")
print("Digitare il tuo nome quando richiesto...")

# input() aspetta che l'utente scriva qualcosa e lo salva in una variabile
nome = input("Qual è il tuo nome? ")

# Ora mostriamo con print() quello che l'utente ha inserito (output):
print("Hai inserito:", nome)

# input() restituisce sempre una stringa (testo)
# Se vuoi un numero, devi convertirlo:
print("\n=== CONVERTIRE INPUT A NUMERO ===")
anno_nascita = int(input("In che anno sei nato? "))
anno_corrente = 2023

# Ora possiamo fare calcoli con il numero:
eta = anno_corrente - anno_nascita
print("Hai circa", eta, "anni!")  # Questo è output

# Esempio completo: Interazione input -> elaborazione -> output
print("\n=== ESEMPIO COMPLETO ===")
colore_preferito = input("Quale è il tuo colore preferito? ")
animale_preferito = input("Quale è il tuo animale preferito? ")

# Elaboriamo i dati e creiamo output personalizzato:
frase = "Mi piace il colore " + colore_preferito + " e l'animale " + animale_preferito
print(frase)

# Esempi NON corretti (commentati per non dare errori):
# numero = input("Inserisci un numero")
# risultato = numero + 10  # Errore: numero è una stringa, non puoi sommarla a 10
# numero = int(input("Inserisci un numero"))
# risultato = numero + 10  # Giusto! Ora funziona

# print senza argomenti stampa una riga vuota:
print()
print("Riga precedente era vuota!")

# Riassunto:
print("\n=== RIASSUNTO ===")
print("print() → OUTPUT (mostra sullo schermo)")
print("input() → INPUT (prende dati da tastiera)")
print("input() restituisce sempre una STRINGA")
print("Usa int() o float() per convertire a numero")

# Finale interattivo:
print("\n=== GIOCO: INDOVINA IL NUMERO ===")
numero_segreto = 7
numero_utente = int(input("Indovina il numero: "))
if numero_utente == numero_segreto:
    print("Esatto! Hai vinto!")
else:
    print("Sbagliato! Il numero era:", numero_segreto)