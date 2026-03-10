# Appunti completi sulle FUNZIONI in Python per principianti
# Una funzione è un "mini-programma" dentro il tuo programma.
# Le funzioni servono per:
# 1. Non ripetere lo stesso codice mille volte.
# 2. Rendere il codice più ordinato e leggibile.



# ============================================================
# PARTE 1: LA RICETTA BASE (Definire e Chiamare)
# ============================================================

print("=== 1. CREARE E USARE UNA FUNZIONE ===")

# DEF = "Definisco" la funzione. Le sto insegnando a fare qualcosa.
def saluta_utente():
    print("Ciao! Benvenuto nel sistema.")
    print("Spero tu stia passando una buona giornata!\n")

# Se non "chiamo" la funzione, lei non fa niente (sta solo lì a prendere polvere).
print("Ora chiamo la funzione due volte:")
saluta_utente()
saluta_utente()

# ============================================================
# PARTE 2: I PARAMETRI (Gli ingredienti della ricetta)
# ============================================================

print("=== 2. PASSARE DATI (PARAMETRI) ===")
# Una funzione può ricevere dei dati dall'esterno per fare il suo lavoro.

def crea_personaggio(nome, classe, livello):
    print(f"Giocatore creato: {nome}")
    print(f"Classe: {classe} | Livello: {livello}\n")

# Posso usare la stessa funzione per creare cose completamente diverse!
crea_personaggio("Gimli", "Guerriero", 10)
crea_personaggio("Legolas", "Arciere", 12)

# ============================================================
# PARTE 3: IL RITORNO (RETURN) vs PRINT
# ============================================================
# QUESTO È IL CONCETTO PIÙ IMPORTANTE DA CAPIRE!
# - print() serve solo per far LEGGERE qualcosa a te umano sullo schermo.
# - return serve per consegnare il risultato al computer, così può usarlo ancora.

print("=== 3. RETURN VS PRINT ===")

# Funzione con PRINT (fa vedere il risultato ma poi lo butta via)
def somma_finta(a, b):
    print(f"Risultato finto: {a + b}")

# Funzione con RETURN (calcola il risultato e te lo riconsegna in mano)
def somma_vera(a, b):
    risultato = a + b
    return risultato

somma_finta(5, 5) # Lo vedi a schermo, ma il computer non lo ricorda più.

# Con return, posso salvare il risultato in una variabile!
soldi_totali = somma_vera(10, 20) 
print(f"Ho salvato i soldi totali: {soldi_totali}")
print(f"Se raddoppio i soldi avrò: {soldi_totali * 2}\n")

# ============================================================
# PARTE 4: LA REGOLA DEL LAS VEGAS (Lo Scope)
# ============================================================
# Regola d'oro: "Quello che succede nella funzione, resta nella funzione"



print("=== 4. VARIABILI LOCALI (SCOPE) ===")

def operazione_segreta():
    # Questa variabile nasce e muore QUI DENTRO.
    codice_segreto = 12345
    print("Dentro la funzione il codice è:", codice_segreto)

operazione_segreta()

# Se togliessi il cancelletto dalla riga sotto, il programma andrebbe in CRASH!
# print(codice_segreto) 
# Perché? Perché fuori dalla funzione, 'codice_segreto' non esiste!

# ============================================================
# PROGRAMMINO INTERATTIVO
# ============================================================

print("\n=== CALCOLATRICE CON FUNZIONE ===")

def calcola_sconto(prezzo, percentuale_sconto):
    sconto_in_euro = (prezzo * percentuale_sconto) / 100
    prezzo_finale = prezzo - sconto_in_euro
    return prezzo_finale

# Usiamo la funzione chiedendo i dati all'utente!
prezzo_base = float(input("Inserisci il prezzo dell'articolo (€): "))
sconto = int(input("Inserisci lo sconto da applicare (%): "))

# Chiamo la funzione passandole i dati dell'utente
totale_da_pagare = calcola_sconto(prezzo_base, sconto)

print(f"Prezzo originale: {prezzo_base}€")
print(f"Prezzo scontato: {totale_da_pagare}€")

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

# === ERRORI COMUNI ===
# Errore 1: Dimenticare le parentesi () quando chiami la funzione
# SBAGLIATO: saluta_utente -> Python legge il nome ma NON la esegue.
# GIUSTO: saluta_utente() -> Le parentesi sono il comando 'AGISCI ORA!'.

# Errore 2: Cercare di usare una variabile 'locale' fuori dalla funzione
# SBAGLIATO: cerchi di stampare 'sconto_in_euro' fuori dalla funzione.
# Perché? Perché quella variabile esiste solo finché la funzione sta lavorando, poi scompare (Scope Error).

# Errore 3: Indentazione (spazi) sbagliata
# Se non metti gli spazi sotto il 'def', Python non capisce che quel codice fa parte della funzione!

# Errore 4: Confondere print con return
# Se una funzione deve passarti un dato per fare altri calcoli, DEVI usare return. 
# Se usi print, il dato va perso e ottieni l'errore 'NoneType'.

# ============================================================
# RIASSUNTO FINALE
# ============================================================

# === RIASSUNTO ===
# 1. def crea la funzione, ma per usarla devi chiamarla con il suo nome().
# 2. I parametri (...) sono gli input, i dati che dai alla funzione.
# 3. print() mostra a schermo, return consegna il dato al programma.
# 4. Le variabili create dentro una funzione non esistono al di fuori di essa!