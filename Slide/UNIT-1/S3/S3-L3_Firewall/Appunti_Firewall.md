# 🛡️ Appunti Dettagliati di Cyber Security: Firewall, IDS/IPS e Segmentazione

Questi appunti coprono in modo approfondito i concetti di difesa perimetrale e analisi del traffico di rete, strutturati per lo studio professionale dell'Ethical Hacking.


## 📌 Indice degli Argomenti

1. [Introduzione e Scopo del Firewall](#1-introduzione-e-scopo-del-firewall)
2. [I Componenti del Firewall](#2-i-componenti-del-firewall)
3. [Tipi di Filtraggio del Traffico](#3-tipi-di-filtraggio-del-traffico)
4. [Logica e Gestione delle Regole (Policy)](#4-logica-e-gestione-delle-regole-policy)
5. [Firewall di Prossima Generazione (NGFW) e Classificazioni](#5-firewall-di-prossima-generazione-ngfw-e-classificazioni)
6. [IDS e IPS: Intrusion Detection & Prevention System](#6-ids-e-ips-intrusion-detection--prevention-system)
7. [Tecniche di Rilevamento: Pattern vs Anomaly](#7-tecniche-di-rilevamento-pattern-vs-anomaly)
8. [Segmentazione della Rete (DMZ e Intranet)](#8-segmentazione-della-rete-dmz-e-intranet)
9. [Strumenti Pratici: iptables e pfSense](#9-strumenti-pratici-iptables-e-pfsense)

## 1. Introduzione e Scopo del Firewall 🧱

Un **firewall** è un dispositivo hardware o software progettato per proteggere una rete informatica (o un singolo computer) da minacce esterne. Funge da "guardiano" tra la rete interna sicura e il mondo esterno (es. Internet).

**Perché lo studiamo?**

1. **Protezione della rete:** Blocca accessi non autorizzati.
2. **Prevenzione degli attacchi:** Rileva e ferma minacce prima che entrino.
3. **Gestione del traffico:** Controlla e indirizza i flussi di dati.
4. **Conformità:** Aiuta a rispettare le normative sulla sicurezza dei dati.

## 2. I Componenti del Firewall ⚙️

Un firewall opera attraverso la sinergia di tre componenti principali:

* **Motore di ispezione del traffico:** È il cuore del sistema. Analizza il traffico di rete basandosi sulle regole configurate. Controlla intestazioni (IP, porte) e, nei modelli avanzati, anche il contenuto dei pacchetti (Deep Packet Inspection - DPI).
* **Interfaccia di gestione:** Il pannello di controllo (spesso web-based) dove gli amministratori configurano il firewall, monitorano il traffico in tempo reale e leggono i report/log.
* **Database delle Regole:** La memoria dove risiedono le policy di sicurezza. È qui che il motore di ispezione cerca le istruzioni su cosa fare con ogni singolo pacchetto dati.

## 3. Tipi di Filtraggio del Traffico 🔍

Il firewall decide se far passare un pacchetto attraverso diverse tecnologie:

### A. Filtraggio Statico (Packet Filtering)

Valuta ogni pacchetto singolarmente basandosi unicamente sulle informazioni presenti nell'intestazione: Indirizzo IP (sorgente/destinazione), Porta e Protocollo.

* *Esempio:* Regola che blocca tutti i pacchetti provenienti dall'IP 192.168.1.10 sulla porta 80.
* *Pro/Contro:* Molto veloce, ma poco intelligente perché non riconosce il contesto della conversazione.

### B. Filtraggio Dinamico (Stateful Inspection)

Tiene traccia dello **stato delle connessioni attive**. Il firewall crea una "tabella di stato" e registra chi ha iniziato la conversazione.

* *Esempio TCP:* Il firewall verifica lo stato del Three-way Handshake (SYN, SYN-ACK, ACK). Se un pacchetto di risposta (es. dati da un sito web) fa parte di una connessione legittima precedentemente richiesta dalla rete interna, lo lascia passare. Se arriva un pacchetto isolato senza che nessuno lo abbia richiesto, lo blocca.

### C. WAF (Web Application Firewall)

Opera a **livello di applicazione (Livello 7 ISO/OSI)**. È progettato specificamente per proteggere le applicazioni web analizzando il traffico HTTP/HTTPS.

* *Scopo:* Prevenire attacchi come SQL Injection, Cross-Site Scripting (XSS) e caricamento di file malevoli.
* *Scenario d'attacco:* Se un utente tenta di caricare uno script `.php` camuffato tramite un form di upload su un sito, il WAF analizza il payload HTTP e blocca la richiesta.

### D. Proxy Firewall

Agisce da **intermediario** tra il client (nella rete interna) e il server (esterno).

1. **Nasconde l'IP:** Il server esterno vedrà solo l'IP del Proxy, mai quello del client reale.
2. **Filtraggio profondo:** Esegue le richieste "per conto del client", analizzando minuziosamente la risposta prima di inoltrarla.
3. **Caching:** Memorizza le pagine web visitate di frequente per velocizzare le risposte future.
4. **Reverse Proxy:** Fa l'esatto contrario. Sta davanti ai server web di un'azienda per proteggerli dagli utenti esterni, offrendo anche bilanciamento del carico (Load Balancing).

## 4. Logica e Gestione delle Regole (Policy) 📝

Il database delle regole definisce il comportamento del firewall. Il motore di ispezione legge le regole con un approccio **Top-Down (dall'alto verso il basso)**.

**Come funziona il Top-Down?**
Il firewall analizza un pacchetto e inizia a leggere le regole dalla riga 1. Appena trova una regola che fa "match" (che corrisponde a quel traffico), applica l'azione stabilita e **smette di leggere le regole successive**.

* Se nessuna regola viene "matchata", si applica la regola finale di default (solitamente configurata come "Deny All").

**Le Azioni (Action) possibili sui pacchetti:**

* 🟢 **Allow (o Accept):** Il pacchetto è sicuro e viene lasciato passare.
* 🟡 **Drop:** Il pacchetto viene scartato silenziosamente. Il mittente non riceve alcuna notifica (utile per ingannare gli scanner di rete, facendogli credere che la macchina sia spenta).
* 🔴 **Deny (o Reject):** Il pacchetto viene bloccato e il firewall invia un messaggio di errore esplicito al mittente.

## 5. Firewall di Prossima Generazione (NGFW) e Classificazioni 🚀

**NGFW (Next-Generation Firewall):**
Un firewall moderno che unisce le funzionalità classiche a tecnologie avanzate:

* Prevenzione intrusioni (IPS integrato).
* Deep Packet Inspection (DPI) per ispezionare il payload dei pacchetti.
* Antimalware e Web Reputation.
* Gestione VPN.

**Classificazioni Hardware vs Software:**

* **Hardware:** Dispositivi dedicati (appliance fisiche).
* **Software:** Installati su sistemi operativi comuni o macchine virtuali.

**Perimetrali vs Host:**

* **Perimetrali:** Posizionati ai confini della rete aziendale per proteggere l'intero perimetro.
* **Host-based:** Installati sul singolo PC/Server (es. Windows Defender Firewall) per gestire il traffico interno o limitare i danni se la rete perimetrale viene violata.

## 6. IDS e IPS: Intrusion Detection & Prevention System 🕵️‍♂️🛡️

Mentre il firewall basa il blocco su regole statiche o stati, IDS e IPS analizzano il traffico alla ricerca di *comportamenti* malevoli.

### IDS (Intrusion Detection System)

È un sistema **passivo**. Agisce come una telecamera di sorveglianza: se rileva una potenziale minaccia analizzando i log di rete o di sistema, **genera un avviso (alert)** per l'amministratore, ma non blocca attivamente l'attacco.

**Tipologie di IDS:**

* **NIDS (Network-based):** Sensori posizionati su switch o gateway strategici. Monitorano tutto il traffico di rete in transito. Offrono un'ampia copertura ma non vedono cosa succede "dentro" le singole macchine.
* **HIDS (Host-based):** Installato sui singoli dispositivi (server critici, laptop). Monitora attività locali (file log, modifiche di configurazione, processi sospetti in esecuzione).

### IPS (Intrusion Prevention System)

È un sistema **attivo**. Lavora "in-line" (in mezzo al flusso di traffico). Quando rileva una minaccia (es. una sequenza di pacchetti tipica di un attacco DDoS), **blocca immediatamente** la connessione, prima che causi danni. L'unico limite è il rischio di *Falsi Positivi* (bloccare traffico legittimo scambiato per malevolo).



## 7. Tecniche di Rilevamento: Pattern vs Anomaly 🧠

Gli IDS/IPS utilizzano due approcci principali per identificare le minacce:

1. **Pattern Matching (Basato sulle Firme):**

   * *Come funziona:* Come un classico Antivirus. Ha un database di "firme" (sequenze di bit note di malware o exploit, es. stringhe malevole per SQL Injection).
   * *Pro:* Molto preciso per minacce conosciute, pochissimi falsi positivi, veloce.
   * *Contro:* Non rileva attacchi nuovi (Zero-Day) per cui non esiste ancora una firma. Richiede aggiornamenti continui.
2. **Anomaly Detection (Rilevamento delle anomalie):**

   * *Come funziona:* Utilizza il machine learning. Prima crea un profilo del traffico "normale" dell'azienda (fase di addestramento). Successivamente, segnala come minaccia qualsiasi deviazione da questa normalità (es. un picco improvviso di traffico verso un server alle 3 di notte).
   * *Pro:* Può rilevare minacce nuove (sconosciute) ed è adattabile.
   * *Contro:* Alti tassi di Falsi Positivi. Fase di configurazione e addestramento molto complessa.

## 8. Segmentazione della Rete (DMZ e Intranet) 🏗️

La segmentazione è il principio di dividere una rete in diverse "zone" per isolare le risorse critiche e contenere eventuali infezioni (zoning).

* **Intranet (LAN Interna):** Rete altamente sicura. Ospita i PC dei dipendenti. Ha un livello di sicurezza discreto, ma solitamente l'accesso è permesso solo ai dispositivi fidati.
* **DMZ (Demilitarized Zone):** Rete "intermediaria" parzialmente esposta. Se un'azienda ha un proprio Web Server o Server Email (che devono essere accessibili da chiunque su Internet), questi vengono messi nella DMZ. Se un hacker compromette il Web Server, non avrà un accesso diretto alla Intranet aziendale, poiché c'è un ulteriore firewall a proteggerla.
* **Applicativi Critici (Backend):** Rete estremamente restrittiva per Database e dati sensibili, posizionata in un segmento di rete inaccessibile dalla DMZ o dall'esterno senza autorizzazioni fortissime.

## 9. Strumenti Pratici: iptables e pfSense 🛠️

### Iptables (Ambiente Linux)

È lo strumento da riga di comando per eccellenza per la configurazione del firewall su sistemi Linux (es. su Kali Linux). Lavora sulle **Catene (Chains)**:

* `INPUT`: Regole per i pacchetti in entrata (diretti al nostro PC).
* `OUTPUT`: Regole per i pacchetti in uscita.
* `FORWARD`: Regole per pacchetti che transitano (quando il PC fa da router).

*Comando di Esempio:*
`iptables -I INPUT -p tcp --dport 22 -j ACCEPT`

* `-I INPUT`: Inserisci nella catena di input.
* `-p tcp`: Specifica il protocollo TCP.
* `--dport 22`: Porta di destinazione 22 (SSH).
* `-j ACCEPT`: Azione (Jump) -> Accetta la connessione.

### pfSense (Firewall Enterprise Open-Source)

Un potente sistema operativo basato su FreeBSD, ottimizzato per funzionare esclusivamente come firewall/router.

* **Interfaccia:** Completamente gestibile via Browser Web (GUI intuitiva).
* **Installazione tipica (Laboratorio VirtualBox):** Richiede una macchina virtuale con almeno due schede di rete: una per la *WAN* (configurata in Bridge o NAT verso l'esterno) e una per la *LAN* (Rete Interna su cui si affacciano le macchine da proteggere). Una volta avviato, pfSense assegna un indirizzo IP alla LAN (es. 192.168.1.125), al quale ci si può collegare da un browser interno per la configurazione grafica completa (creazione regole, dashboard traffico).

⭐ *Appunti approfonditi strutturati per la comprensione tecnica avanzata in Ethical Hacking.* ⭐
