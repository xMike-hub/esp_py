# Appunti sulle stringhe in Python per principianti
# Le stringhe sono sequenze di caratteri (lettere, numeri, simboli) racchiuse tra virgolette.
# Puoi usare " " oppure ' ' indifferentemente.

# Esempi di stringhe:
messaggio = "Ciao, Python!"
nome = 'Mario'
frase = "Python è fantastico!"

print("Messaggio:", messaggio)
print("Nome:", nome)
print("Frase:", frase)

# Concatenazione (unire stringhe):
cognome = "Rossi"
nome_completo = nome + " " + cognome
print("Nome completo:", nome_completo)

# Lunghezza della stringa (quanti caratteri ha):
print("Lunghezza di 'Ciao':", len("Ciao"))
print("Lunghezza di messaggio:", len(messaggio))

# Accedere ai caratteri (posizione inizia da 0):
testo = "Python"
print("Primo carattere:", testo[0])   # P
print("Secondo carattere:", testo[1]) # y
print("Ultimo carattere:", testo[-1]) # n

# Metodi utili delle stringhe:
testo_minuscolo = messaggio.lower()  # Tutte minuscole
print("Minuscolo:", testo_minuscolo)

testo_maiuscolo = messaggio.upper()  # Tutte maiuscole
print("Maiuscolo:", testo_maiuscolo)

# Trovare una parte dentro la stringa:
if "Python" in frase:
    print("La parola Python è nella frase!")

# Sostituire una parte:
frase_modificata = frase.replace("fantastico", "meraviglioso")
print("Frase modificata:", frase_modificata)

# Dividere una stringa:
frase_divisa = "Ciao, come stai?"
parole = frase_divisa.split(",")
print("Parole divise:", parole)

# Stringhe con più righe:
poesia = """Python è bello
Facile e divertente
Perfetto per imparare!"""
print("Poesia:\n" + poesia)

# Esempi NON corretti (commentati per non dare errori):
# stringa = "Ciao'  # Errore: virgolette non chiuse
# print("Testo" 'Testo2')  # Errore: assenza di operatore tra stringhe
# print(stringa + 10)  # Errore: non puoi sommare stringa e numero

# Per rendere interattivo: chiediamo il nome e creiamo un saluto personalizzato
nome_utente = input("Inserisci il tuo nome: ")
saluto = "Benvenuto, " + nome_utente + "! Stai imparando Python!"
print(saluto)
print("Il tuo nome ha", len(nome_utente), "caratteri.")