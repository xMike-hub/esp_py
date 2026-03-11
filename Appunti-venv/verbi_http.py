import http.client 

host = input("Enter the host to scan: ")
# 1. Lasciamo l'input come testo per ora
port_input = input("Enter the port to scan (premi Invio per la porta 80): ")

# 2. Controlliamo SE è vuoto PRIMA di trasformarlo in numero
if port_input == "":
    port = 80  # Imposta la porta predefinita
else:
    port = int(port_input) # Se ha scritto qualcosa, trasformiamolo in numero

try:
    # Creo una connessione HTTP al host e alla porta specificati
    conn = http.client.HTTPConnection(host, port, timeout=5)
    conn.request("HEAD", "/")  # Invia una richiesta HEAD per verificare se il server risponde
    response = conn.getresponse()
    
    # Se riceviamo una risposta, la porta è aperta e il server web funziona!
    # Ho aggiunto anche lo status code (es. 200 OK, 403 Forbidden)
    print(f"[+] Port {port} is open on {host}. Status HTTP: {response.status}")
    
    # Chiudiamo la connessione
    conn.close()

except Exception as e:
    # 3. Ecco l'except! Se la connessione fallisce o la porta è chiusa, finisce qui.
    print(f"[-] Port {port} is closed or non-HTTP on {host}. Dettaglio errore: {e}")