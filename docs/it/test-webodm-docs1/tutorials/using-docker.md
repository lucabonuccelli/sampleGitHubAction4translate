---

titolo: Utilizzo di Docker
---


Poiché molti utenti utilizzano la finestra mobile per distribuire WebODM, può essere utile comprendere alcuni comandi di base per interrogare le istanze della finestra mobile quando le cose vanno male o quando siamo curiosi di sapere cosa sta succedendo. Docker è un ambiente containerizzato destinato, tra le altre cose, a semplificare la distribuzione di software indipendente dall'ambiente locale. In questo modo è simile alle macchine virtuali.

### Elenco delle macchine Docker

Possiamo iniziare elencando le macchine docker disponibili sulla macchina attualmente in esecuzione come segue:

```
> finestra mobile ps
ID CONTENITORE COMANDO IMMAGINE CREATO STATO NOMI PORTE
2518817537ce webodm/odx "bash" 36 ore fa Su 36 ore zen_wright
1cdc7fadf688 webodm/nodeodx "/usr/bin/nodejs /va…" 37 ore fa Su 37 ore 0.0.0.0:3000->3000/tcp flamboyant_dhawan
```

Se vogliamo vedere macchine che potrebbero non essere in esecuzione ma che esistono ancora, possiamo aggiungere il flag `-a`:

```
> finestra mobile ps -a
ID CONTENITORE COMANDO IMMAGINE CREATO STATO NOMI PORTE
2518817537ce webodm/odx "bash" 36 ore fa Su 36 ore zen_wright
1cdc7fadf688 webodm/nodeodx "/usr/bin/nodejs /va…" 37 ore fa Su 37 ore 0.0.0.0:3000->3000/tcp flamboyant_dhawan
cd7b9585b8f6 webodm/odx "bash" 3 giorni fa Uscito (1) 37 ore fa nostalgic_lederberg
e31010c00b9a webodm/odx "python /code/run.py…" 3 giorni fa Uscito (2) 3 giorni fa sospetto_kepler
c44e0d0b8448 webodm/nodeodx "/usr/bin/nodejs /va…" 3 giorni fa Uscito (0) 37 ore fa meraviglioso_burnell
```

### Accesso ai log sull'istanza

Utilizzando l'"ID CONTAINER" o il nome, possiamo accedere a tutti i log disponibili sulla macchina come segue:

```bash
registri della finestra mobile 2518817537ce
```

Probabilmente sarà ingombrante, ma possiamo usare il carattere pipe `|` e altri strumenti per estrarre proprio ciò di cui abbiamo bisogno dai log. Ad esempio possiamo spostarci lentamente nel registro utilizzando il comando `more`:

```
> registri della finestra mobile 2518817537ce | Di più
[INFO] Il DTM è attivato, attivando automaticamente la classificazione della nuvola di punti
[INFO] Inizializzazione dell'app ODX - lun 23 set 01:30:33 2019
[INFO] ==============
[INFO] build_overviews: falso
[INFO] obiettivo_camera: automatico
[INFO] ritaglia: 3
Debug [INFO]: falso
[INFO] dem_decimazione: 1
[INFO] dem_euclidean_map: Falso
...

```

Premendo "Invio" o "Spazio", i tasti freccia o i tasti "Pagina su" o "Pagina giù" ora ci aiuteranno a navigare tra i registri. La lettera minuscola "Q" ci consentirà di tornare alla riga di comando.

Possiamo anche estrarre solo la fine dei log utilizzando il comando `tail` come segue:

```
> registri della finestra mobile 2518817537ce | coda -5
[INFO] Ritaglio /datasets/code/odm_orthophoto/odm_orthophoto.tif
[INFO] in esecuzione gdalwarp -cutline /datasets/code/odm_georeferencing/odm_georeferenced_model.bounds.gpkg ...
Utilizzando la banda 4 dell'immagine sorgente come alfa.
Creazione del file di output 111567P x 137473L.
Elaborazione del file di input /datasets/code/odm_orthophoto/odm_orthophoto.original.tif.
```

Il valore "-5" dice al comando tail di fornirci solo le ultime 5 righe dei log.

### Accesso dalla riga di comando alle istanze

A volte abbiamo bisogno di andare un po' più in profondità nella nostra esplorazione del processo per OpenDroneMap. Per questo, possiamo ottenere l'accesso diretto alla riga di comando alle macchine utilizzando `docker exec`:

```bash
> docker exec -ti 2518817537ce bash
root@2518817537ce:/codice#
```

Ora abbiamo effettuato l'accesso alla nostra istanza docker e possiamo esplorare la macchina.

### Ripulitura dopo Docker

Docker fa un uso deplorevole dello spazio e per impostazione predefinita non ripulisce i dati e le macchine in eccesso una volta completati i processi. Ciò può essere vantaggioso se dobbiamo accedere a un processo che nel frattempo è terminato, ma comporta l'onere di utilizzare quantità crescenti di spazio di archiviazione nel tempo. Maciej Łebkowski ha un'[eccellente panoramica su come gestire l'utilizzo eccessivo del disco nella finestra mobile](https://lebkowski.name/docker-volumes/).
