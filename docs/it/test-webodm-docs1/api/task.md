---

titolo: Compito
modello: doc
---


> Esempio di attività:

```json
{

"id": 134,
"progetto": 27,
"processing_node": 10,
"processing_node_name": "localhost:3000",
"conteggio_immagini": 48,
"can_rerun_from": [],
"risorse_disponibili": [
"tutto.zip",
"ortofoto.tif",
"ortofoto.png",
"modello_georeferenziato.las",
"modello_georeferenziato.ply",
"modello_georeferenziato.csv",
"modello_strutturato.zip"
  ],

"uuid": "4338d684-91b4-49a2-b907-8ba171894393",
"name": "Nome attività",
"tempo_elaborazione": 2197417,
"auto_processing_node": falso,
"stato": 40,
"ultimo_errore": nullo,
"opzioni": [
    {

"nome": "use-opensfm-pointcloud",
"valore": vero
    }

  ],

"created_at": "2017-02-18T18:01:55.402551Z",
"pending_action": nullo,
"upload_progress": 1.0,
"resize_progress": 0.0,
"running_progress": 1.0
}

```

Un [Attività](/api/task/) è l'unità di elaborazione di base di WebODM. Per calcolare un'ortofoto, una nuvola di punti e un modello con texture da un insieme di immagini, è necessario creare un [Attività](/api/task/).

Campo | Digitare | Descrizione
----- | ---- | -----------

