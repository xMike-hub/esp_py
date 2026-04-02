# 📝 Appunti e Riassunto: Build Week 1 - Progetto Compagnia Theta

Questi appunti riassumono i requisiti e gli obiettivi presentati nel PDF per la "Build Week - Progetto" di Epicode.

## 🏢 1. Panoramica e Scenario
Siamo stati ingaggiati dalla **Compagnia Theta** per sviluppare il progetto concettuale, l'infrastruttura di rete e un preventivo di spesa per un edificio di **6 piani**.

## 💻 2. Requisiti Hardware (Dispositivi)
*   **Computer (Host):** 20 PC per ogni piano (Totale: 120 computer).
*   **Switch:** 1 switch dedicato per ogni piano (i 20 PC vi saranno collegati).
*   **Router centrale:** 1 router a cui collegare tutti gli switch dei piani.
*   **Firewall:** 1 firewall perimetrale (da posizionare tra il router e Internet).
*   **NAS (Storage):** 1 NAS (collegato allo switch del piano terra per essere accessibile a tutti).
*   **IDS/IPS:** 3 sistemi di rilevamento/prevenzione intrusioni sul perimetro interno.
*   **Web Server:** 1 server (simulato tramite DVWA sulla macchina vulnerabile *Metasploitable 2*).

## 🏗️ 3. Architettura Organizzativa
*   **Rete Interna:** Gli switch raccolgono il traffico dei PC e vanno verso il router. Gli IDS/IPS monitorano questo perimetro.
*   **DMZ (Zona Demilitarizzata):** Il Web Server (Metasploitable) andrà posizionato in questa zona protetta, logicamente tra la rete Internet e il firewall (o in una sua porta dedicata), in modo da essere esposto su Internet in maniere sicura senza compromettere la rete LAN interna.

## 🐍 4. Sviluppo Tool in Python & Testing
Oltre al design dell'infrastruttura, il progetto richiede di programmare dei tool di sicurezza in **Python** per eseguire la verifica attiva del server:

1.  **Verifica Verbi HTTP (HTTP Methods):**
    *   Sviluppare uno script Python in grado di inviare richieste (GET, POST, PUT, DELETE) per determinare quali metodi sono abilitati su determinati percorsi del web server.
    *   *Nota operativa:* Utilizzare l'applicativo `phpMyAdmin` sulla porta 80 della Metasploitable per il test. Lo script prende in input un percorso/URL e resistuisce la lista dei metodi permessi.
2.  **Scansione Porte (Port Scanner):**
    *   Sviluppare un *port scanner* custom in Python.
    *   Il tool prende un IP e un range di porte in input.
    *   L'output dovrà restituire la lista delle porte specificando il loro stato (aperta / chiusa).

## 📄 5. Report Finale
Va consegnato un file di reportistica che includa:
*   La documentazione generata dai tool sui verbi HTTP.
*   L'elenco dei risultati e delle porte analizzate con commenti sulla sicurezza e l'accessibilità.

## ⭐ BONUS (Opzionali per la Lode)
1.  **Subnetting:** Applicare il calcolo VLSM/Subnetting per suddividere razionalmente gli indirizzi IP della rete aziendale.
2.  **Sniffing (Socket):** Sviluppare uno script Python aggiuntivo per usare i socket di rete atti a catturare/sniffare i pacchetti.
