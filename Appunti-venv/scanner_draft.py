import socket as so 

target = input("Enter the target IP address: ")
# Correzione: rimosso "int()" perché "5-200" è una stringa con un trattino, non un numero!
prtran = input("Enter the target port (es 5-200): ")

# scoppiare il range di porte in due variabili high_port e low_port
low_port = int(prtran.split("-")[0]) # type: ignore
high_port = int(prtran.split("-")[1]) # type: ignore

# ora dobbiamo scorrere tutte le porte tra low_port e high_port e verificare se sono aperte o chiuse
print(f"Scanning {target} for open ports between {low_port} and {high_port}...")

for port in range(low_port, high_port + 1):
    # configuriamo il socket per connettersi al target e alla porta specificata
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    
    # abiamo un timaout di 1 secondo per evitare di aspettare troppo a lungo se la porta è chiusa
    # Correzione: scommentato e spostato QUI prima di connettersi
    s.settimeout(1)
    
    status = s.connect_ex((target, port)) # connect_ex() è un metodo che tenta di connettersi al target e alla porta specificata e restituisce 0 se la connessione è riuscita, altrimenti restituisce un codice di errore.
    
    # Correzione: sistemata l'indentazione (gli spazi) per allinearla a "status ="
    if status == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
        
    # Correzione: aggiungiamo s.close() per pulire il socket ad ogni tentativo
    s.close()