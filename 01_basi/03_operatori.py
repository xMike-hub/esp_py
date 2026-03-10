# Appunti sugli OPERATORI in Python per principianti
# Gli operatori sono simboli magici che dicono a Python di fare operazioni sui dati.
# Ci sono 4 famiglie principali: Aritmetici, di Confronto, Logici, di Assegnazione.

# ============================================================
# PARTE 1: OPERATORI ARITMETICI (La Calcolatrice)
# ============================================================

print("=== 1. OPERATORI ARITMETICI ===")
a = 10
b = 3

print(f"I nostri numeri di partenza sono: a={a}, b={b}\n")
print("Somma (+):", a + b)           # 13
print("Sottrazione (-):", a - b)     # 7
print("Moltiplicazione (*):", a * b) # 30
print("Divisione (/):", a / b)       # 3.3333333333333335 (Restituisce sempre un decimale/float)

# Questi tre sotto sono i più importanti da imparare bene:
print("Divisione intera (//):", a // b) # 3 (Toglie i decimali, quante volte il 3 sta nel 10?)
print("Resto o Modulo (%):", a % b)     # 1 (Cosa avanza dalla divisione intera?)
print("Potenza (**):", a ** b)          # 1000 (10 elevato alla 3)



# ============================================================
# PARTE 2: OPERATORI DI CONFRONTO (Le Domande)
# ============================================================
# Restituiscono sempre un valore Booleano: True (Vero) o False (Falso)

print("\n=== 2. OPERATORI DI CONFRONTO ===")
print(f"Confrontiamo {a} e {b}:")
print("Uguale (==):", a == b)             # False
print("Diverso (!=):", a != b)            # True
print("Maggiore (>):", a > b)             # True
print("Minore (<):", a < b)               # False
print("Maggiore o uguale (>=):", a >= b)  # True
print("Minore o uguale (<=):", a <= b)    # False

# ============================================================
# PARTE 3: OPERATORI LOGICI (Combinare le Domande)
# ============================================================



#[Image of logic truth tables AND OR NOT]


print("\n=== 3. OPERATORI LOGICI ===")
x = True
y = False

print("AND (e):", x and y) # False (Devono essere ENTRAMBI veri)
print("OR (o):", x or y)   # True  (Basta che UNO SOLO sia vero)
print("NOT (non):", not x) # False (Inverte la carta: il Vero diventa Falso)

# ============================================================
# PARTE 4: OPERATORI DI ASSEGNAZIONE (Le Scorciatoie)
# ============================================================

print("\n=== 4. OPERATORI DI ASSEGNAZIONE ===")
c = 5
print("Valore iniziale di c:", c)

c += 2  # È esattamente uguale a scrivere: c = c + 2
print("Dopo c += 2:", c) # 7

c -= 1  # È esattamente uguale a scrivere: c = c - 1
print("Dopo c -= 1:", c) # 6

c *= 3  # È esattamente uguale a scrivere: c = c * 3
print("Dopo c *= 3:", c) # 18

# ============================================================
# PROGRAMMINO INTERATTIVO
# ============================================================

print("\n=== CALCOLA LA TUA ETÀ ===")
# Usiamo int() perché input() restituisce sempre del testo!
anno_nascita = int(input("Inserisci il tuo anno di nascita (es. 2000): "))
anno_corrente = 2026  # Aggiornato all'anno attuale
eta = anno_corrente - anno_nascita
print("Nel", anno_corrente, "hai (o compirai)", eta, "anni!")

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

print("\n=== ERRORI COMUNI ===")
print("Errore 1: TypeError (Mischiare tipi incompatibili)")
print("SBAGLIATO: print(10 + 'ciao') -> Python non sa come sommare un numero a una parola!")

print("\nErrore 2: Confondere = con ==")
print("SBAGLIATO: if a = b: -> '=' serve per mettere un valore nella scatola (assegnazione)")
print("GIUSTO: if a == b: -> '==' serve per fare una domanda di uguaglianza (confronto)")

# ============================================================
# RIASSUNTO FINALE
# ============================================================

print("\n=== RIASSUNTO ===")
print("1. Aritmetici: +, -, *, /, // (senza virgola), % (resto), ** (potenza)")
print("2. Confronto: ==, !=, >, <, >=, <=")
print("3. Logici: and (tutti veri), or (almeno uno vero), not (inverte)")
print("4. Assegnazione: =, +=, -=, *=, /=")