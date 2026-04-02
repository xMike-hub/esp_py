<div align="center">
  <h1>🐍 Python per Principianti & CyberSecurity</h1>
  <p><i>Una raccolta di appunti pratici, script di rete e materiale teorico per imparare Python da zero, con un forte focus sulla sicurezza informatica.</i></p>

  [![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Progress](https://img.shields.io/badge/Status-Work_in_Progress-brightgreen.svg)](#)
</div>

---

Benvenuto nel mio repository! 👋  
Questo spazio raccoglie il mio percorso di apprendimento. Qui troverai concetti fondamentali di Python affiancati a laboratori pratici dedicati al networking e alla **Cyber Security**.

## 🗺️ Indice dei Contenuti

- [📂 Struttura del Progetto](#-struttura-del-progetto)
- [💻 Moduli Python (Le Basi)](#-moduli-python-le-basi)
- [🛠️ Laboratorio di Sicurezza](#%EF%B8%8F-laboratorio-di-sicurezza)
- [📚 Slide & Teoria (PDF)](#-slide--teoria-pdf)
- [🚀 Come Iniziare](#-come-iniziare)

## 📂 Struttura del Progetto

Ecco la mappa completa di tutto il materiale presente nel repository:

```text
esp_py/
├── 01_basi/                 # Fondamentali (I/O, Variabili, Operatori)
├── 02_strutture_dati/       # Liste, Stringhe e Dizionari
├── 03_controllo_flusso/     # If/Else e Cicli For/While
├── 04_funzioni_e_moduli/    # Organizzazione del codice
├── Appunti-venv/            # 🛠️ LABORATORIO: Script di Security & Network
├── Slide/                   # 📚 TEORIA: Slide PDF del corso Epicode
└── README.md                # 👈 Sei qui
```

## 💻 Moduli Python (Le Basi)

Qui è dove si costruiscono le fondamenta della programmazione in Python.

| 🗂️ Modulo e Argomento | 📝 Script Pratici (Esempi e Appunti) | 🔗 Percorso |
| :--- | :--- | :---: |
| 🟢 **01_basi**<br><sub>*Fondamentali del linguaggio*</sub> | 🔸 [01_input_output.py](./01_basi/01_input_output.py)<br>🔸 [02_variabili.py](./01_basi/02_variabili.py)<br>🔸 [03_operatori.py](./01_basi/03_operatori.py) | [Apri 📂](./01_basi/) |
| 🟡 **02_strutture_dati**<br><sub>*Gestione delle informazioni*</sub> | 🔸 [01_stringhe.py](./02_strutture_dati/01_stringhe.py)<br>🔸 [02_liste.py](./02_strutture_dati/02_liste.py)<br>🔸 [03_dizionari.py](./02_strutture_dati/03_dizionari.py) | [Apri 📂](./02_strutture_dati/) |
| 🔴 **03_controllo_flusso**<br><sub>*Condizioni e cicli interattivi*</sub> | 🔸 [01_condizioni.py](./03_controllo_flusso/01_condizioni.py)<br>🔸 [02_cicli.py](./03_controllo_flusso/02_cicli.py) | [Apri 📂](./03_controllo_flusso/) |
| 🟣 **04_funzioni_e_moduli**<br><sub>*Organizzare il codice*</sub> | 🔸 [m01_funzioni.py](./04_funzioni_e_moduli/m01_funzioni.py)<br>🔸 [m02_moduli_teoria.py](./04_funzioni_e_moduli/m02_moduli_teoria.py)<br>🔸 [m03_moduli_pratica.py](./04_funzioni_e_moduli/m03_moduli_pratica.py) | [Apri 📂](./04_funzioni_e_moduli/) |

## 🛠️ Laboratorio di Sicurezza

Una sezione interamente dedicata all'analisi di rete e ai primi script di ethical hacking.  
📍 **Ambiente isolato nel percorso:** [`/Appunti-venv`](./Appunti-venv/)

| 🛡️ Tool / Script | 🎯 Obiettivo Tecnico | 📜 File Sorgente |
| :--- | :--- | :--- |
| **🔍 Network Scanner** | Scansione avanzata della rete e delle porte aperte | [scanner_draft.py](./Appunti-venv/scanner_draft.py) |
| **🚪 Backdoor** | Bozza di implementazione di una reverse shell/backdoor | [backdoor_draft.py](./Appunti-venv/backdoor_draft.py) |
| **🌐 HTTP Analysis** | Verifiche di sicurezza sui verbi e metodi HTTP permessi | [verbi_http.py](./Appunti-venv/verbi_http.py) |
| **⚙️ Dipendenze** | Librerie e moduli Python necessari per l'esecuzione dei tool | [requirements.txt](./Appunti-venv/requirements.txt) |

## 📚 Slide & Teoria (PDF)

Materiale didattico ufficiale diviso per unità di apprendimento.


| 📚 Unità & Settimana | 📂 Lezioni Mappate (Struttura Cartelle) | 🔗 Link |
| :----------------- | :-------------------------------------- | :----: |
| 📘 **UNIT 1 - S1** | 🔸 [S1-L1_Introduzione_all_Ethical_Hacking](./Slide/UNIT-1/S1/S1-L1_Introduzione_all_Ethical_Hacking/)<br>🔸 [S1-L2_Fondamenti_di_Network_1](./Slide/UNIT-1/S1/S1-L2_Fondamenti_di_Network_1/)<br>🔸 [S1-L3_Fondamenti_di_Network_2](./Slide/UNIT-1/S1/S1-L3_Fondamenti_di_Network_2/)<br>🔸 [S1-L4_Fondamenti_di_Network_3](./Slide/UNIT-1/S1/S1-L4_Fondamenti_di_Network_3/)<br>🔸 [S1-L5_Progetto](./Slide/UNIT-1/S1/S1-L5_Progetto/) | [Apri 📁](./Slide/UNIT-1/S1/) |
| 📘 **UNIT 1 - S2** | 🔸 [S2-L1_Fondamenti_Network _Protocolli](./Slide/UNIT-1/S2/S2-L1_Fondamenti_Network%20_Protocolli/)<br>🔸 [S2-L2_Python-1](./Slide/UNIT-1/S2/S2-L2_Python-1/)<br>🔸 [S2-L3_Python-2](./Slide/UNIT-1/S2/S2-L3_Python-2/)<br>🔸 [S3-L4_Python_&_AI](./Slide/UNIT-1/S2/S3-L4_Python_&_AI/)<br>🔸 [S2-L5_Progetto](./Slide/UNIT-1/S2/S2-L5_Progetto/) | [Apri 📁](./Slide/UNIT-1/S2/) |
| 📘 **UNIT 1 - S3** | 🔸 [S3-L1_Sistemi_Operativi](./Slide/UNIT-1/S3/S3-L1_Sistemi_Operativi/)<br>🔸 [S3-L2_Penetration_Testing_Intro](./Slide/UNIT-1/S3/S3-L2_Penetration_Testing_Intro/)<br>🔸 [S3-L3_Firewall](./Slide/UNIT-1/S3/S3-L3_Firewall/)<br>&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 [Appunti_Firewall.md](./Slide/UNIT-1/S3/S3-L3_Firewall/Appunti_Firewall.md)<br>🔸 [S4-L4_Crittografia](./Slide/UNIT-1/S3/S4-L4_Crittografia/)<br>&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 [Appunti_Crittografia.md](./Slide/UNIT-1/S3/S4-L4_Crittografia/Appunti_Crittografia.md) | [Apri 📁](./Slide/UNIT-1/S3/) |
| 🛠️ **UNIT 1 - BW1** | 🔸 [Build Week 1: Progetto Compagnia Theta](./Slide/UNIT-1/BW-1/)<br>&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 [Appunti_BW1.md](./Slide/UNIT-1/BW-1/Appunti_BW1.md) | [Apri 📁](./Slide/UNIT-1/BW-1/) |
| 📗 **UNIT 2 - S1** | 🔸 [S5-L1_OSINT](./Slide/UNIT-2/S1/S5-L1_OSINT/)<br>&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 [Appunti_OSINT.md](./Slide/UNIT-2/S1/S5-L1_OSINT/Appunti_OSINT.md)<br>🔸 [S5-L2_Social_Engineering](./Slide/UNIT-2/S1/S5-L2_Social_Engineering/)<br>&nbsp;&nbsp;&nbsp;&nbsp;↳ 📄 [Social_Engineering.md](./Slide/UNIT-2/S1/S5-L2_Social_Engineering/Social_Engineering.md) | [Apri 📁](./Slide/UNIT-2/S1/) |

## 🚀 Come Iniziare

Ecco i passaggi per replicare il laboratorio sul tuo computer:

1. **Clona il Repository**
   ```bash
   git clone https://github.com/tuo-username/esp_py.git
   cd esp_py
   ```

2. **Configura l'Ambiente di Rete / Security (Opzionale)**
   ```bash
   # Spostati nell'area di sicurezza e installa i requisiti (es. requests, moduli vari)
   cd Appunti-venv
   pip install -r requirements.txt
   ```

3. **Esegui e Testa il Codice**
   ```bash
   # Esegui i tuoi primi appunti dalla root del progetto
   python 01_basi/01_input_output.py
   ```

---
> 🌱 **Work in Progress:** Questo repository è "vivo" ed è in continuo aggiornamento man mano che avanzo nel mio percorso di studio come Ethical Hacker e Sviluppatore Python! ✨
