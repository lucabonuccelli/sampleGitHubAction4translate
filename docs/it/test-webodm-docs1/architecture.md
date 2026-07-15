---

titolo: Architettura
modello: doc
---


[WebODM](https://github.com/WebODM/WebODM) è composto da diversi componenti.

- [ODX](https://github.com/WebODM/ODX) è un toolkit da riga di comando che elabora immagini aeree. Gli utenti che si sentono a proprio agio con la riga di comando probabilmente sono d'accordo nell'utilizzare solo questo componente.
- [NodeODX](https://github.com/WebODM/NodeODX) è un'interfaccia leggera e un'API (Application Program Interface) costruita direttamente su [ODX](https://github.com/WebODM/ODX). Gli utenti che non si sentono a proprio agio con la riga di comando possono utilizzare questa interfaccia per elaborare immagini aeree e gli sviluppatori possono utilizzare l'API per creare applicazioni. Non sono fornite funzionalità come l'autenticazione dell'utente, la visualizzazione delle mappe, ecc.
- [WebODM](https://github.com/WebODM/WebODM) aggiunge ulteriori funzionalità come l'autenticazione dell'utente, la visualizzazione di mappe, visualizzazioni 3D, un'API di livello superiore e la capacità di orchestrare più nodi di elaborazione (eseguire lavori in parallelo). I nodi di elaborazione sono semplicemente server che eseguono [NodeODX](https://github.com/WebODM/NodeODX).

![webodm](https://cloud.githubusercontent.com/assets/1951843/25567386/5aeec7aa-2dba-11e7-9169-aca97b70db79.png)

WebODM è costruito pensando alla scalabilità e alle prestazioni. Sebbene la configurazione predefinita collochi tutti i database e le applicazioni sullo stesso computer, gli utenti possono separarne i componenti per migliorare le prestazioni (ad esempio posizionare un lavoratore Celery su un computer separato per eseguire attività in background).

![Architettura](https://user-images.githubusercontent.com/1951843/36916884-3a269a7a-1e23-11e8-997a-a57cd6ca7950.png)

Alcune cose da notare:
* Utilizziamo i lavoratori Celery per eseguire attività in background come il ridimensionamento delle immagini e l'elaborazione dei risultati delle attività, ma utilizziamo un meccanismo di pianificazione ad hoc per comunicare con NodeODX (che elabora le ortofoto, i modelli 3D, ecc.). La scelta di utilizzare due sistemi separati per la pianificazione delle attività è dovuta alla flessibilità che un meccanismo ad hoc ci offre per determinate operazioni (acquisizione dell'output delle attività, dati persistenti e possibilità di riavviare le attività a metà, comunicazione tramite chiamate REST, ecc.).
* Se caricati su più macchine, i lavoratori di Celery dovrebbero tutti condividere la propria directory "app/media" con l'applicazione Django (tramite condivisioni di rete). Puoi gestire i lavoratori tramite `./worker.sh`