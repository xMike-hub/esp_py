# Appunti su COME USARE LE PROPRIE IMPORTAZIONI
# Perché importiamo altri file? 
# 1. Per non fare "copia e incolla" dello stesso codice in 100 file diversi.
# 2. Per tenere i file corti, ordinati e facili da leggere.
# 3. Se trovo un errore in una funzione, lo correggo in UN SOLO file, e in automatico 
#    si aggiorna in tutti i programmi che la stanno importando!



# ============================================================
# PARTE 1: IMPORTARE IL NOSTRO FILE
# ============================================================
print("=== 1. IMPORTIAMO LA NOSTRA CASSETTA DEGLI ATTREZZI ===")

# Immagina che il file di prima si chiami 'importazioni_e_main.py'
# e si trovi nella STESSA CARTELLA di questo file.
# Lo importiamo per rubargli le funzioni che avevamo creato!

import importazioni_e_main

print("\n(Se hai notato, non è apparso nessun messaggio di test dal file importato.")
print("Questo è il miracolo dell' 'if __name__ == \"__main__\":' che abbiamo usato di là!)")

# ============================================================
# PARTE 2: USARE GLI STRUMENTI IMPORTATI
# ============================================================
print("\n=== 2. USIAMO LE FUNZIONI ===")
# Per usare una funzione dell'altro file, scriviamo: nome_file.nome_funzione()

print("Sto giocando a Monopoli e mi serve un dado...")
# Chiamo la funzione lancia_dado() che vive nell'altro file!
mio_dado = importazioni_e_main.lancia_dado()
print(f"Ho tirato il dado ed è uscito: {mio_dado}")

print("\nOra devo calcolare l'area di una torta di raggio 10...")
# Chiamo l'altra funzione!
area_torta = importazioni_e_main.calcola_area_cerchio(10)
print(f"L'area della mia torta è: {area_torta}")


# ============================================================
# ERRORI COMUNI E COME EVITARLI (Solo appunti)
# ============================================================

# === ERRORI COMUNI ===
# Errore 1: Dimenticare il nome del file prima della funzione
# SBAGLIATO: lancia_dado() -> Python cercherà questa funzione IN QUESTO file e darà errore.
# GIUSTO: importazioni_e_main.lancia_dado() -> Diciamo a Python esattamente DOVE andare a prenderla.

# Errore 2: Cercare di importare il file con il ".py" alla fine
# SBAGLIATO: import importazioni_e_main.py
# GIUSTO: import importazioni_e_main (Python sa già che è un file .py!)

# ============================================================
# RIASSUNTO FINALE
# ============================================================

# === RIASSUNTO ===
# 1. Importare i tuoi file ti salva ore di "copia e incolla".
# 2. I file comunicano tra loro: uno fa il lavoro sporco (calcoli, funzioni), 
#    l'altro (il main) guida il programma e lo mostra all'utente.
# 3. Grazie a `if __name__ == "__main__":` nell'altro file, importarlo è sicuro e pulito!