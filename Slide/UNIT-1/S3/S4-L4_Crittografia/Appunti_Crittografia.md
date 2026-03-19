# 🔐 Guida Semplice alla Crittografia

*Riassunto completo basato sulle slide del modulo "Cyber Security & Ethical Hacking"*

Benvenuto! Questo documento è pensato per spiegare i concetti complessi della crittografia in modo chiaro e comprensibile, anche se non sei un programmatore.

## 📍 Indice

1. [Cosa significa fare Crittografia?](#1-cosa-significa-fare-crittografia)
2. [I 4 Pilastri della Sicurezza](#2-i-4-pilastri-della-sicurezza)
3. [Crittografia Simmetrica (Una sola chiave)](#3-crittografia-simmetrica-una-sola-chiave)
4. [Crittografia Asimmetrica (Due chiavi)](#4-crittografia-asimmetrica-due-chiavi)
5. [La Firma Digitale](#5-la-firma-digitale)
6. [Certificati Digitali e Autorità (CA)](#6-certificati-digitali-e-autorità-ca)
7. [Crittografia in Rete: TLS e SSL](#7-crittografia-in-rete-tls-e-ssl)
8. [Steganografia: L'arte di nascondere](#8-steganografia-larte-di-nascondere)

## 1. Cosa significa fare Crittografia?

La crittografia è l'arte di trasformare un messaggio leggibile (**Testo in Chiaro** o *Plaintext*) in un messaggio incomprensibile (**Crittotesto** o *Ciphertext*).

* **Cifratura:** Il processo che "chiude" il messaggio.
* **Decifratura:** Il processo che "apre" il messaggio per tornare all'originale.

**Un po' di storia:** Il metodo più antico è il **Cifrario di Cesare**, dove ogni lettera veniva spostata di 3 posizioni nell'alfabeto (es. la A diventa D). Oggi usiamo algoritmi matematici molto più complessi.

## 2. I 4 Pilastri della Sicurezza

Perché usiamo la crittografia? Per garantire quattro cose fondamentali:

1. **Riservatezza (Confidentiality):** Solo chi è autorizzato può leggere il messaggio.
2. **Integrità (Integrity):** Il messaggio non è stato modificato durante il viaggio.
3. **Autenticazione (Authentication):** Siamo sicuri di chi ha inviato il messaggio.
4. **Non ripudio (Non-repudiation):** Chi invia il messaggio non può negare di averlo fatto.

## 3. Crittografia Simmetrica (Una sola chiave)

Immagina una cassaforte che si apre e si chiude con **la stessa identica chiave**.

* **Vantaggio:** È molto veloce.
* **Svantaggio:** Il problema è: come facciamo a scambiarci la chiave in modo sicuro? Se qualcuno la ruba mentre te la sto portando, potrà leggere tutti i messaggi.
* **Esempi:** AES (usato per proteggere i file sul tuo PC o i messaggi WhatsApp).

## 4. Crittografia Asimmetrica (Due chiavi)

Questa è la vera rivoluzione. Ogni persona ha **due chiavi** collegate matematicamente:

1. **Chiave Pubblica:** Puoi darla a chiunque (come il tuo indirizzo di casa). Serve per **chiudere** il messaggio.
2. **Chiave Privata:** Devi tenerla segreta. Serve per **aprire** i messaggi chiusi con la tua chiave pubblica.

*Analogia:* Chiunque può mettere una lettera nella tua cassetta della posta (chiave pubblica), ma solo tu hai la chiave per aprirla (chiave privata).

* **Vantaggio:** Non dobbiamo scambiarci chiavi segrete.
* **Esempi:** RSA, ECC.

## 5. La Firma Digitale

Non serve per nascondere il messaggio, ma per garantire che sia **autentico**.
Funziona al contrario: io "firmo" un riassunto del messaggio (chiamato *Hash*) usando la mia **chiave privata**. Tu puoi verificare la firma usando la mia **chiave pubblica**. Se la verifica ha successo, sappiamo che il messaggio è mio e non è stato toccato.

## 6. Certificati Digitali e Autorità (CA)

Come facciamo a sapere che la chiave pubblica di "SitoBanca.it" appartiene davvero alla banca e non a un truffatore?
Entrano in gioco le **Autorità di Certificazione (CA)**. Sono enti fidati che emettono un "Certificato Digitale" (una sorta di carta d'identità elettronica) che garantisce l'identità del proprietario della chiave.

## 7. Crittografia in Rete: TLS e SSL

Quando vedi il **lucchetto** sul browser (HTTPS), stai usando il protocollo TLS/SSL.
È un sistema "misto":

1. Si usa la **Crittografia Asimmetrica** per conoscersi e scambiarsi una chiave segreta in modo sicuro.
2. Una volta stabilita la connessione, si passa alla **Crittografia Simmetrica** perché è più veloce per scambiare i dati del sito.

## 8. Steganografia: L'arte di nascondere

A differenza della crittografia (che rende il messaggio illeggibile), la steganografia **nasconde l'esistenza stessa** del messaggio.

* *Esempio:* Inserire un testo segreto dentro i pixel di una foto di un gattino. Chi guarda vede solo la foto, ma dentro ci sono dati nascosti.

*Documento creato per Chris - Appunti Epicode*
