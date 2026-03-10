# Appunti sulle VARIABILI in Python per principianti
# Le variabili sono come "scatole" con un'etichetta sopra, in cui mettiamo i nostri dati.
# In Python, per creare una variabile basta inventare un nome e assegnarle un valore con "=".

#[Image of programming variables as labeled boxes holding values]

# ============================================================
# PARTE 1: I 4 TIPI DI DATO PRINCIPALI
# ============================================================

print("=== 1. CREAZIONE E TIPI DI DATO ===")
# Python capisce da solo che tipo di dato stai inserendo nella scatola:

nome = "Mario"      # str (Stringa): Testo, va sempre tra virgolette
eta = 25            # int (Intero): Numero senza virgola
altezza = 1.75      # float (Decimale): Numero con il PUNTO (non usare la virgola!)
is_studente = True  # bool (Booleano): Vero o Falso (True o False, sempre con la Maiuscola)

print("Nome (str):", nome)
print("Età (int):", eta)
print("Altezza (float):", altezza)
print("È studente? (bool):", is_studente)

# ============================================================
# PARTE 2: REGOLE PER I NOMI DELLE VARIABILI
# ============================================================

print("\n=== 2. COME SCRIVERE I NOMI ===")
# Regole fisse di Python:
# - Devono iniziare con una lettera o un underscore (_)
# - Possono contenere SOLO lettere, numeri e underscore
# - NON possono iniziare con un numero
# - Sono case-sensitive (Maiuscole e minuscole sono scatole diverse!)

# Esempi CORRETTI:
mia_variabile = 10   # Questo stile (tutto minuscolo con underscore) si chiama "snake_case" ed è lo standard in Python!
_variabile = 20      # Usato per variabili "nascoste" o speciali
Variabile123 = 30    # Corretto, ma di solito la maiuscola iniziale si usa per altre cose (le Classi)

# Esempi NON corretti (commentati per non far crashare il programma):
# 123variabile = 40  # Errore (SyntaxError): inizia con un numero
# mia-variabile = 50 # Errore: il trattino in mezzo è visto come una sottrazione!
# mia variabile = 60 # Errore: gli spazi non sono MAI permessi nei nomi

# ============================================================
# PROGRAMMINO INTERATTIVO
# ============================================================

print("\n=== CREA LE TUE VARIABILI ===")
# Riempiamo le variabili con i dati scritti dall'utente
nome_utente = input("Inserisci il tuo nome: ")

# Ricorda: input() crea sempre una Stringa! Usiamo int() per trasformarla in numero intero
eta_utente = int(input("Inserisci la tua età: "))

print("Ciao", nome_utente, "hai", eta_utente, "anni!")

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

print("\n=== ERRORI COMUNI ===")
print("Errore 1: Usare parole riservate")
print("Non puoi chiamare una variabile 'print', 'if', 'True' o 'for', perché Python le usa già per altro!")

print("\nErrore 2: Dimenticare che Python è Case-Sensitive")
print("Se crei: Nome = 'Luca'")
print("E poi chiedi: print(nome) -> ERRORE (NameError), perché 'Nome' e 'nome' sono due cose diverse.")

# ============================================================
# RIASSUNTO FINALE
# ============================================================

print("\n=== RIASSUNTO ===")
print("1. nome = valore → Crea la scatola e ci mette dentro il dato")
print("2. Tipi base: str (testo), int (interi), float (decimali), bool (True/False)")
print("3. Usa lo 'snake_case' (parole_separate_da_underscore) per i nomi")
print("4. Mai spazi, mai numeri all'inizio, mai trattini centrali nel nome")