
# Appunti sui CICLI (for e while) in Python per principianti
# I cicli servono per RIPETERE delle istruzioni più volte.
# Invece di scrivere la stessa cosa 100 volte, usi un ciclo!
# In Python ci sono due tipi: FOR e WHILE



# ============================================================
# PARTE 1: ESEMPI SEMPLICI E FACILI
# ============================================================

print("=== ESEMPIO 1: CICLO WHILE SEMPLICE ===")
# Definiamo una variabile che partirà da 0
contatore = 0
# WHILE significa: FINCHÉ la seguente condizione è vera, ripeti il codice
# La condizione è: contatore < 3 (cioè finché contatore è minore di 3)
while contatore < 3:
    # Stampiamo il valore di contatore
    print("Ciao! Contatore:", contatore)
    # IMPORTANTE: Aumentiamo contatore di 1, altrimenti il ciclo non finisce mai!
    contatore = contatore + 1
# Qui il ciclo finisce perché contatore è diventato 3 (non < 3)
print("Fine mentre!\n")




print("=== ESEMPIO 2: CICLO FOR SEMPLICE ===")
# FOR significa: PER OGNI numero (da 0 a 2), ripeti il codice
# range(3) genera i numeri: 0, 1, 2
# La variabile "numero" prende uno di questi valori ogni volta
for numero in range(3):  # Ripeti 3 volte: numero = 0, 1, 2
    # Stampiamo il valore di numero
    print("Numero:", numero)
# Qui il ciclo finisce perché abbiamo finito i numeri di range(3)
print("Fine for!\n")




print("=== ESEMPIO 3: FOR CON UNA LISTA ===")
# Creiamo una lista di frutti
frutti = ["mela", "banana", "arancia"]
# FOR scorre ogni elemento della lista, uno per uno
# La variabile "frutto" prende il valore di ogni elemento
for frutto in frutti:
    # Stampiamo il frutto corrente
    print("Frutto:", frutto)
# Qui il ciclo finisce perché abbiamo finito gli elementi della lista





# ============================================================
# PARTE 2: COME FUNZIONANO E DIFFERENZE
# ============================================================

# === COME FUNZIONA WHILE ===
# Sintassi: while condizione:
#          ... codice ...
#
# Logica: Finché la condizione è VERA, ripeti il codice
#         Quando la condizione diventa FALSA, esci dal ciclo

numero = 1
print("Esempio: Stampa finché numero < 4")
while numero < 4:
    print("  numero =", numero)
    numero = numero + 1
print("Condizione falsa! Esci dal ciclo.\n")

# === COME FUNZIONA FOR ===
# Sintassi: for variabile in sequenza:
#          ... codice ...
#
# Logica: Per OGNI elemento nella sequenza, ripeti il codice
#         La variabile prende il valore di ogni elemento uno per uno

numeri = [10, 20, 30]
print("Esempio: Stampa ogni numero dalla lista")
for num in numeri:
    print("  num =", num)
print("Fine della lista! Esci dal ciclo.\n")

# === DIFFERENZA TRA FOR E WHILE ===
# FOR: Quando CONOSCI quante volte devi ripetere
#      Es: Scorrere una lista, ripetere 5 volte, numeri da 1 a 10
#
# WHILE: Quando DIPENDE DA UNA CONDIZIONE
#        Es: Finché l'utente non digita 'esci', continua
#        Es: Finché il numero non è maggiore di 100, continua





# ============================================================
# PARTE 3: ESEMPI PIÙ COMPLESSI
# ============================================================

print("\n=== ESEMPIO 1: FOR CON RANGE ===")
# range(n) genera numeri da 0 a n-1
print("range(5) = numeri da 0 a 4")
for i in range(5):
    print("  i =", i)
    


print("\nrange(2, 6) = numeri da 2 a 5")
for i in range(2, 6):
    print("  i =", i)

    

