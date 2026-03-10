# Appunti sulle IMPORTAZIONI GLOBALI e il magico if __name__ == "__main__":
# Quando i programmi crescono, li dividiamo in più file.
# Ma cosa succede se un file viene "importato" da un altro?
# Python eseguirà tutto! Per evitare disastri o stampe a caso, usiamo una "guardia".



# ============================================================
# PARTE 1: IMPORTAZIONI GLOBALI (In cima al file)
# ============================================================
# Mettendo gli import qui in alto, li rendiamo "GLOBALI" per l'intero file.
# Significa che QUALSIASI funzione che scriviamo qui sotto potrà usare questi strumenti,
# senza doverli importare di nuovo ogni volta.

import math      # Cassetta degli attrezzi per la matematica
import random    # Cassetta degli attrezzi per generare cose casuali

# ============================================================
# PARTE 2: CREIAMO I NOSTRI STRUMENTI (Le Funzioni)
# ============================================================
# Ora definisco delle funzioni che usano i moduli globali importati sopra.
# Queste funzioni sono i "servizi" che questo file offre.

def calcola_area_cerchio(raggio):
    # Posso usare 'math.pi' tranquillamente perché l'ho importato in cima!
    area = math.pi * (raggio ** 2)
    return round(area, 2)  # Arrotondo a 2 decimali

def lancia_dado():
    # Posso usare 'random' perché è globale per questo file!
    numero = random.randint(1, 6)
    return numero



# ============================================================
# PARTE 3: LA GUARDIA (La stanza dei bottoni)
# ============================================================
# Questo blocco è FONDAMENTALE nei progetti veri. Significa:
# "SE questo file viene avviato DIRETTAMENTE dal terminale, esegui questo codice."
# "MA SE questo file viene IMPORTATO da un altro file, ignora tutta questa parte!"

if __name__ == "__main__":
    
    # Tutto ciò che è indentato qui sotto verrà eseguito SOLO se fai "python3 importazioni_e_main.py"
    print("=== IL PROGRAMMA PRINCIPALE È PARTITO! ===")
    print("Visto che hai avviato questo file direttamente, ti faccio vedere i test:\n")

    # Uso le funzioni che ho creato sopra
    print(f"Lancio del dado: è uscito un bel {lancia_dado()}!")
    print(f"L'area di un cerchio di raggio 5 è: {calcola_area_cerchio(5)}")

    print("\n[Nota: Se un altro file facesse 'import importazioni_e_main',")
    print("queste scritte NON apparirebbero sul suo schermo! L'altro file")
    print("otterrebbe solo l'accesso segreto alle funzioni in alto.]")


# ============================================================
# ERRORI COMUNI E COME EVITARLI (Solo appunti)
# ============================================================

# === ERRORI COMUNI ===
# Errore 1: Importare la stessa cosa dentro ogni funzione
# SBAGLIATO: Scrivere 'import math' dentro 'calcola_area_cerchio'. Non serve!
# GIUSTO: Mettere 'import math' alla riga 1 del file. Così diventa "Globale" 
# e tutte le funzioni del file lo vedranno.

# Errore 2: Scrivere codice "libero" senza il blocco if __name__ == "__main__":
# Se metti dei print() fuori dalle funzioni e fuori dal blocco __main__,
# chiunque importerà il tuo file vedrà apparire quelle scritte a caso sul suo schermo 
# rovinando il suo programma!

# ============================================================
# RIASSUNTO FINALE
# ============================================================

# === RIASSUNTO ===
# 1. Gli 'import' vanno sempre all'inizio del file. Così valgono per tutto il codice (Globali).
# 2. Le funzioni definiscono gli "attrezzi" che il tuo file mette a disposizione.
# 3. if __name__ == "__main__": è la tua area di test sicura.
#    - Se premi "Play" su QUESTO file, si attiva.
#    - Se un amico importa QUESTO file nel suo, questa parte rimane spenta e invisibile.