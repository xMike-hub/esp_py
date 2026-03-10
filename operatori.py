# Appunti sugli operatori in Python per principianti
# Gli operatori sono simboli che permettono di fare operazioni sui dati.
# Ci sono diversi tipi: aritmetici, di confronto, logici, di assegnazione.

# Operatori aritmetici (per fare calcoli):
a = 10
b = 3

print("Somma:", a + b)        # 13
print("Sottrazione:", a - b)  # 7
print("Moltiplicazione:", a * b)  # 30
print("Divisione:", a / b)    # 3.333...
print("Divisione intera:", a // b)  # 3 (senza decimali)
print("Resto:", a % b)        # 1 (resto della divisione)
print("Potenza:", a ** b)     # 1000 (10 alla terza)

# Operatori di confronto (per confrontare valori):
print("Uguale:", a == b)      # False
print("Diverso:", a != b)     # True
print("Maggiore:", a > b)     # True
print("Minore:", a < b)       # False
print("Maggiore o uguale:", a >= b)  # True
print("Minore o uguale:", a <= b)    # False

# Operatori logici (per combinare condizioni):
x = True
y = False

print("AND:", x and y)  # False (vero solo se entrambi veri)
print("OR:", x or y)    # True (vero se almeno uno è vero)
print("NOT:", not x)    # False (inverte il valore)

# Operatori di assegnazione (per assegnare valori):
c = 5
print("Iniziale:", c)
c += 2  # c = c + 2
print("Dopo += 2:", c)
c -= 1  # c = c - 1
print("Dopo -= 1:", c)
c *= 3  # c = c * 3
print("Dopo *= 3:", c)

# Esempi NON corretti (commentati per non dare errori):
# print(10 + "ciao")  # Errore: non puoi sommare numero e testo
# print(a = b)        # Errore: usa == per confronto, = per assegnazione

# Per rendere interattivo: calcoliamo l'età tra due anni
anno_nascita = int(input("Inserisci il tuo anno di nascita: "))
anno_corrente = 2023  # Puoi cambiarlo
eta = anno_corrente - anno_nascita
print("Hai circa", eta, "anni!")