print("\n=== ESEMPIO 2: FOR CON range E STEP ===")
# range(inizio, fine, step) con incremento personalizzato
print("range(0, 10, 2) = numeri da 0 a 9, ogni 2")
for i in range(0, 10, 2):
    print("  i =", i)



print("\n=== ESEMPIO 3: WHILE CON CONDIZIONE COMPLESSA ===")
# WHILE continua finché una condizione è vera
numero_segreto = 5
tentativi = 0
print("Indovinando il numero segreto (5):")
numero_utente = int(input("Indovina il numero: "))
while numero_utente != numero_segreto:
    print("Sbagliato! Riprova.")
    numero_utente = int(input("Indovina il numero: "))
print("Esatto! Hai vinto!\n")



print("=== ESEMPIO 4: FOR PER CONTARE ===")
# Usa for quando vuoi contare (sapere esattamente quante volte)
print("Conto da 1 a 5:")
for i in range(1, 6):
    print(i)



print("\n=== ESEMPIO 5: WHILE PER LEGGERE FINCHÉ ===")
# Usa while quando dipende da una condizione di arresto
somma = 0
numero = int(input("Inserisci numeri (0 per finire): "))
while numero != 0:
    somma = somma + numero
    numero = int(input("Inserisci numeri (0 per finire): "))
print("Somma totale:", somma)



print("\n=== ESEMPIO 6: CICLI ANNIDATI ===")
# Un ciclo dentro un altro ciclo
print("Tabella di moltiplicazione:")
for riga in range(1, 4):  # Righe 1, 2, 3
    for colonna in range(1, 4):  # Colonne 1, 2, 3
        risultato = riga * colonna
        print(f"{riga} x {colonna} = {risultato}", end="  ")
    print()  # A capo dopo ogni riga
    
    
    
    

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

# === ERRORI COMUNI ===
# Errore 1: CICLO INFINITO
# SBAGLIATO: while True:
#              print("Questo non finisce")
# PROBLEMA: La condizione "True" è sempre vera, il ciclo non finisce mai!
# SOLUZIONE: Usa una condizione che diventa falsa, come "while numero < 5:"
#
# Errore 2: Dimenticare di aggiornare la variabile in WHILE
# SBAGLIATO: numero = 0
#            while numero < 5:
#              print(numero)
# PROBLEMA: numero rimane sempre 0, il ciclo non finisce mai!
# SOLUZIONE: Aumenta la variabile dentro il ciclo: numero = numero + 1
#
# Errore 3: Sbagliare l'indentazione
# SBAGLIATO: Il codice dentro il ciclo NON indentato non fa parte del ciclo
# PROBLEMA: Python non sa qual è il codice da ripetere
# SOLUZIONE: Il codice dentro il ciclo DEVE essere indentato (4 spazi)
#
# Errore 4: Usare FOR su un numero
# SBAGLIATO: for i in 10:
#              print(i)
# PROBLEMA: 10 non è una sequenza, FOR ha bisogno di una lista o range
# SOLUZIONE: for i in range(10):  oppure  for i in [1, 2, 3]:

# ============================================================
# RIASSUNTO FINALE
# ============================================================

# === RIASSUNTO FINALE ===
# QUANDO USARE FOR
# Usa FOR quando conosci il numero di iterazioni
# Se hai una lista: for elemento in lista:
# Se vuoi contare: for i in range(5):
# FOR sa IN ANTICIPO quanti cicli farà
#
# QUANDO USARE WHILE
# Usa WHILE quando dipende da una condizione
# Sintassi: while condizione:
# RICORDA: La condizione deve diventare falsa per uscire dal ciclo!
# WHILE NON sa in anticipo quanti cicli farà
#
# DIFFERENZA CHIAVE
# FOR = Sa esattamente quante volte ripetersi (iterazioni fisse)
# WHILE = Ripete finché una condizione è vera (iterazioni variabili)
#
# REGOLA IMPORTANTE
# INDENTAZIONE! Il codice dentro il ciclo DEVE essere indentato!
# Se dimentichi l'indentazione, Python non sa qual è il codice da ripetere    