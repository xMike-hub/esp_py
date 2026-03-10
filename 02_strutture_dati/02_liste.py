# Appunti sulle LISTE per principianti
# Una lista è una collezione ordinata di elementi (numeri, stringhe, ecc.)
# Si usano le parentesi quadre [ ] per crearle
# Gli elementi sono separati da una virgola

# ============================================================
# PARTE 1: CREAZIONE E ACCESSO (GLI INDICI)
# ============================================================

print("=== ESEMPIO 1: CREARE UNA LISTA ===")
frutti = ["mela", "banana", "ciliegia", "arancia"]
print("Lista frutti:", frutti)

print("\n=== ESEMPIO 2: ACCEDERE AGLI ELEMENTI (INDEX) ===")
# IMPORTANTE: In Python si inizia a contare da 0!
print("Primo frutto (indice 0):", frutti[0])
print("Secondo frutto (indice 1):", frutti[1])
# L'indice negativo parte dalla fine
print("Ultimo frutto (indice -1):", frutti[-1])



# ============================================================
# PARTE 2: MODIFICARE LE LISTE (METODI)
# ============================================================

print("\n=== MODIFICARE LA LISTA ===")
# Cambiare un elemento esistente
frutti[1] = "mirtillo"
print("Dopo la modifica all'indice 1:", frutti)

# Aggiungere elementi
frutti.append("mango") # Aggiunge in fondo
print("Dopo .append():", frutti)

frutti.insert(1, "kiwi") # Aggiunge in una posizione specifica
print("Dopo .insert() in posizione 1:", frutti)

# Rimuovere elementi
frutti.remove("mela") # Rimuove un elemento specifico per nome
print("Dopo .remove('mela'):", frutti)

ultimo = frutti.pop() # Rimuove l'ultimo elemento e lo "restituisce"
print("Dopo .pop() (rimosso", ultimo, "):", frutti)

# ============================================================
# PARTE 3: OPERAZIONI UTILI
# ============================================================

print("\n=== OPERAZIONI SULLE LISTE ===")
numeri = [10, 5, 8, 20, 1]

# Ordinare la lista
numeri.sort()
print("Lista ordinata:", numeri)

# Sapere quanti elementi ci sono (Lunghezza)
lunghezza = len(numeri)
print("La lista contiene", lunghezza, "numeri")

# Verificare se un elemento esiste (IN)
cerca = 8
if cerca in numeri:
    print(f"Sì, il numero {cerca} è presente!")

# ============================================================
# PARTE 4: SLICING (TAGLIARE LE LISTE)
# ============================================================

print("\n=== SLICING [inizio:fine] ===")
# Prende un pezzo della lista (il 'fine' è escluso)
lettere = ["a", "b", "c", "d", "e"]
print("Primi tre:", lettere[0:3]) 
print("Dal terzo in poi:", lettere[2:])

# ============================================================
# ERRORI COMUNI E COME EVITARLI
# ============================================================

print("\n=== ERRORI COMUNI ===")
print("Errore 1: IndexError")
print("Cercare un indice che non esiste (es: frutti[100]) farà crashare il programma.")

print("\nErrore 2: Dimenticare che si parte da 0")
print("Se la lista ha 3 elementi, l'ultimo indice è 2, non 3!")

print("\nErrore 3: .append() vs .extend()")
print(".append(lista) mette una lista DENTRO un'altra lista.")
print(".extend(lista) unisce le due liste insieme.")

# ============================================================
# RIASSUNTO FINALE
# ============================================================

print("\n=== RIASSUNTO ===")
print("1. [ ] → Crea la lista")
print("2. lista[indice] → Accedi all'elemento (si parte da 0!)")
print("3. .append() → Aggiunge in coda")
print("4. .pop() → Toglie l'ultimo")
print("5. len(lista) → Dice quanto è lunga")
print("6. .sort() → Ordina gli elementi")