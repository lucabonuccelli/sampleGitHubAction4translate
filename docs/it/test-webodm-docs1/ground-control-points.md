---

titolo: Punti di controllo a terra
modello: doc
---


I punti di controllo a terra sono utili per correggere le distorsioni nei dati e fare riferimento ai dati a sistemi di coordinate noti.

Un punto di controllo a terra (GCP) è una misurazione della posizione effettuata a terra, in genere utilizzando un GPS ad alta precisione.

I punti di controllo a terra possono essere impostati su strutture esistenti come angoli del marciapiede, linee su un parcheggio o piastrelle del pavimento in colori contrastanti, altrimenti possono essere impostati utilizzando bersagli posizionati a terra.

I bersagli possono essere acquistati o costruiti con un'ampia varietà di materiali, dai coperchi dei secchi alle piastrelle del pavimento.

### Pratiche consigliate per l'impostazione di GCP

Mantieni visibili i punti di controllo a terra per tutte le posizioni delle telecamere. Considerare la distanza di campionamento del terreno prevista, l'illuminazione, la vegetazione, gli edifici e tutti gli ostacoli esistenti.

Garantire una distribuzione uniformemente orizzontale dei GCP all'interno del progetto, coprendo quote elevate e basse. Un minimo di 5 GCP funziona per la maggior parte dei lavori e per progetti più grandi sono sufficienti 8-10. Individua alcuni punti vicino agli angoli e altri al centro, considerando che la spaziatura GCP dovrebbe essere maggiore dell'impronta dell'immagine in modo da non poter vedere più di un GCP in una singola immagine.

Per garantire che i GCP siano presenti in almeno 5 immagini, separare i punti da 10 a 30 metri dal perimetro del progetto. Questa distanza dipende dalla sovrapposizione, pertanto l'aumento della sovrapposizione dovrebbe ridurre la distanza richiesta dal perimetro.

### Formato file GCP

Il formato del file GCP è semplice.

- La prima riga deve contenere il nome della proiezione utilizzata per le coordinate geografiche. Questo può essere specificato come stringa PROJ (ad esempio `+proj=utm +zone=10 +ellps=WGS84 +datum=WGS84 +units=m +no_defs`), codice EPSG (ad esempio `EPSG:4326`) o come valore `WGS84 UTM <zone>[N|S]` (ad esempio `WGS84 UTM 16N`)
- Le righe successive sono le coordinate X, Y e Z, i pixel associati, il nome del file immagine e campi aggiuntivi opzionali, separati da tabulazioni o spazi
- Evitare di impostare i valori di elevazione su "NaN" per non indicare alcun valore. Ciò può causare errori di elaborazione. Utilizzare invece 0.0
- Allo stesso modo, diminuendo il numero di cifre dopo la cifra decimale per "geo_x" e "geo_y" si possono ridurre gli errori di elaborazione
- La settima colonna (facoltativa) contiene in genere l'etichetta del GCP

```
<proiezione>
geo_x geo_y geo_z im_x im_y nome file [etichetta] [extra1] [extra2]
...

```

Esempio:

```
+proj=utm +zone=10 +ellps=WGS84 +datum=WGS84 +unità=m +no_defs
544256.7 5320919.9 5 3044 2622 IMG_0525.jpg
544157.7 5320899.2 5 4193 1552 IMG_0585.jpg
544033.4 5320876.0 5 1606 2763 IMG_0690.jpg
```

:::nota
* Il nome del file fa distinzione tra maiuscole e minuscole. IMG_0001.jpg non è uguale a IMG_0001.JPG.
* Il nome del file non può contenere spazi. Gli spazi possono essere codificati utilizzando la sequenza di escape %20. Per esempio. Il riferimento a My Image.JPG deve essere My%20Image.JPG.
:::


Se fornisci un file GCP chiamato "gcp_list.txt", WebODM lo rileverà automaticamente. Se hai un file gcp e desideri invece eseguire la georeferenziazione con EXIF, puoi specificare `--use-exif`. Se nelle tue immagini sono presenti misurazioni GPS ad alta precisione (RTK) e desideri utilizzare tali informazioni insieme a un file gcp, puoi specificare `--force-gps`.

È importante trovare oggetti ad alto contrasto presenti in **almeno** 3 foto e trovare un minimo di 5 oggetti.

