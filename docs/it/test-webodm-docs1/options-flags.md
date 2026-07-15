---

titolo: Opzioni e flag
modello: doc
---


Questo è l'elenco completo delle opzioni disponibili in [ODX](https://github.com/WebODM/ODX).


:::nota
Alcuni di questi non saranno visibili in [WebODM](https://github.com/WebODM/WebODM) perché non si applicano o sono integrati nel flusso di lavoro dell'esperienza utente (ad esempio, i GCP vengono selezionati automaticamente, quindi non è necessario specificare un'opzione `--gcp`).
:::


## Piastrelle 3D

Genera output di piastrelle 3D OGC.

**Predefinito:** "Falso".

## allinea

Percorso verso un DEM GeoTIFF o una nuvola di punti LAS/LAZ a cui allineare automaticamente gli output della ricostruzione. Sperimentale.

**Opzioni:** `<stringa del percorso>`

**Predefinito:** "Nessuno".

## confine automatico

Imposta automaticamente un confine utilizzando le posizioni delle riprese della fotocamera per limitare l'area della ricostruzione. Ciò può aiutare a rimuovere gli artefatti di sfondo lontani (cielo, paesaggi di sfondo, ecc.). Vedi anche --boundary.

**Predefinito:** "Falso".

## distanza dal confine automatico

Specificare la distanza tra le posizioni delle riprese della fotocamera e il bordo esterno del confine quando si calcola il confine con --auto-boundary. Impostare su 0 per scegliere automaticamente un valore.

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "0".

## rimozione-bg

Calcola automaticamente le maschere delle immagini utilizzando l'intelligenza artificiale per rimuovere lo sfondo. Sperimentale.

**Predefinito:** "Falso".

## confine

Poligono GeoJSON che limita l'area della ricostruzione. Può essere specificato come percorso di un file GeoJSON o come stringa JSON che rappresenta il contenuto di un file GeoJSON.

**Opzioni:** `<json>`

## panoramiche della build

Crea panoramiche di ortofoto per una visualizzazione più rapida in programmi come QGIS.

**Predefinito:** "Falso".

## obiettivo della fotocamera

Imposta un tipo di proiezione della telecamera. L'impostazione manuale di un valore può aiutare a migliorare l'assenza di distorsione geometrica. Per impostazione predefinita, l'applicazione tenta di determinare un tipo di obiettivo dai metadati delle immagini.

**Opzioni:** `auto |  prospettiva |  marrone |  occhio di pesce |  fisheye_opencv |  sferico |  equirettangolare |  doppio`

**Predefinito:** "auto".

## fotocamere

Utilizza i parametri della fotocamera calcolati da un altro set di dati invece di calcolarli. Può essere specificato come percorso di un file cameras.json o come stringa JSON che rappresenta il contenuto di un file cameras.json.

**Opzioni:** `<json>`

## ingranaggio

Crea GeoTIFF ottimizzati per il cloud invece dei normali GeoTIFF.

**Predefinito:** "Falso".

## copia in

Copia i risultati di output in questa cartella dopo l'elaborazione.

**Opzioni:** `<percorso>`

## raccolto

Ritaglia automaticamente gli output delle immagini creando un buffer uniforme attorno ai confini del set di dati, ridotto di N metri. Utilizzare 0 per disattivare il ritaglio.

**Opzioni:** "<virgola mobile positivo>".

**Predefinito:** "3".

##decimazionedem

Decimare i punti prima di generare il DEM. 1 non rappresenta alcuna decimazione (qualità completa). 100 decima circa il 99%% dei punti. Utile per accelerare la generazione di risultati DEM in set di dati molto grandi.

**Opzioni:** `<intero positivo>`

**Predefinito:** "1".

## mappa-dem-euclidea

Calcola una mappa raster euclidea per ogni DEM. La mappa riporta la distanza da ciascuna cella al valore NODATA più vicino (prima che avvenga qualsiasi riempimento del buco). Questo può essere utile per isolare le aree che sono state riempite.

**Predefinito:** "Falso".

## passaggi per riempire i vuoti

Numero di passaggi utilizzati per riempire le aree con spazi vuoti. Impostare su 0 per disabilitare il riempimento degli spazi. A partire da un raggio uguale alla risoluzione di output, N diversi DEM vengono generati con raggio progressivamente maggiore utilizzando l'algoritmo IDW (inverse distance pondered) e fusi insieme. Gli spazi rimanenti vengono quindi uniti utilizzando l'interpolazione del vicino più vicino.

**Opzioni:** `<intero positivo>`

**Predefinito:** "3".

## risoluzione dem

Risoluzione DSM/DTM in cm/pixel. Si noti che questo valore è limitato da una stima della distanza di campionamento del suolo (GSD).

**Opzioni:** `<float>`

**Predefinito:** "5".

##dsm

Utilizza questo tag per costruire un DSM (Digital Surface Model, terreno + oggetti) utilizzando un filtro morfologico progressivo. Controlla i parametri --dem* per una regolazione più precisa.

**Predefinito:** "Falso".

##dtm

Utilizza questo tag per costruire un DTM (Digital Terrain Model, ground only) utilizzando un semplice filtro morfologico. Controlla i parametri --dem* e --smrf* per una regolazione più precisa.

**Predefinito:** "Falso".

## termina con

Terminare l'elaborazione in questa fase.

**Opzioni:** `dataset |  diviso |  unisci |  opensfm |  openmvs |  odm_filterpoints |  odm_meshing |  mvs_texturing |  odm_georeferenziazione |  odm_dem |  odm_ortofoto |  odm_report |  odm_postprocess`

**Predefinito:** `odm_postprocess`

## ortofoto veloce

Salta la ricostruzione densa e la generazione del modello 3D. Genera un'ortofoto direttamente dalla ricostruzione sparsa. Su terreno pianeggiante senza oggetti/strutture, attiva questa opzione per risparmiare tempo.

**Predefinito:** "Falso".

## qualità delle funzionalità

Imposta la qualità di estrazione delle caratteristiche. Una qualità più elevata genera funzionalità migliori, ma richiede più memoria e richiede più tempo.

**Opzioni:** `ultra |  alto |  medio |  basso |  più basso`

**Predefinito:** "alto".

## tipo di funzionalità

Scegli l'algoritmo per l'estrazione dei punti chiave e i descrittori di calcolo.

**Opzioni:** `akaze |  dspsift |  ahah |  sfera |  setacciare`

**Predefinito:** `dspsift`

## forza-gps

Utilizza i dati EXIF ​​GPS delle immagini per la ricostruzione, anche se sono presenti GCP. Questo flag è utile se disponi di misurazioni GPS ad alta precisione. Se non sono presenti GCP, questo flag non fa nulla.

**Predefinito:** "Falso".

##gcp

Percorso del file contenente i punti di controllo a terra utilizzati per la georeferenziazione. Il file deve utilizzare il seguente formato:

EPSG:`<codice>` o `<+definizione progetto>`

geo_x geo_y geo_z im_x im_y nome_immagine [nome_gcp] [extra1] [extra2]

**Opzioni:** `<stringa del percorso>`

**Predefinito:** "Nessuno".

## geografico

Percorso del file di geolocalizzazione dell'immagine contenente le coordinate del centro della fotocamera utilizzate per la georeferenziazione. Se non disponi di valori per imbardata/beccheggio/rollio puoi impostarli su 0. Il file deve utilizzare il seguente formato:

EPSG:`<codice>` o `<+definizione progetto>`

nome_immagine geo_x geo_y geo_z [imbardata (gradi)] [beccheggio (gradi)] [rollio (gradi)] [precisione orizzontale (metri)] [precisione verticale (metri)]

**Opzioni:** `<stringa del percorso>`

**Predefinito:** "Nessuno".

## gltf

Genera modelli con texture glTF (GLB) binari a file singolo.

**Predefinito:** "Falso".

## precisione GPS

Impostare un valore in metri per le informazioni sulla diluizione della precisione GPS (DOP) per tutte le immagini. Se le tue immagini sono contrassegnate con informazioni GPS ad alta precisione (RTK), questo valore verrà impostato automaticamente di conseguenza. È possibile utilizzare questa opzione per impostarla manualmente nel caso in cui la ricostruzione fallisca. Abbassare questa opzione a volte può aiutare a controllare gli effetti del bowling su vaste aree.

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "3".

## offset-z-gps

Imposta un offset GPS in metri per l'asse verticale (Z) aggiungendolo al valore di altitudine dei dati EXIF ​​GPS. Ciò non modifica il valore di alcun GCP. Ciò può essere utile, ad esempio, quando si regola l'altezza da ellissoidale a ortometrica.

**Opzioni:** `<float>`

**Predefinito:** "0".

## aiuto

mostra questo messaggio di aiuto ed esci

## ignora-gsd

Ignora la distanza di campionamento del suolo (GSD). Una modifica affamata di memoria e processore rispetto al comportamento predefinito se impostata su true. Di solito, le stime GSD vengono utilizzate per limitare la risoluzione massima delle immagini in uscita e ridimensionare le immagini quando necessario, con conseguente elaborazione più rapida e minore utilizzo della memoria. Poiché il GSD è una stima, a volte ignorarlo può comportare una qualità di output dell'immagine leggermente migliore. Non impostare mai --ignore-gsd su true a meno che tu non sia sicuro di averne bisogno, e anche in quel caso: non usarlo.

**Predefinito:** "Falso".

## matcher-vicini

Esegui la corrispondenza delle immagini con le immagini più vicine in base ai dati GPS EXIF. Impostato su 0 per la corrispondenza tramite triangolazione.

**Opzioni:** `<intero positivo>`

**Predefinito:** "0".

## ordine di corrispondenza

Esegui la corrispondenza delle immagini con le N immagini più vicine in base all'ordine dei nomi dei file immagine. Può accelerare l'elaborazione di immagini sequenziali, come quelle estratte da un video. Si applica solo su dataset non georeferenziati. Impostare su 0 per disabilitare.

**Opzioni:** `<intero positivo>`

**Predefinito:** "0".

## tipo di corrispondenza

Algoritmo Matcher, Libreria veloce per i vicini più vicini approssimati o Borsa di parole. FLANN è più lento, ma più stabile. BOW è più veloce, ma a volte può perdere corrispondenze valide. BRUTEFORCE è molto lento ma robusto. HAMMING è molto più veloce con set di dati di grandi dimensioni ma richiede una GPU.

**Opzioni:** `auto |  arco |  forza bruta |  Flann |  martellando`

**Predefinito:** "auto".

## massima concorrenza

Il numero massimo di processi da utilizzare in vari processi. Il requisito massimo di memoria è di ~1 GB per thread e una risoluzione dell'immagine di 2 megapixel.

**Opzioni:** `<intero positivo>`

**Predefinito:** "4".

## unisci

Scegli cosa unire nella fase di unione in un set di dati diviso. Per impostazione predefinita, tutti gli output disponibili vengono uniti. Opzioni: ['tutti', 'nuvola di punti', 'ortofoto', 'dem'].

**Opzioni:** `tutti |  nuvola di punti |  ortofoto |  dem`

**Predefinito:** "tutti".

## mesh-octree-profondità

Profondità di otto utilizzati nella ricostruzione della mesh, aumentare per ottenere più vertici, i valori consigliati sono 8-12.

**Opzioni:** `<numero intero: 1 <= x <= 14>`

**Predefinito:** "11".

## dimensione della maglia

Il numero massimo di vertici della mesh di output.

**Opzioni:** `<intero positivo>`

**Predefinito:** "200000".

## numero-min-funzioni

Numero minimo di funzionalità da estrarre per immagine. Più funzionalità possono essere utili per trovare più corrispondenze tra le immagini, consentendo potenzialmente la ricostruzione di aree con poca sovrapposizione o caratteristiche insufficienti. Ulteriori funzionalità rallentano anche l'elaborazione.

**Opzioni:** `<numero intero>`

**Predefinito:** "10000".

## nome

Nome del set di dati (ovvero il nome della sottocartella all'interno della cartella del progetto).

**Opzioni:** "<nome set di dati>".

**Predefinito:** `codice`

## senza GPU

Non utilizzare l'accelerazione GPU, anche se disponibile.

**Predefinito:** "Falso".

## ottimizza lo spazio su disco

Elimina file intermedi pesanti per ottimizzare l'utilizzo dello spazio su disco. Ciò influisce sulla possibilità di riavviare la pipeline da una fase intermedia, ma consente l'elaborazione dei set di dati su macchine che non dispongono di spazio su disco sufficiente.

**Predefinito:** "Falso".

## ortofoto-compressione

Imposta la compressione da utilizzare per le ortofoto.

**Opzioni:** `JPEG |  LZW |  PACKBITS |  SGONFIARE |  LZMA |  NESSUNO

**Predefinito:** "SGONFIAGGIO".

## ortofoto-taglio

Genera un poligono attorno all'area di ritaglio che taglia l'ortofoto attorno ai bordi delle geometrie. Questo poligono può essere utile per cucire mosaici senza soluzione di continuità con più ortofoto sovrapposte.

**Predefinito:** "Falso".

## ortofoto-kmz

Imposta questo parametro se vuoi generare un rendering Google Earth (KMZ) dell'ortofoto.

**Predefinito:** "Falso".

##ortofoto-non-piastrellata

Imposta questo parametro se desideri un GeoTIFF con striping.

**Predefinito:** "Falso".

## ortofoto-png

Imposta questo parametro se vuoi generare un rendering PNG dell'ortofoto.

**Predefinito:** "Falso".

## risoluzione ortofoto

Risoluzione ortofoto in cm/pixel. Si noti che questo valore è limitato da una stima della distanza di campionamento del suolo (GSD).

**Opzioni:** `<float > 0.0>`

**Predefinito:** "5".

## classificazione PC

Classificare gli output della nuvola di punti. Puoi controllare il comportamento di questa opzione modificando i parametri --dem-*.

**Predefinito:** "Falso".

##pc-copc

Salvare la nuvola di punti georeferenziata nel formato Cloud Optimized Point Cloud (COPC).

**Predefinito:** "Falso".

##pc-csv

Esporta la nuvola di punti georeferenziata in formato CSV.

**Predefinito:** "Falso".

## pc-ep

Esporta la nuvola di punti georeferenziata in formato Entwine Point Tile (EPT).

**Predefinito:** "Falso".

## filtro per PC

Filtra la nuvola di punti rimuovendo i punti che deviano più di N deviazioni standard dalla media locale. Impostato su 0 per disabilitare il filtraggio.

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "5".

##pc-las

Esporta la nuvola di punti georeferenziata in formato LAS.

**Predefinito:** "Falso".

## qualità PC

Imposta la qualità della nuvola di punti. Una qualità più elevata genera nuvole di punti migliori e più dense, ma richiede più memoria e richiede più tempo. Ogni miglioramento della qualità aumenta il tempo di elaborazione di circa un fattore 4x.

**Opzioni:** `ultra |  alto |  medio |  basso |  più basso`

**Predefinito:** "medio".

## campione per PC

Filtra la nuvola di punti mantenendo un solo punto attorno a un raggio N (in metri). Ciò può essere utile per limitare la risoluzione di output della nuvola di punti e rimuovere i punti duplicati. Impostare su 0 per disabilitare il campionamento.

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "0".

## pc-salta-geometrico

Le stime geometriche migliorano la precisione della nuvola di punti calcolando mappe di profondità geometricamente coerenti, ma potrebbero non essere utilizzabili in set di dati più grandi. Questo flag disabilita le stime geometriche.

**Predefinito:** "Falso".

## banda primaria

Durante l'elaborazione di set di dati multispettrali, è possibile specificare il nome della banda primaria che verrà utilizzata per la ricostruzione. Si consiglia di scegliere una fascia con dettagli nitidi e a fuoco.

**Opzioni:** `<string>`

**Predefinito:** "auto".

## percorso-progetto

Percorso della cartella del progetto. La cartella del progetto dovrebbe contenere sottocartelle per ciascun set di dati. Ogni set di dati dovrebbe avere una cartella "immagini".

**Opzioni:** `<percorso>`

## calibrazione radiometrica

Impostare la calibrazione radiometrica da eseguire sulle immagini. Quando si elaborano immagini multispettrali e termiche è necessario impostare questa opzione per ottenere valori di riflettanza/temperatura (altrimenti si otterranno valori numerici digitali). [fotocamera] applica il livello di nero, la vignettatura, il guadagno del gradiente di riga/compensazione dell'esposizione (se vengono trovati tag EXIF ​​appropriati) e calcola i valori di temperatura assoluti. [camera+sun] è sperimentale, applica tutte le correzioni di [camera], inoltre compensa la radianza spettrale registrata tramite un sensore di luce discendente (DLS) prendendo in considerazione l'angolo del sole.

**Opzioni:** `nessuno |  macchina fotografica |  fotocamera+sole`

**Predefinito:** "nessuno".

## unità di report

Imposta le unità del report PDF. Per impostazione predefinita vengono utilizzate le unità verticali del sistema di riferimento delle coordinate.

**Opzioni:** `m |  piedi |  Piede di indagine statunitense`

**Predefinito:** `m`

## replica

Rieseguire solo questa fase e fermarsi.

**Opzioni:** `dataset |  diviso |  unisci |  opensfm |  openmvs |  odm_filterpoints |  odm_meshing |  mvs_texturing |  odm_georeferenziazione |  odm_dem |  odm_ortofoto |  odm_report |  odm_postprocess`

## riesegui tutto

Elimina definitivamente tutti i risultati precedenti ed esegui nuovamente la pipeline di elaborazione.

**Predefinito:** "Falso".

## replica da

Eseguire nuovamente l'elaborazione da questa fase.

**Opzioni:** `dataset |  diviso |  unisci |  opensfm |  openmvs |  odm_filterpoints |  odm_meshing |  mvs_texturing |  odm_georeferenziazione |  odm_dem |  odm_ortofoto |  odm_report |  odm_postprocess`

## tapparella

Attiva la correzione della tapparella. Se la fotocamera è dotata di tapparella e le immagini sono state scattate in movimento, puoi attivare questa opzione per migliorare la precisione dei risultati. Vedi anche --rolling-shutter-readout.

**Predefinito:** "Falso".

## Lettura tapparelle

Sostituisci il tempo di lettura della tapparella per il sensore della fotocamera (in millisecondi), invece di utilizzare il database di lettura della tapparella. Tieni presente che non tutte le telecamere sono presenti nel database. Impostare su 0 per utilizzare il valore del database.

**Opzioni:** `<intero positivo>`

**Predefinito:** "0".

## algoritmo sfm

Scegli la struttura dall'algoritmo di movimento. Per i set di dati aerei, se sono disponibili le posizioni e gli angoli GPS della fotocamera, la triangolazione può essere più rapida. Planar è deprecato e verrà rimosso in una versione futura.

**Opzioni:** `incrementale |  triangolazione |  planare`

**Predefinito:** "incrementale".

## sfm-no-parziale

Non tentare di unire ricostruzioni parziali. Ciò può accadere quando le immagini non hanno una sovrapposizione sufficiente o sono isolate.

**Predefinito:** "Falso".

## salta-3dmodello

Salta la generazione di un modello 3D completo. Ciò può farti risparmiare tempo se hai bisogno solo di risultati 2D come ortofoto e DEM.

**Predefinito:** "Falso".

## allineamento salta-banda

Durante l'elaborazione di set di dati multispettrali, allinea automaticamente le immagini per ciascuna banda. Se le immagini sono state postelaborate e sono già allineate, utilizza questa opzione.

**Predefinito:** "Falso".

## salta-ortofoto

Salta la generazione dell'ortofoto. Ciò può farti risparmiare tempo se hai bisogno solo di risultati 3D o DEM.

**Predefinito:** "Falso".

## skip-report

Salta la generazione del report PDF. Ciò può farti risparmiare tempo se non hai bisogno di un rapporto.

**Predefinito:** "Falso".

## rimozione del cielo

Calcola automaticamente le maschere delle immagini utilizzando l'intelligenza artificiale per rimuovere il cielo. Sperimentale.

**Predefinito:** "Falso".

## cluster sm

URL a un'istanza ClusterODM per la distribuzione di un flusso di lavoro diviso-unito su più nodi in parallelo.

**Opzioni:** `<string>`

**Predefinito:** "Nessuno".

## sm-non-allinea

Salta l'allineamento dei sottomodelli nella suddivisione-unione. Utile se il GPS è sufficientemente buono su set di dati molto grandi.

**Predefinito:** "Falso".

## smrf-scalare

Parametro scalare di elevazione del filtro morfologico semplice.

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "1.25".

## pendenza-srf

Parametro di pendenza del filtro morfologico semplice (salita rispetto alla corsa).

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "0,15".

## soglia smrf

Parametro di soglia di elevazione del Filtro Morfologico Semplice (metri).

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "0,5".

## finestra smrf

Parametro del raggio della finestra del filtro morfologico semplice (metri).

**Opzioni:** `<virgola mobile positivo>`

**Predefinito:** "18.0".

## diviso

Numero medio di immagini per sottomodello. Quando si suddivide un set di dati di grandi dimensioni in sottomodelli più piccoli, le immagini vengono raggruppate in cluster. Questo valore regola il numero di immagini che ogni cluster dovrebbe avere in media.

**Opzioni:** `<intero positivo>`

**Predefinito:** `999999`

## gruppi di immagini divise

Percorso del file dei gruppi di immagini che controlla il modo in cui le immagini devono essere suddivise in gruppi. Il file deve utilizzare il seguente formato:

nome_immagine nome_gruppo

**Opzioni:** `<stringa del percorso>`

**Predefinito:** "Nessuno".

## sovrapposizione divisa

Raggio della sovrapposizione tra sottomodelli in metri. Dopo aver raggruppato le immagini in cluster, le immagini che sono più vicine di questo raggio a un cluster vengono aggiunte al cluster. Questo viene fatto per garantire che i sottomodelli vicini si sovrappongano. Tutte le immagini necessitano di informazioni GPS.

**Opzioni:** `<intero positivo>`

**Predefinito:** "150".

## texturizzazione-mantieni-volti-invisibili

Mantieni nella mesh i volti che non vengono visualizzati in nessuna fotocamera.

**Predefinito:** "Falso".

## texturizzazione-monomaterica

Genera OBJ che hanno un singolo materiale e un singolo file di texture invece di più.

**Predefinito:** "Falso".

## texturing-skip-global-seam-leveling

Salta la normalizzazione dei colori su tutte le immagini. Utile durante l'elaborazione dei dati radiometrici.

**Predefinito:** "Falso".

## piastrelle

Genera riquadri statici per ortofoto e DEM adatti a visualizzatori come Leaflet o OpenLayers.

**Predefinito:** "Falso".

## usa-3dmesh

Utilizza una mesh 3D completa per calcolare l'ortofoto invece di una mesh 2.5D. Questa opzione è un po' più veloce e fornisce risultati simili nelle aree planari.

**Predefinito:** "Falso".

## usa-exif

Utilizza questo tag se disponi di un file GCP ma desideri invece utilizzare le informazioni EXIF ​​per la georeferenziazione.

**Predefinito:** "Falso".

## usa-parametri-fotocamera-fissi

Disattiva l'ottimizzazione dei parametri della fotocamera durante la regolazione del pacchetto. Questo a volte può essere utile per migliorare i risultati che mostrano dome/bowling o quando le immagini vengono scattate con una fotocamera con otturatore scorrevole.

**Predefinito:** "Falso".

## usa la regolazione del pacchetto ibrido

Eseguire una regolazione del bundle locale per ogni immagine aggiunta alla ricostruzione e una regolazione globale ogni 100 immagini. Accelera la ricostruzione di set di dati molto grandi.

**Predefinito:** "Falso".

## versione

Visualizza il numero di versione ed esce.

## limite video

Numero massimo di fotogrammi da estrarre dai file video per l'elaborazione. Impostato su 0 per nessun limite.

**Opzioni:** `<intero positivo>`

**Predefinito:** "500".

## risoluzione video

La massima risoluzione di output dei fotogrammi video estratti in pixel.

**Opzioni:** `<intero positivo>`

**Predefinito:** "4000".


