# 🎭 Riassunto Completo: Social Engineering & Minacce AI-Powered

> [!NOTE]
> Riassunto dell'unità didattica relativa all'Ingegneria Sociale e minacce moderne.

## 🧠 1. Fondamenti dell'Ingegneria Sociale

- **Definizione:** L'Ingegneria Sociale è l'arte di manipolare le persone affinché compiano azioni o rivelino informazioni confidenziali.
- **L'Approccio Psicologico:** Non si tratta di hacking tecnico, ma di psicologia applicata. L'attaccante non forza un sistema, ma *convince una persona ad aprirgli la porta*.
- **I 6 Principi di Cialdini:** Sono la base scientifica di ogni attacco e includono: *Reciprocità, Impegno e Coerenza, Riprova Sociale, Simpatia, Autorità* e *Scarsità (Urgenza)*.
- **Tecniche Classiche:** 
  - 📧 **Phishing / Spear Phishing:** Attacchi via email (generici o mirati).
  - ☎️ **Vishing / Smishing:** Attacchi via telefono (Voice) o tramite SMS.
  - 💽 **Baiting:** Uso di un'esca fisica, come una chiavetta USB abbandonata o recapitata via posta.
  - 🚶 **Tailgating:** Seguire una persona autorizzata per superare un varco fisico delimitato.
  - 🎭 **Pretexting:** Creazione di uno scenario fittizio credibile per ingannare la vittima.
- **Consent Phishing:** Invece di richiedere le credenziali o la password, l'attaccante richiede l'autorizzazione a un'applicazione malevola. In questo modo riceve un *token di sessione* che gli garantisce l'accesso ai dati, bypassando completamente un eventuale MFA (Autenticazione a Due Fattori).

## 🤖 2. La Rivoluzione dell'AI (AI-Driven Threats)

- **Phishing Perfetto e Scalabile:** Grazie ai LLM (Large Language Models), gli attaccanti generano messaggi perfetti, senza errori grammaticali in qualsiasi lingua, automatizzando campagne massive e personalizzate tramite i dati raccolti (OSINT).
- **Deepfake:** Contenuti audio o video iperrealistici ma falsi, generati dall'AI tramite le *GAN (Generative Adversarial Networks)*. Il costo e le competenze per creare un deepfake credibile sono drasticamente crollati.
- **Voice Cloning:** Creazione di una replica sintetica della voce di un obiettivo. Ad oggi bastano pochissimi secondi di registrazione audio (estrapolabili facilmente dai social network) per ricreare fedelmente una persona.

> [!WARNING]
> Con la diffusione dell'Intelligenza Artificiale Generativa, consigliare agli utenti di riconoscere le frodi semplicemente prestando "attenzione agli errori di battitura" non è più una difesa sufficiente.

## 🛡️ 3. Difese Email (Autenticazione)

Il protocollo base della posta (SMTP) non prevede l'identificazione certa del mittente. Per difendersi dallo *spoofing* si usano protocolli aggiuntivi per i record DNS:

1. **SPF (Sender Policy Framework):** Un record DNS che "dichiara" quali server o IP sono esplicitamente autorizzati a inviare email per conto di un dominio.
2. **DKIM (DomainKeys Identified Mail):** Una firma crittografica strutturale ai messaggi, inserita nell'header, per garantire l'integrità del contenuto in transito.
3. **DMARC:** Una policy di sicurezza che istruisce i server riceventi su come comportarsi (*none, quarantine, reject*) quando sia l'SPF che il DKIM falliscono l'autenticazione.

> [!CAUTION]
> **I Limiti dei Protocolli:** SPF, DKIM e DMARC non proteggono in alcun modo contro lo *Spoofing del Display Name* (es. vedo scritto "Banca Intesa" ma la mail sotto è diversa) né contro i domini *Look-alike* (es. `rnicrosoft.com` invece di `microsoft.com`, o l'uso di caratteri cirillici).

## 🧰 4. Tool e Simulazioni (Red Teaming)

- **SET (Social Engineering Toolkit):** Strumento open-source dei Penetration Tester integrato in Kali Linux. Ha un famoso modulo, il *Credential Harvester*, che permette di clonare una pagina web di login legittima (es. Google, Facebook) per rubare pass e sessioni.
- **Gophish:** Piattaforma fra le più usate per l'education e l'invio simulato di campagne di Phishing Awareness ai dipendenti di un'azienda.

---

## 🛑 Concetti Essenziali e Red Flags

> [!IMPORTANT]
> - **L'Anello Debole:** L'essere umano è - e sarà sempre - il segmento più a rischio (e facile da hackerare) in una catena di sicurezza informatica aziendale.
> - **L'Urgenza (Panic & Rarity):** L'inserimento dell'urgenza o della paura blocca il pensiero critico razionale e obbliga a reagire senza verificare con il reparto IT. È la Red Flag per eccellenza.
> - **Rischi enormi dei Token (Consent Phishing):** L'accesso illegittimo dura virtualmente per sempre o finché l'utente stesso non revoca le autorizzazioni della "falsa" App dalle impostazioni dell'Account Microsoft/Google, poiché la password non è mai stata cambiata.
> - **La Regola d'Oro contro l'AI - Verifica Fuori Banda (Out-of-Band):** Se un dirigente o collega richiede procedure fuori dal normale (es. trasferimento fondi) con una videochiamata (Deepfake) o una telefonata (Voice Cloning), la procedura va **sempre** confermata riagganciando e inviando un SMS, o chiamando indietro sulla linea aziendale canonica.
> - **Linee Guida del Red Teaming:** Durante una simulazione contrattata, vi è il divieto testuale e morale di raccogliere e conservare password reali e di creare pretesti invasivi che danneggino mentalmente le persone.