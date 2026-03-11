import socket as so 

SRV_ADDR = '0.0.0.0'
SRV_PORT = 4444

# AF_INET indica che stiamo usando IPv4, SOCK_STREAM indica che stiamo usando TCP
# SOK_STREAM è un tipo di socket che fornisce un flusso di dati affidabile, ordinato e senza errori.

# Create a socket object ovvero lo inizializziamo 
s = so.socket(so.AF_INET, so.SOCK_STREAM)

# ora dobbiamo configurare il socket e di mettersi in ascolto sulla porta 4444

s.bind((SRV_ADDR, SRV_PORT)) 

# ora spiego quenite connesioni piu accettare prima di rifiutarle
s.listen(1)

# ora madiamo un messaggio di attesa per il client
print(f"[*] Listening on {SRV_ADDR}:{SRV_PORT}")
print("[*] Waiting for incoming connections...")

# ora accettiamo la connessione in arrivo
# --> accept() è un metodo che accetta una connessione in arrivo e restituisce un nuovo socket e l'indirizzo del client. 
# Il nuovo socket viene utilizzato per comunicare con il client, mentre il socket originale continua ad ascoltare per altre connessioni in arrivo.
connection, address = s.accept()
print("conesso con: ", address)

# ora avviamo un ciclo infinito per ricevere i comandi dal client
while True:
    connection.sendall(b"Shell> ") # inviamo un prompt al client
    data = connection.recv(1024) # riceviamo il comando dal client
    if not data:
        break # se non riceviamo dati, usciamo dal ciclo
    print(data.decode("utf-8")) # stampiamo il comando ricevuto
    
    # se esce dal ciclo significa che il client si è disconnesso, quindi chiudiamo la connessione
connection.close()
    