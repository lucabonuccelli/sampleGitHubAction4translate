---

titolo: Contribuire
modello: doc
---


Dare un contributo al codice potrebbe sembrare intimidatorio, ma non è troppo difficile:

1. Crea un fork del [repository WebODM](https://github.com/WebODM/WebODM/)
2. Clona il tuo repository in una directory
3. Crea un nuovo ramo: `git checkout -b branchname`.
4. [Configura un ambiente di sviluppo](#setup-a-development-environment) con docker.
5. Effettua il commit delle modifiche: `git commit -a -m "descrivi le tue modifiche"`
6. Invia le modifiche al tuo repository: `git push origin branchname`
7. Crea una [richiesta pull](https://github.com/WebODM/WebODM/compare)

Non abbiamo molte regole. Segui le linee guida indicate nel documento [Contribuire](https://github.com/WebODM/WebODM/blob/master/CONTRIBUTING.md), sii gentile con gli altri e andrai alla grande! :)

## Configura un ambiente di sviluppo

Segui le [Istruzioni per l'installazione del docker WebODM](https://github.com/WebODM/WebODM/#manual-installation-docker), quindi esegui:

`./webodm.sh avvia --dev`

Questo è tutto! È possibile modificare qualsiasi file, inclusi i file SASS e React.js. Le modifiche si rifletteranno automaticamente nell'istanza WebODM in esecuzione.

## Esegui test unitari

Riteniamo che i test siano una parte necessaria per fornire un software robusto. Cerchiamo di ottenere una copertura completa dei test per il codice backend e come minimo un robusto smoke testing per il codice frontend.

Per eseguire i test unitari, è sufficiente digitare:

`./webodm.sh prova`

## Applica modifiche alla produzione

Una volta terminate le modifiche, se avvii WebODM in modalità produzione (senza il flag `--dev`), noterai che le modifiche mancano. Questo perché "webodm.sh" utilizza l'immagine docker "webodm/webodm_webapp" per avviare WebODM, che non contiene le modifiche apportate. Per applicare le modifiche, è necessario ricostruire localmente l'immagine della finestra mobile:

`docker build -t webodm/webodm_webapp .`

Puoi anche modificare il file `docker-compose.yml` per puntare a un'immagine diversa.

## Panoramica del progetto

### Backend

Il backend si basa principalmente su [Django](https://www.djangoproject.com/) e [Django REST Framework](http://www.django-rest-framework.org/).

Non utilizziamo gran parte del sistema di template di Django, ad eccezione delle sezioni "Amministrazione" e "Nodi di elaborazione". Utilizziamo invece Django per esporre un'[API](/api/task/), che poi leghiamo a un'app [React.js](https://facebook.github.io/react/).

Le directory di interesse sono elencate come segue:

Elenco | Descrizione
--------- | -----------

"/app" | Applicazione principale, include componenti dell'interfaccia utente, API, test e logica di backend.
`/nodeodx`| Applicazione che collega la comunicazione tra WebODM e [NodeODX](https://github.com/WebODM/NodeODX). Include i propri test unitari e modelli.
`/webodm` | La directory principale del progetto di Django. I file di impostazione sono qui.

### Fine frontale

Utilizziamo un'app [React.js](https://facebook.github.io/react/) (sintassi [ES6](https://leanpub.com/understandinges6/read/)) e [SCSS](http://sass-lang.com/) per vari componenti dell'interfaccia utente come il dashboard. Usiamo [webpack](https://webpack.github.io/) per creare componenti intermedi in un bundle statico.

Le directory di interesse sono elencate come segue:

Elenco | Descrizione
--------- | -----------

`/app/modelli/app` | Posizione dei modelli Django. Anche se non li usiamo molto, li usiamo per alcune pagine e come collante per avviare il codice React.
`/app/static/app/js` | Posizione dei file Javascript per tutti i componenti dell'interfaccia utente.
`/app/static/app/js/components` | Cerchiamo di separare i componenti per la riutilizzabilità in vari componenti React. Ogni componente è memorizzato qui.
`/app/static/app/js/css` | Ogni componente dovrebbe avere il proprio file SCSS. Quei file sono archiviati qui.

"/app/static/app/js/main.jsx" è il punto di ingresso per l'interfaccia utente. Se ti chiedi come colleghiamo Django e React.js, questo è il file da guardare per iniziare la ricerca.

### Documentazione

Usiamo [Astro](https://astro.build) per generare la nostra documentazione. Consulta la [documentazione](https://docs.astro.build/en/getting-started/) del progetto per informazioni su come apportare modifiche alla documentazione.

