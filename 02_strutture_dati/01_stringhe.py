# Appunti sulle STRINGHE in Python per principianti
# Le stringhe (str) sono sequenze di caratteri (lettere, numeri, spazi, simboli).
# Si creano racchiudendo il testo tra virgolette doppie (" ") o singole (' ').

# ============================================================
# PARTE 1: CREAZIONE E CONCATENAZIONE (Unire i testi)
# ============================================================

print("=== 1. CREAZIONE E CONCATENAZIONE ===")
messaggio = "Ciao, Python!"
nome = 'Mario'  # Singole o doppie è indifferente per Python
frase = "Python è fantastico!"

# Concatenazione: usare il + per incollare due o più stringhe
cognome = "Rossi"
nome_completo = nome + " " + cognome  # Aggiungiamo uno spazio in mezzo!
print("Nome completo:", nome_completo)

# ============================================================
# PARTE 2: LUNGHEZZA E INDICI (Come per le liste!)
# ============================================================

print("\n=== 2. LUNGHEZZA E INDICI ===")
# len() conta quanti caratteri ci sono (compresi gli spazi e la punteggiatura)
print("Lunghezza di 'Ciao':", len("Ciao"))
print("Il messaggio ha", len(messaggio), "caratteri")



# Accedere ai singoli caratteri usando le parentesi quadre [] (Si parte da 0!)
testo = "Python"
print("La parola è:", testo)
print("Primo carattere (indice 0):", testo[0])   # P
print("Secondo carattere (indice 1):", testo[1]) # y
print("Ultimo carattere (indice -1):", testo[-1])# n

# ============================================================
# PARTE 3: I METODI DELLE STRINGHE (Azioni pronte all'uso)
# ============================================================
# Si usano scrivendo: nome_variabile.metodo()

print("\n=== 3. METODI PRINCIPALI ===")
# .lower() e .upper() per le maiuscole/minuscole
print("Tutto minuscolo:", messaggio.lower())
print("Tutto maiuscolo:", messaggio.upper())

# .replace(vecchio, nuovo) per sostituire parole o lettere
frase_modificata = frase.replace("fantastico", "meraviglioso")
print("Frase modificata:", frase_modificata)

# .split(separatore) taglia la stringa e crea una LISTA!
frase_divisa = "Ciao, come stai?"
parole = frase_divisa.split(",") # Taglia dove c'è la virgola
print("Parole divise in una lista:", parole)

# ============================================================
# PARTE 4: RICERCA E STRINGHE MULTIRIGA
# ============================================================

print("\n=== 4. RICERCA E TESTI LUNGHI ===")
# L'operatore 'in' verifica se una sottostringa esiste
if "Python" in frase:
    print("Sì, la parola 'Python' è presente nella frase!")

# Le tre virgolette (""") permettono di andare a capo liberamente
poesia = """Python è bello
Facile e divertente
Perfetto per imparare!"""
print("Poesia:\n" + poesia)

# ============================================================
# PROGRAMMINO INTERATTIVO
# ============================================================

print("\n=== SALUTO PERSONALIZZATO ===")
nome_utente = input("Inserisci il tuo nome: ")
# Uniamo le stringhe per creare la frase finale
saluto = "Benvenuto, " + nome_utente + "! Stai imparando Python!"
print(saluto)
print("Curiosità: Il tuo nome è lungo", len(nome_utente), "caratteri.")

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

print("\n=== ERRORI COMUNI ===")
print("Errore 1: Dimenticare di chiudere le virgolette, o mischiarle")
print("SBAGLIATO: stringa = \"Ciao'")
print("GIUSTO: stringa = \"Ciao\" oppure 'Ciao'")

print("\nErrore 2: Sommare stringhe e numeri (TypeError)")
print("SBAGLIATO: print('Il mio numero è ' + 10)")
print("GIUSTO: print('Il mio numero è ' + str(10)) -> str() converte il numero in testo")
print("OPPURE: print('Il mio numero è', 10) -> La virgola nel print gestisce tutto da sola")

# ============================================================
# RIASSUNTO FINALE
# ============================================================

print("\n=== RIASSUNTO ===")
print("1. 'testo' o \"testo\" → Creano la stringa")
print("2. stringa1 + stringa2 → Le unisce (concatenazione)")
print("3. len(stringa) → Conta i caratteri")
print("4. stringa[0] → Prende il primo carattere")
print("5. Metodi utili: .upper(), .lower(), .replace(), .split()")