id | int | Identificatore univoco
progetto | int | [Progetto](/api/reference/operazioni/projects_create/) ID a cui appartiene l'attività
nodo_elaborazione | int | L'ID del [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) a cui è stata assegnata questa attività oppure `null` se non è stato assegnato alcun [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/).
nome_nodo_elaborazione | stringa | Il nome del nodo di elaborazione riportato di seguito o "null" se non è stato assegnato alcun [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/).
conteggio_immagini | int | Numero di immagini
può_rieseguire_da | stringa[] | Elenco di possibili opzioni di "riesecuzione da" da cui questa attività potrebbe riavviarsi, dato il nodo di elaborazione attualmente assegnato. Se l'elenco è vuoto, l'attività può essere riavviata solo dall'inizio della pipeline.
risorse_disponibili | stringa[] | Elenco di [risorse](/api/task/#download-assets) disponibili per il download
uuid | stringa | Identificatore univoco assegnato da un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) una volta avviata l'elaborazione.
nome | stringa | Nome definito dall'utente per l'attività
tempo_dielaborazione | int | Millisecondi trascorsi dall'inizio dell'elaborazione o "-1" se non sono disponibili informazioni. Utile per visualizzare all'utente un report sullo stato temporale.
nodo_di_elaborazione_auto | booleano | Indica se WebODM deve assegnare automaticamente il successivo [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) disponibile per elaborare questa [Attività](/api/task/). Un utente può impostarlo su "false" per scegliere manualmente un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/).
stato | int | Uno dei [Codici di stato](#status-codes) o "null" se non è disponibile alcuno stato.
ultimo_errore | stringa | L'ultimo messaggio di errore segnalato da un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) in caso di errore di elaborazione.
opzioni | JSON[] | Elenco con codifica JSON di coppie nome/valore, dove ogni coppia rappresenta un'opzione della riga di comando da passare a un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/).
creato_a | stringa | Data e ora di creazione.
in attesa_azione | int | Una delle [Azioni in sospeso](#azioni-in sospeso) o "null" se non è impostata alcuna azione in sospeso.
upload_progress | galleggiante | Valore compreso tra 0 e 1 che indica l'avanzamento del caricamento dei file di questa attività nel nodo di elaborazione.
ridimensiona_progress | galleggiante | Valore compreso tra 0 e 1 che indica l'avanzamento del ridimensionamento delle immagini di questa attività.
esecuzione_progress | galleggiante | Valore compreso tra 0 e 1 che indica l'avanzamento dell'esecuzione (stimato) di questa attività.


<aside class="notice">Le attività ereditano le impostazioni di autorizzazione dal <a href="/api/reference/operazioni/projects_read/">Progetto</a> a cui appartengono.</aside>

### Crea un'attività

`POST /api/projects/{project_id}/tasks/`

Parametro | Obbligatorio | Predefinito | Descrizione
--------- | -------- | ------- | -----------

immagini[] | *| "" | Elenco di immagini con codifica in più parti (minimo 2)
nodo_elaborazione | | nullo | L'ID del [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) a cui deve essere assegnata questa [Attività](/api/task/). Se non specificato e auto_processing_node è "true", verrà assegnato automaticamente un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/).
nome | | "" | Nome definito dall'utente per l'attività
nodo_di_elaborazione_auto | | vero | Indica se WebODM deve assegnare automaticamente il successivo [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) disponibile per elaborare questa [Attività](/api/task/).
opzioni | | "[]" | Elenco con codifica JSON di coppie nome/valore, dove ogni coppia rappresenta un'opzione della riga di comando da passare a un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/).

Assegni un [Attività](/api/task/) a un [Progetto](/api/reference/operazioni/projects_create/) passando il percorso `project_id` corretto nell'URL.


### Aggiorna un'attività

`PATCH /api/projects/{project_id}/tasks/{task_id}/`

I parametri sono gli stessi di cui sopra.

### Importa attività

`POST /api/projects/{project_id}/tasks/import`

Importa attività che sono state elaborate da un'altra istanza WebODM (o tramite [webodm.net](https://webodm.net) o NodeODX)

Parametro | Obbligatorio | Predefinito | Descrizione
--------- | -------- | ------- | ----------
nome |          | Attività importata | Nome definito dall'utente per l'attività.
nomefile | */ | "" | File con risorse. Deve essere una cerniera.
URL | /* | "" | URL alle risorse compresse.

Devi fornire il parametro "nome file" o "url" (ma non entrambi) per importare le risorse create.

Ricorda di impostare il tipo di contenuto corretto per la richiesta a seconda di come vengono caricate le risorse:

Parametro | Tipo di contenuto
--------- | ---

nomefile | applicazione/zip
URL | application/x-www-form-urlencoded

### Ottieni l'elenco delle attività

> Elenco attività:

```json
[

    {

"id": 6,
"progetto": 2,
"processing_node": 2,
"processing_node_name": "localhost:3000",
"conteggio_immagini": 89,
"uuid": "2e8b687d-c269-4e2f-91b3-5a2cd51b5321",
"nome": "Nome del test",
"tempo_elaborazione": 8402184,
"auto_processing_node": vero,
"stato": 40,
"ultimo_errore": nullo,
"opzioni": [],
"created_at": "2016-12-08T13:32:28.139474Z",
"pending_action": nullo,
"upload_progress": 1.0,
"resize_progress": 0.0,
"running_progress": 1.0
    }

]

```

`GET /api/projects/{project_id}/tasks/`

Recupera tutti gli elementi [Attività](/api/task/) associati a "project_id".

### Scarica risorse

`GET /api/projects/{project_id}/tasks/{task_id}/download/{asset}`

Dopo che un'attività è stata elaborata correttamente, l'utente può scaricare diverse risorse da questo URL. Non tutte le risorse sono sempre disponibili. Ad esempio, se nelle immagini di input mancano le informazioni GPS, mancherà la risorsa "orthophoto.tif". Puoi controllare la proprietà "available_assets" di un [Attività](/api/task/) per vedere quali risorse sono disponibili per il download.

Risorsa | Descrizione
----- | -----------

all.zip | Archivio (.zip) contenente tutte le risorse, tra cui un'ortofoto, piastrelle TMS, un modello 3D con texture e una nuvola di punti in vari formati.
ortofoto.tif | Ortofoto GeoTIFF.
ortofoto.png | Ortofoto PNG.
orthophoto.mbtiles | Archivio Ortofoto MBTiles.
modello_strutturato.zip | Archivio contenente il modello 3D strutturato
georeferenced_model.las | Nuvola di punti in formato .LAS.
georeferenced_model.ply | Nuvola di punti in formato .PLY.
georeferenziato_modello.csv | Nuvola di punti in formato .CSV.

### Scarica risorse (percorso non elaborato)

`GET /api/projects/{project_id}/tasks/{task_id}/assets/{percorso}`

Dopo che un'attività è stata elaborata con successo, le sue risorse vengono archiviate in una directory nel file system. Questa chiamata API consente l'accesso diretto ai file in quella directory (per impostazione predefinita: `WebODM/app/media/project/{project_id}/task/{task_id}/assets`). Ciò può essere utile per quelle applicazioni che desiderano eseguire lo streaming di un set di dati "Potree" o eseguire il rendering al volo di un modello 3D con texture.

<aside class="avviso">
Questi percorsi potrebbero cambiare nelle versioni future di WebODM. Se la risorsa di cui hai bisogno può essere raggiunta tramite <b>/api/projects/{project_id}/tasks/download/{asset}</b>, utilizza quella.
</a parte>

### Recupera l'output della console

> Esempio di output della console:

```bash
curl -H "Autorizzazione: JWT <your_token>" http://localhost:8000/api/projects/2/tasks/1/output/?line=5

[DEBUG] /var/www/data/e453747f-5fd4-4654-9622-b02727b29fc5/images\n[DEBUG] Caricato DJI_0219.JPG | fotocamera: dji fc300s...
```


`GET /api/projects/{project_id}/tasks/{task_id}/output/`

Durante l'elaborazione di un [Attività](/api/task/), i nodi di elaborazione restituiranno una stringa di output che può essere utilizzata per scopi informativi e di debug. L'output è disponibile solo dopo l'avvio dell'elaborazione.

Parametro | Obbligatorio | Predefinito | Descrizione
--------- | -------- | ------- | -----------

linea | | 0| Visualizza solo l'output a partire da un determinato numero di riga. Ciò può essere utile per visualizzare l'output in tempo reale all'utente tenendo traccia del numero di righe che sono state visualizzate all'utente finora ed evitando così di scaricare tutto l'output ad ogni richiesta.

### Annulla l'attività

`POST /api/projects/{project_id}/tasks/{task_id}/cancel/`

Interrompe l'elaborazione di una [Attività](/api/task/). Le attività annullate possono essere riavviate.

### Rimuovi l'attività

`POST /api/projects/{project_id}/tasks/{task_id}/remove/`

Anche tutti i beni ad esso associati verranno distrutti. Se l'[Attività](/api/task/) è attualmente in fase di elaborazione, l'elaborazione verrà interrotta.

### Riavvia l'attività

`POST /api/projects/{project_id}/tasks/{task_id}/restart/`

Se un'[Attività](/api/task/) è stata annullata o ha fallito l'elaborazione oppure è stata completata ma l'utente ha deciso di modificare le opzioni di elaborazione, può essere riavviata. Se il [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) assegnato all'[Attività](/api/task/) non è cambiato, l'elaborazione avverrà più rapidamente rispetto alla creazione di una nuova [Attività](/api/task/), poiché il [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) ricorda l'"uuid" dell'[Attività](/api/task/) [Task](/api/task/) e tenterà di riutilizzare i risultati precedenti dalla pipeline di calcolo.

### Strato TMS di ortofoto

`GET /api/projects/{project_id}/tasks/{task_id}/orthophoto/tiles.json`

`GET /api/projects/{project_id}/tasks/{task_id}/orthophoto/tiles/{Z}/{X}/{Y}.png`

Dopo che un'attività è stata elaborata con successo, un livello TMS viene reso disponibile per l'inclusione in programmi come [Leaflet](http://leafletjs.com/) o [Cesium](http://cesiumjs.org).

<aside class="notice">Se utilizzi <a href="http://leafletjs.com/" target="_blank">Leaflet</a>, dovrai passare il token di autenticazione tramite querystring: /api/projects/{project_id}/tasks/{task_id}/tiles/{Z}/{X}/{Y}.png?jwt=your_token</aside>

### Strato TMS del modello di superficie

`GET /api/projects/{project_id}/tasks/{task_id}/dsm/tiles.json`

`GET /api/projects/{project_id}/tasks/{task_id}/dsm/tiles/{Z}/{X}/{Y}.png`

### Livello TMS del modello del terreno

`GET /api/projects/{project_id}/tasks/{task_id}/dtm/tiles.json`

`GET /api/projects/{project_id}/tasks/{task_id}/dtm/tiles/{Z}/{X}/{Y}.png`

### Azioni in sospeso

In alcune circostanze, una [Attività](/api/task/) può avere un'azione in sospeso che richiede una certa quantità di tempo per essere eseguita.

Azione in sospeso | Codice | Descrizione
----- | ---- | -----------

ANNULLA | 1| [Attività](/api/task/) in fase di annullamento
RIMUOVI | 2| [Attività](/api/task/) è in fase di rimozione
RIPARTIRE | 3| [Attività](/api/task/) è in fase di riavvio

### Codici di stato

Stato | Codice | Descrizione
----- | ---- | -----------

IN CODA | 10| I file di [Attività](/api/task/) sono stati caricati su un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) e sono in attesa di essere elaborati.
CORRERE | 20| [Attività](/api/task/) è attualmente in fase di elaborazione.
FALLITO | 30| [Task](/api/task/) non è riuscito per qualche motivo (immagini insufficienti, memoria esaurita, Piero ha dimenticato di chiudere una parentesi, ecc.)
COMPLETATO | 40| [Attività](/api/task/) è stata completata. Le risorse sono pronte per essere scaricate.
ANNULLATO | 50| [Attività](/api/task/) è stata annullata manualmente dall'utente.
