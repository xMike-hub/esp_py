# 🕵️ Appunti e Riassunto: OSINT & AI-Driven Reconnaissance

Questo documento riassume i concetti chiave presentati nelle slide "OSINT e AI-Driven Reconnaissance" di Epicode.

## 🔍 Parte 1: Introduzione all'OSINT
*   **Definizione:** **OSINT (Open Source Intelligence)** è la raccolta e l'analisi di informazioni da fonti pubblicamente accessibili (social media, registri DNS, motori di ricerca, Shodan, articoli, ecc.).
*   **Information Gathering:** È la fase di ricognizione (Reconnaissance). Si divide in:
    *   **Passive Recon:** Non si tocca direttamente il target (es. leggere il sito aziendale, Whois). È furtiva e legale.
    *   **Active Recon:** Si interagisce con i sistemi del bersaglio (es. scansione porte). Genera allarmi nei log e richiede un'autorizzazione scritta ("Regole d'Ingaggio" / RoE).
*   **Limiti Legali:** Accesso abusivo o intercettazione non autorizzata violano articoli penali (es. Art. 615-ter in Italia, GDPR in Europa). Se lavoriamo su target reali serve sempre il **consenso esplicito** e documentato. Qualunque cosa trovata esposta va segnalata eticamente (Responsible Disclosure).

## 🔎 Parte 2: Tecniche di Ricerca e Tool (Google Dorking e DNS)
*   **Google Dorking:** L'uso di operatori di ricerca avanzati (Dorks) per scoprire pannelli vulnerabili, documenti riservati e credenziali.
    *   *Operatori utili:* `site:` (cerca in un dominio), `filetype:` (cerca estensioni, es. pdf o env), `intitle:` (cerca parole nel titolo), `inurl:` (cerca nell'url), `-` (esclude parole).
*   **DNS Reconnaissance:** Si studiano i record DNS (A per gli IP, MX per la posta, NS per chi gestisce il DNS, TXT per configurazioni varie).
    *   Strumenti come **WHOIS** rivelano chi ha registrato il dominio.
*   **Subdomain Enumeration:** Scoprire i sottodomini (spesso usati per staging, backoffice o dimenticati) che hanno falle di sicurezza usando tool come *Sublist3r, Amass o DNSDumpster*.

## 🛠️ Parte 3: I Grandi Tool dell'OSINT
*   **theHarvester:** Strumento da riga di comando preinstallato in Kali Linux per trovare email, sottodomini, IP e nomi dipendenti interrogando più fonti (Google, LinkedIn, ecc.).
*   **Recon-ng:** Framework modulare per l'OSINT, scritto in Python. Simile a Metasploit, utilizza "moduli" e richiede di configurare chiavi API (es. *hackertarget*, *shodan*) per analizzare domini, email o contatti.
*   **Shodan:** Il "motore di ricerca per hacker". Non cerca pagine web ma i veri e propri dispositivi fisici connessi a internet (webcam, router SCADA, database aperti). Indica banner, porte, sistemi operativi vulnerabili.
*   **Maltego:** Un potentissimo tool visuale (GUI). Usa dei "Transformer" per estrarre le relazioni fra le *entità* (es. da un Domain ricava l'IP, poi i DNS, poi le email) creando spettacolari **grafi a nodi**.
*   **Have I Been Pwned (HIBP):** Servizio indispensabile per capire se una casella email data è finita in un "Data Breach" (un furto di dati pubblici).

## 🤖 Parte 4: AI e Automazione
*   Il vero problema dell'OSINT oggi è elaborare enormi quantità di "falsi positivi" estratti dai tools automatici. 
*   **L'Intelligenza Artificiale (LLM come Gemini, ChatGPT, Llama)** supporta l'analista filtrando e normalizzando i dati testuali non strutturati.
*   *Scripting Python:* Si può collegare uno strumento come *theHarvester* a Python e mandare l'output grezzo (JSON) all'API di Gemini perché estragga le "vulnerabilità più critiche" organizzate in una tabella o report.
*   **Allucinazioni:** L'AI non è esente da difetti. Può inventare dei risultati (allucinazione). L'analista umano serve SEMPRE per validare ogni singola analisi. Se l'informazione è critica e sensibile, conviene installare un LLM locale offline su Kali (es. via Ollama).

## 🛡️ Parte 5: Mitre ATT&CK e Workflow
*   L'OSINT rientra nella tattica **TA0043 (Reconnaissance)** del framework MITRE.
*   Il ciclo corretto di OSINT: 
    1. Pianificazione ed emissione Regole d'Ingaggio.
    2. Raccolta Passiva (Whois, Dorking, Shodan).
    3. Organizzazione e Aggregazione (Database, Maltego).
    4. Analisi e Correlazione (LLM/AI, Profilazione).
    5. Creazione del Report.

---

# 🛑 LE COSE PIÙ IMPORTANTI DA RICORDARE (SINTESI)

Per rendere più facile la memorizzazione, ecco i concetti absolutamenti fondamentali dalle slide:

1. **Passive vs Active Reconnaissance:** Se fai "Passive Recon" (Google, Shodan, WhoIs) stai solo leggendo cataloghi internet pubblici. Se fai "Active Recon" stai toccando le porte del cliente. **Senza contratto scritto formale, NON TOCCARE MAI attivamente i sistemi altrui.**
2. **"Google Dorking" trova gli scheletri nell'armadio:** Qualsiasi dipendente può dimenticare file sensibili o interi database (file `.env` o file `.sql`) esposti pubblicamente. Usare termini di ricerca intelligenti svela grandissime vulnerabilità senza usare nessun codice malevolo.
3. **Automazione ed Eccesso di informazioni:** Saper lanciare un tool da terminale (come theHarvester o recon-ng) è facile, il difficile è gestire 200 milioni di righe di testo inquinato. L'analista bravo deve scremare le bugie dalla verità.
4. **LLM come Copiloti (Non Piloti):** Le intelligenze artificiali velocizzano la lettura dei referti e l'interpolazione logica, ma "hanno le allucinazioni" (inventano cose che non esistono). Quindi, l'investigatore *valida sempre empiricamente* i fatti estratti dall'AI.
5. **Documenta Tutto (Best Practice):** Salva ed esporta i risultati dei tool. Fai registrazioni storiche, appunta gli step su file di report, perché la validità legale di una verifica di sicurezza passa da un report curato. Non usare le mail del cliente in theHarvester o Shodan per giocarci!
