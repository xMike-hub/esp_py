# Appunti sui DIZIONARI in Python per principianti
# Un dizionario è una collezione di dati che funziona a coppie: "Chiave" e "Valore".
# - Si usano le parentesi graffe { }
# - Ogni elemento è scritto così: "chiave": "valore"
# - Gli elementi sono separati da virgole



# ============================================================
# PARTE 1: CREAZIONE E ACCESSO
# ============================================================

print("=== 1. CREARE UN DIZIONARIO ===")
# Immagina di descrivere un personaggio o un utente
utente = {
    "nome": "Luca",
    "eta": 25,
    "ruolo": "Admin",
    "attivo": True
}
print("Tutto il dizionario:", utente)

print("\n=== 2. LEGGERE I VALORI ===")
# Invece di usare i numeri (indici) come nelle liste, si usa il nome della CHIAVE
print("Il nome dell'utente è:", utente["nome"])
print("La sua età è:", utente["eta"])

# ============================================================
# PARTE 2: AGGIUNGERE E MODIFICARE
# ============================================================

print("\n=== 3. MODIFICARE E AGGIUNGERE ===")
# Modificare un valore esistente (basta sovrascriverlo)
utente["eta"] = 26
print("Età aggiornata a:", utente["eta"])

# Aggiungere una NUOVA coppia chiave-valore
utente["citta"] = "Roma"
print("Dizionario dopo aver aggiunto la città:", utente)

# ============================================================
# PARTE 3: RIMUOVERE ELEMENTI E METODI UTILI
# ============================================================

print("\n=== 4. RIMUOVERE ELEMENTI ===")
# Il metodo .pop() rimuove la chiave e ti restituisce il suo valore
ruolo_rimosso = utente.pop("ruolo")
print("Ho rimosso il ruolo:", ruolo_rimosso)
print("Dizionario attuale:", utente)

print("\n=== 5. I TRE METODI PIÙ IMPORTANTI ===")
# .keys() -> Ti dà solo l'elenco delle chiavi (i "titoli")
print("Solo le chiavi:", utente.keys())

# .values() -> Ti dà solo l'elenco dei valori (i "contenuti")
print("Solo i valori:", utente.values())

# .items() -> Ti dà le coppie (molto utile da usare con i cicli for)
print("Coppie chiave-valore:", utente.items())

# ============================================================
# PROGRAMMINO INTERATTIVO
# ============================================================

print("\n=== INTERROGA IL DIZIONARIO ===")
# Usiamo il metodo .get() che è più sicuro delle parentesi quadre
# Se la chiave non esiste, .get() restituisce 'None' o un messaggio personalizzato
informazione = input("Cosa vuoi sapere dell'utente? (nome/eta/citta): ")

risultato = utente.get(informazione, "Informazione non trovata!")
print(f"Risultato per '{informazione}':", risultato)

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

print("\n=== ERRORI COMUNI ===")
print("Errore 1: KeyError")
print("Succede se provi a leggere una chiave che non esiste con le parentesi quadre.")
print("SBAGLIATO: print(utente['cognome']) -> Crash del programma se 'cognome' non c'è!")
print("GIUSTO: Usa utente.get('cognome') -> Se non c'è, restituisce 'None' senza crashare.")

print("\nErrore 2: Dimenticare le virgole o i due punti")
print("Ogni coppia deve essere 'chiave': 'valore' e separata da una virgola dalla successiva.")

# ============================================================
# RIASSUNTO FINALE
# ============================================================

print("\n=== RIASSUNTO ===")
print("1. { } → Creano il dizionario")
print("2. dizionario['chiave'] → Legge o modifica un valore")
print("3. dizionario['nuova_chiave'] = valore → Crea una nuova coppia")
print("4. .get('chiave') → Legge un valore in modo sicuro senza crashare")
print("5. .keys(), .values(), .items() → Per esplorare il contenuto")