# Appunti sul CONTROLLO DI FLUSSO (if, else, elif) per principianti
# Il controllo di flusso serve per fare scelte nel programma
# In base a una condizione, il programma fa cose diverse
# È come dire: "SE succede questo, FAI questo, ALTRIMENTI FAI quest'altro"

# ============================================================
# PARTE 1: ESEMPI SEMPLICI E FACILI
# ============================================================

print("=== ESEMPIO 1: IF SEMPLICE ===")
# La cosa più semplice: SE una condizione è vera, FAI qualcosa
eta = 18
if eta >= 18:
    print("Sei maggiorenne!")

print("\n=== ESEMPIO 2: IF CON ELSE ===")
# SE una condizione è vera, FAI qualcosa, ALTRIMENTI FAI un'altra cosa
temperatura = 15
if temperatura > 20:
    print("È caldo, metti un maglioncino leggero!")
else:
    print("È freddo, metti una giacca!")

print("\n=== ESEMPIO 3: IF CON ELIF E ELSE ===")
# SE è vero questo, FAI A. ALTRIMENTI SE è vero quest'altro, FAI B. ALTRIMENTI FAI C.
voto = 7
if voto >= 8:
    print("Bravo! Hai preso una buona votazione!")
elif voto >= 6:
    print("Sei passato, ma puoi fare meglio!")
else:
    print("Purtroppo hai preso un brutto voto.")

# ============================================================
# PARTE 2: COME FUNZIONANO LE CONDIZIONI
# ============================================================

print("\n=== COME FUNZIONANO LE CONDIZIONI ===")
# Una condizione è una domanda vera o falsa
# Usiamo operatori di confronto:

numero = 10
print("numero = 10")
print()
print("numero == 10:", numero == 10)   # Uguale? → True
print("numero != 10:", numero != 10)   # Diverso? → False
print("numero > 5:", numero > 5)       # Maggiore? → True
print("numero < 5:", numero < 5)       # Minore? → False
print("numero >= 10:", numero >= 10)   # Maggiore o uguale? → True
print("numero <= 5:", numero <= 5)     # Minore o uguale? → False

print("\n=== COMBINARE CONDIZIONI ===")
# Puoi combinare più condizioni con AND, OR, NOT
eta_persona = 25
ha_patente = True

if eta_persona >= 18 and ha_patente:
    print("Puoi guidare l'auto!")
else:
    print("Non puoi guidare ancora.")

# ============================================================
# PARTE 3: INDENTAZIONE (IMPORTANTE IN PYTHON!)
# ============================================================

print("\n=== INDENTAZIONE ===")
# In Python, l'indentazione (spazi all'inizio della riga) è MOLTO importante!
# Se ritorni il codice dentro if, else, elif DEVE essere indentato
# Sbagliare l'indentazione = errore!

numero = 5
if numero > 0:
    print("Il numero è positivo")  # Indentato con 4 spazi
    print("Scritto dentro l'if")    # Indentato con 4 spazi
print("Pronto!")                   # NON indentato, eseguito comunque

# ============================================================
# PARTE 4: ESEMPI PIÙ COMPLESSI
# ============================================================

print("\n=== ESEMPIO: SISTEMA DI VOTI ===")
voto = int(input("Inserisci il tuo voto (0-10): "))
if voto >= 9:
    print("Eccellente! 🌟")
elif voto >= 7:
    print("Buono! ✓")
elif voto >= 6:
    print("Accettabile")
elif voto >= 4:
    print("Insufficiente")
else:
    print("Molto insufficiente")

print("\n=== ESEMPIO: MAGGIORENNE O MINORENNE ===")
eta_utente = int(input("Quanti anni hai? "))
if eta_utente < 0:
    print("L'età non può essere negativa!")
elif eta_utente < 13:
    print("Sei un bambino!")
elif eta_utente < 18:
    print("Sei un adolescente!")
else:
    print("Sei un adulto!")

print("\n=== ESEMPIO: CALCOLATORE SEMPLICE ===")
numero1 = int(input("Primo numero: "))
numero2 = int(input("Secondo numero: "))
operazione = input("Operazione (+, -, *, /): ")

if operazione == "+":
    risultato = numero1 + numero2
    print(numero1, "+", numero2, "=", risultato)
elif operazione == "-":
    risultato = numero1 - numero2
    print(numero1, "-", numero2, "=", risultato)
elif operazione == "*":
    risultato = numero1 * numero2
    print(numero1, "*", numero2, "=", risultato)
elif operazione == "/":
    if numero2 != 0:
        risultato = numero1 / numero2
        print(numero1, "/", numero2, "=", risultato)
    else:
        print("Errore! Non puoi dividere per zero!")
else:
    print("Operazione non riconosciuta!")

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

print("\n=== ERRORI COMUNI ===")
print("Errore 1: Confondere = (assegnazione) con == (confronto)")
print("SBAGLIATO: if numero = 5:")  # Assegna, non confronta
print("GIUSTO: if numero == 5:")    # Confronta

print("\nErrore 2: Dimenticare i due punti :")
print("SBAGLIATO: if numero > 5")
print("GIUSTO: if numero > 5:")

print("\nErrore 3: Sbagliare l'indentazione")
print("SBAGLIATO: il codice dentro if NON indentato non funziona")
print("GIUSTO: il codice dentro if deve essere indentato")

# ============================================================
# RIASSUNTO FINALE
# ============================================================

print("\n=== RIASSUNTO ===")
print("1. if → SE la condizione è vera, FAI questo")
print("2. else → ALTRIMENTI, FAI questo")
print("3. elif → ALTRIMENTI SE la condizione è vera, FAI questo")
print("4. Operatori: ==, !=, >, <, >=, <=")
print("5. Combina condizioni con: and (e), or (o), not (non)")
print("6. RICORDA: Il codice dentro if/else/elif DEVE essere indentato!")