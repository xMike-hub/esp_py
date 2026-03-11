# Importiamo la libreria integrata in Python per comunicare con i server web (protocollo HTTP)
import http.client 

# ==========================================
# 1. ACQUISIZIONE DATI DAL TERMINALE
# ==========================================
# Chiediamo all'utente l'indirizzo del bersaglio (es. 192.168.1.50 o www.sito.com)
host = input("Enter the host to scan: ")

# Chiediamo la porta, ma lasciamo l'input come testo per poter gestire il caso in cui l'utente prema solo Invio
port_input = input("Enter the port to scan (premi Invio per la porta 80): ")

# ==========================================
# 2. GESTIONE DELLA PORTA DI DEFAULT
# ==========================================
# Se l'utente preme solo Invio, la stringa sarà vuota ("")
if port_input == "":
    port = 80  # Impostiamo la porta 80, che è quella standard per il traffico web (HTTP)
else:
    port = int(port_input) # Altrimenti, convertiamo ciò che ha scritto in un numero intero (int)

# ==========================================
# 3. TENTATIVO DI CONNESSIONE AL SERVER
# ==========================================
# Usiamo il blocco try/except in modo che, se il server è irraggiungibile, lo script non vada in crash
try:
    # Creiamo la connessione specificando host, porta e un limite di tempo (timeout) di 5 secondi
    conn = http.client.HTTPConnection(host, port, timeout=5)
    
    # Inviamo la richiesta "OPTIONS" alla directory principale del server ("/").
    # Questo metodo serve proprio a chiedere: "Quali azioni mi permetti di fare su questa pagina?"
    #conn.request("OPTIONS", "/")
    conn.request("OPTIONS", "/dav/") 
    
    # Aspettiamo e memorizziamo la risposta ricevuta dal server
    response = conn.getresponse()
    
    # Stampiamo a schermo che la connessione è riuscita e il codice di stato (es. 200 OK, 403 Forbidden)
    print(f"\n[+] Connesso a {host} sulla porta {port}.")
    print(f"[i] Status HTTP restituito: {response.status}")
    
    # ==========================================
    # 4. ESTRAZIONE DEI VERBI HTTP
    # ==========================================
    # I server rispondono inviando informazioni nascoste chiamate "header". 
    # Noi cerchiamo lo specifico header "Allow", che contiene la lista dei verbi consentiti.
    allowed_methods = response.getheader("Allow")
    
    # ==========================================
    # 5. STAMPA DEL RISULTATO
    # ==========================================
    if allowed_methods:
        # Se il server ha risposto con l'header "Allow", stampiamo la lista (es. GET, POST, OPTIONS)
        print(f"[*] Verbi HTTP supportati: {allowed_methods}")
    else:
        # Se l'header manca (spesso i server lo rimuovono per sicurezza per non dare info agli hacker)
        print("[-] Il server non ha dichiarato i verbi (l'header 'Allow' è vuoto o nascosto).")
    
    # Chiudiamo la connessione per liberare le risorse del computer
    conn.close()

# ==========================================
# 6. GESTIONE DEGLI ERRORI (EXCEPT)
# ==========================================
# Se qualcosa va storto (porta chiusa, connessione assente, IP errato), il programma salta direttamente qui
except Exception as e:
    print(f"[-] Impossibile connettersi o errore su {host}:{port}. Dettaglio: {e}")