Gli angoli acuti sono una buona scelta per i GCP. Dovresti anche posizionare/trovare i GCP in modo uniforme nell'area di indagine.

Il file `gcp_list.txt` deve essere creato nella base della cartella del progetto.

Per ottenere buoni risultati il ​​tuo file dovrebbe avere un minimo di 15 righe dopo l'intestazione (5 punti con 3 immagini per ciascun punto).

### Contrassegnare i checkpoint

I checkpoint vengono utilizzati per verificare l'accuratezza della ricostruzione. Vengono esclusi dal processo di ricostruzione e vengono invece utilizzati per misurare l'accuratezza dei risultati finali.

Puoi contrassegnare un checkpoint etichettandolo con il prefisso "CHK-". Per esempio:

```
+proj=utm +zone=10 +ellps=WGS84 +datum=WGS84 +unità=m +no_defs
544256.7 5320919.9 5 3044 2622 IMG_0525.jpg CHK-A
```


### Interfacce utente

Puoi utilizzare una delle due interfacce utente per creare file GCP:

- [POSM GCPi](https://github.com/posm/posm-gcpi)
- [GCP Editor Pro](https://github.com/uav4geo/GCPEditorPro)

#### POSM GCPi

Il POSM GCPi viene caricato per impostazione predefinita su WebODM. Per utilizzarlo con i valori XYZ di controllo a terra noti, è necessario procedere come segue:

Crea un elenco GCP che includa solo il nome GCP, x, yez, con un'intestazione con una stringa proj4 dei tuoi GCP (assicurati che siano in un sistema di coordinate planari, come UTM). Dovrebbe assomigliare a questo:

```
+proj=utm +zone=37 +sud +ellps=WGS84 +datum=WGS84 +unità=m +no_defs
gcp01 529356.250827686 9251137.5643209 8.465
gcp02 530203.125367657 9250140.80991621 15.781
gcp03 530292.136003818 9250745.02372435 11.977
gcp04 530203.125367657 9250140.80991621 15.781
gcp05 530292.136003818 9250745.02372435 11.977
```

Quindi è possibile caricare questo elenco GCP nell'interfaccia, caricare le immagini e posizionare ciascuno dei GCP nell'immagine.

#### Editor GCP Pro

:::suggerimento[Lo sapevi?]

[GCP Editor Pro](https://gcp.uav4geo.com) è creato dagli sviluppatori di WebODM. Acquistandolo si supporta direttamente lo sviluppo di WebODM. ❤

:::


È necessario acquistare [GCP Editor Pro](https://gcp.uav4geo.com), ma fornisce un flusso di lavoro più fluido rispetto a POSM GCPi.

Per utilizzarlo, crea un file CSV che includa i nomi GCP, nord, est ed elevazione.

```
Etichetta GCP,Nord,Est,Elevazione
gcp01,529356.250827686,9251137.5643209,8.465
gcp02,530203.125367657,9250140.80991621,15.781
...

```

Quindi importa il CSV dalla schermata principale e digita `+proj=utm +zone=37 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs` nella casella `EPSG/PROJ`. Puoi trovare un database di codici EPSG su https://epsg.io

Nella schermata seguente verrà visualizzata una mappa da cui selezionare i GCP a cui taggare e importare le rispettive immagini.

## Precisione della mappa

L'accuratezza può essere definita come il grado o la vicinanza con cui le informazioni su una mappa corrispondono ai valori nel mondo reale. Pertanto, quando parliamo di accuratezza, parliamo di qualità dei dati e di numero di errori contenuti in un determinato set di dati (Pascual 2011).

**Precisione relativa o locale**

La precisione locale o relativa può essere definita come il grado in cui le distanze tra due punti su una mappa corrispondono alle distanze effettive tra tali punti nel mondo reale.

La precisione relativa è indipendente dalla posizione della mappa nel mondo, quindi una mappa può avere un'elevata precisione relativa (in termini di dimensioni e forma) ma la sua posizione nel mondo può essere spostata.

![Modello che mostra un'elevata precisione relativa](/images/rel_accuracy.webp)

*Figura 1. Modello che mostra un'elevata precisione relativa ma è fuori posto rispetto alla sua posizione nel mondo reale*

**Precisione assoluta o globale**

L'accuratezza assoluta è l'accuratezza della ricostruzione rispetto alla sua reale posizione sul pianeta (Pix4D 2019). La Figura 2 mostra un modello relativo e assolutamente accurato, poiché i punti sono posizionati correttamente in base alla posizione nel mondo reale.

![Modello che mostra un'elevata precisione assoluta](/images/abs_accuracy.webp)

*Figura 2. Modello che mostra un'elevata precisione relativa e assoluta. Posizionato correttamente in base alla sua posizione nel mondo reale*

**Un livello di precisione per ogni progetto**

Ogni progetto ha esigenze di precisione specifiche da soddisfare. Ad esempio, valutare lo stato di avanzamento di un cantiere o misurare un'area colpita da un incendio non richiede l'uso della GCP, poiché la precisione assoluta non avrà alcun impatto sul processo decisionale. D'altra parte, ci sono compiti in cui la precisione è fondamentale, ad esempio le valutazioni di conformità dei progetti e il rilevamento dei titoli fondiari, che richiedono una maggiore precisione relativa e assoluta.

### Cosa aspettarsi

In termini generali, ci si può aspettare che la precisione relativa sia nell'ordine da 1 a 3 volte il GSD medio per il set di dati. E per quanto riguarda la precisione assoluta, bisogna considerare che dipende dall'unità GPS montata sull'UAV, ma la precisione orizzontale di un GPS standard è solitamente compresa tra 2 e 6 metri e la precisione verticale tra 3 e 4 volte la precisione orizzontale.

Quando si utilizza GCP, la precisione assoluta può essere migliorata a 2,5 volte GSD per la precisione orizzontale e 4 volte GSD per la precisione verticale (Madawalagama 2016).

Con un GSD di 1 cm, la precisione è pari a quella del RTK GNSS ed è entro le scale 1:200 secondo gli standard di precisione della mappatura NSDI e FGDC durante condizioni non ottimali (Barry 2013).

### Aspetti che influiscono sulla precisione della mappa

**Meteo**: le condizioni meteorologiche hanno un impatto diretto sui risultati della fotogrammetria, quindi è importante considerare la copertura nuvolosa, la velocità del vento, l'umidità, l'altitudine del sole e altri fattori che influenzano la stabilità dell'UAV e l'illuminazione del terreno.

**Fotocamere**: sensori più grandi e migliori producono meno rumore e immagini più chiaramente a fuoco. Considerare inoltre che le telecamere con otturatore mobile producono immagini distorte quando l'UAV è in movimento, quindi per i lavori di mappatura si consigliano telecamere con otturatore globale o meccanico.

**Altitudine di volo**: maggiore è l'altitudine di volo, maggiore è l'impronta dell'immagine e il GSD. Con il GSD più grande risultante, la precisione diminuirà poiché ci saranno meno dettagli nelle caratteristiche riconoscibili. Quando è richiesto un GSD più piccolo, si consiglia un'altitudine da 3 a 4 volte l'altezza del punto più alto.

**Velocità di volo**: la velocità di volo ha un effetto speciale nelle fotocamere dotate di otturatore rotante, mentre quelle dotate di otturatore globale o meccanico tendono a ridurre questo effetto. Anche gli UAV dotati di sistemi di posizionamento RTK risentono della velocità, ma passando il mouse su ogni foto scattata è possibile ottenere un'ottima precisione. Se invece ti muovi durante ogni scatto fotografico, la precisione sarà limitata da due fattori: la velocità con cui ti muovi moltiplicata per gli incrementi di 1 secondo di RTK (Mather 2020).

## Miglioramento della precisione relativa

La georeferenziazione per impostazione predefinita viene eseguita utilizzando GPS (GNSS) o GCP (se forniti).

WebODM può anche allineare due attività. Quando ciò accadrà, la ricostruzione verrà inizialmente eseguita utilizzando GPS/GCP e successivamente sarà allineata al modello di riferimento tramite un'operazione di ridimensionamento/rotazione/spostamento lineare.

### Set di dati multitemporali

Quando è necessario rivisitare siti precedentemente mappati, WebODM può allineare più versioni di un set di dati nel tempo utilizzando una nuvola di punti precedente o un modello di elevazione digitale.

**Flusso di lavoro per set di dati multitemporali:**

1. Elabora i tuoi dati originali. Questo passaggio non richiede un file dei punti di controllo a terra, ma utilizzane uno se la precisione assoluta è un requisito del progetto
2. Carica un altro set di dati allineato a quello precedente e cerca l'opzione **Allinea**, quindi seleziona l'attività originale.

### Allineamento di set di dati di grandi dimensioni

Quando si tenta di elaborare set di dati molto grandi, potrebbe essere necessario dividere un ampio set di immagini in blocchi più piccoli e più gestibili per facilitare l'elaborazione. Questo processo, tuttavia, può introdurre qualche incertezza rispetto all’allineamento di tutti gli output elaborati. Per garantire che tutte le nuvole di punti e i modelli di terreno/superficie siano perfettamente allineati in preparazione all'unione, seguiamo le semplici tecniche descritte di seguito.

## File di geolocalizzazione delle immagini

Per impostazione predefinita WebODM utilizzerà le informazioni GPS incorporate nelle immagini, se disponibili. A volte le immagini non contengono informazioni GPS oppure un utente desidera sovrascrivere le informazioni con dati più accurati (come RTK).

Puoi anche utilizzare un file di geolocalizzazione per specificare i centroidi GPS delle immagini.

Il formato del file di geolocalizzazione dell'immagine è semplice.

- La prima riga deve contenere il nome della proiezione utilizzata per le coordinate geografiche. Questo può essere specificato come stringa PROJ (ad esempio `+proj=utm +zone=10 +ellps=WGS84 +datum=WGS84 +units=m +no_defs`), codice EPSG (ad esempio `EPSG:4326`) o come valore `WGS84 UTM <zone>[N|S]` (ad esempio `WGS84 UTM 16N`)
- Le righe successive sono il nome del file immagine, le coordinate X, Y e Z (opzionali), gli angoli della telecamera (opzionali, attualmente utilizzati solo per la calibrazione radiometrica) e la precisione orizzontale/verticale (opzionale)
- Gli angoli della telecamera possono essere impostati su "0" se non sono disponibili
- La decima colonna (facoltativa) può contenere campi aggiuntivi, come un'etichetta

```
<proiezione>
nome file geo_x geo_y [geo_z] [imbardata (gradi)] [beccheggio (gradi)] [rollio (gradi)] [precisione orizzontale (metri)] [precisione verticale (metri)] [extra...]
...

```

Esempio:

```
EPSG:4326
DJI_0028.JPG -91.9942096111111 46.84252125 198.609
DJI_0032.JPG -91.9938293055556 46.8424584444444 198.609
```

Se fornisci un file chiamato "geo.txt", WebODM lo rileverà automaticamente. Se ha un altro nome, puoi specificarlo utilizzando `--geo <path>`.

Il file `geo.txt` deve essere creato nella base della cartella del progetto o, quando si utilizza WebODM, caricato con i file di input grezzi jpg o tif.

## Riferimenti

- Barry, P. e Coakley, R. ["Precisione della fotogrammetria UAV rispetto alla rete RTK GPS."](http://uav.ie/PDF/Accuracy_UAV_compare_RTK_GPS.pdf) Sondaggi di base. 2013.
- Schieramento dei droni. [Come utilizzo i punti di controllo a terra?: Una guida all'utilizzo dei punti di controllo a terra con il software di mappatura dei droni.](https://www.dronedeploy.com/blog/what-are-ground-control-points-gcps/) 2017.
- Madawalagama, S.L., Munasinghe, N., Dampegama, S.D.P.J. e Samarakoon, L. "Mappatura aerea a basso costo di livello consumer". 37a Conferenza asiatica sul telerilevamento. Colombo, Sri Lanka, 2016.
- Mamma, Stephen. [OpenDroneMap.](https://community.opendronemap.org/t/the-accuracy-of-webodm-using-rtk-uavs/3937) 2020.
- Pascual, Manuel S. [GIS Lounge: Dati GIS: uno sguardo ad accuratezza, precisione e tipi di errori.](https://www.gislounge.com/gis-data-a-look-at-accuracy-precision-and-types-of-errors/) 2011.
-Pix4D. ["Che cos'è la precisione in un progetto di mappatura aerea?"](https://www.pix4d.com/blog/accuracy-aerial-mapping) 2019.