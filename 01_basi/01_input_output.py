# Appunti su INPUT e OUTPUT (print e input) per principianti
# Questi comandi sono la base per far comunicare il programma con l'utente.
# - print: serve per far "parlare" il programma (Output)
# - input: serve per far "ascoltare" il programma (Input)

# ============================================================
# PARTE 1: IL COMANDO PRINT (Far parlare il programma)
# ============================================================

print("=== ESEMPIO 1: PRINT SEMPLICE ===")
print("hello-world")  

print("
=== ESEMPIO 2: STAMPARE DATI DIVERSI ===")
print("Benvenuto in Python!")  # Stampa una stringa (testo: servono le virgolette)
print(42)                      # Stampa un numero (NON servono le virgolette)

print("
=== ESEMPIO 3: COMBINARE PIÙ ELEMENTI ===")
# Puoi separare più cose con una virgola. Python aggiungerà uno spazio in automatico!
print("Il mio nome è", "Mario")
print("2 + 2 =", 2 + 2)        # Fa il calcolo matematico prima di stamparlo

# ============================================================
# PARTE 2: USARE LE VARIABILI CON IL PRINT
# ============================================================

print("
=== STAMPARE LE VARIABILI ===")
# Invece di stampare testo fisso, stampiamo il contenuto di una "scatola" (variabile)
nome = "Utente"
print("Ciao", nome, "!")

# ============================================================
# PARTE 3: IL COMANDO INPUT (Ascoltare l'utente)
# ============================================================

print("
=== RICEVERE DATI DALL'UTENTE ===")
# input() mette in PAUSA il programma. 
# Aspetta che tu scriva qualcosa sulla tastiera e prema Invio.
# Quello che scrivi viene salvato nella variabile a sinistra dell'uguale.

nome_utente = input("Come ti chiami? ")

# Ora usiamo il dato che l'utente ha appena inserito:
print("Benvenuto", nome_utente, "! Questo è il tuo primo programma interattivo.")

print("
=== CONVERTIRE L'INPUT A NUMERO ===")
# ATTENZIONE: input() restituisce sempre una stringa (testo), non un numero!
# Se voglio usare il numero per fare calcoli, devo convertirlo con int()
numero_testo = input("Scrivi un numero: ")
print("Hai scritto:", numero_testo, "e il tipo è", type(numero_testo))

numero_vero = int(input("Scrivi un altro numero (verrà convertito in intero): "))
print("Hai scritto:", numero_vero, "e il tipo è", type(numero_vero))
print("Numero + 10 =", numero_vero + 10)

# ============================================================
# ESEMPI PIÙ COMPLESSI (Dal file saluto.py)
# ============================================================

print("
=== ESEMPIO COMPLETO: CALCOLO ETÀ ===")
# Raccogliamo due input: anno di nascita e anno corrente
anno_nascita = int(input("In che anno sei nato? "))
anno_corrente = 2026
# Calcoliamo l'età
eta = anno_corrente - anno_nascita
# Mostriamo il risultato
print("Nel", anno_corrente, "hai circa", eta, "anni!")

print("
=== ESEMPIO: CONCATENAZIONE ===")
# Possiamo unire stringhe da input con output personalizzato
colore = input("Quale è il tuo colore preferito? ")
animale = input("Quale è il tuo animale preferito? ")
# Creiamo una frase personalizzata
frase = "Ti piace il colore " + colore + " e l'animale " + animale
print(frase)

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

print("
=== ERRORI COMUNI ===
")
print("Errore 1: Dimenticare le parentesi (genera un SyntaxError)")
print("SBAGLIATO: print hello")
print("GIUSTO: print('hello')")

print("
Errore 2: Dimenticare di chiudere le virgolette o le parentesi")
print("SBAGLIATO: print('testo) oppure print('testo'")
print("GIUSTO: print('testo')")

print("
Errore 3: Usare input() senza salvare il risultato")
print("SBAGLIATO: input('Quanti anni hai?') -> Il programma lo chiede ma poi lo scorda!")
print("GIUSTO: eta = input('Quanti anni hai?') -> Il dato viene salvato in 'eta'")

print("
Errore 4: Usare input() come numero senza convertire")
# numero = input("Numero: ")
# risultato = numero + 10  # ERRORE! Non puoi sommare stringa e numero
print("SOLUZIONE: numero = int(input('Numero: '))")

# ============================================================
# RIASSUNTO FINALE
# ============================================================

print("
=== RIASSUNTO ===")
print("1. print('testo') → Mostra un messaggio fisso sullo schermo.")
print("2. print(variabile) → Mostra il contenuto che c'è dentro una variabile.")
print("3. print('a', 'b') → Stampa più cose unendole con uno spazio.")
print("4. input('domanda') → Fa una domanda e ASPETTA la tua risposta sulla tastiera.")
print("5. var = input(...) → Salva la tua risposta nella variabile per usarla dopo.")
print("6. int(input(...)) → Converte la risposta in numero intero per fare calcoli.")
