---

titolo: Misurazione delle scorte
---


### Pianificazione del lavoro sul campo

Le condizioni meteorologiche modificano l'illuminazione e quindi incidono sui risultati della fotografia. I migliori risultati si ottengono con cieli uniformemente nuvolosi o sereni. Cerca anche velocità del vento basse che consentano alla fotocamera di rimanere stabile durante il processo di raccolta dei dati.

Per evitare ombre che su un lato della pila possano ostacolare il rilevamento degli elementi e diminuire il numero di punti risultanti, preferire sempre i voli durante il mezzogiorno, quando il sole è al nadir in modo che tutto sia costantemente illuminato.

Assicurati inoltre che la distanza di visibilità orizzontale a occhio nudo sia congruente con le distanze di volo pianificate per il progetto specifico, in modo che la qualità dell'immagine non venga influenzata negativamente da polvere, nebbia, fumo, cenere vulcanica o inquinamento.

### Schema di volo

La maggior parte dei lavori di misurazione delle scorte non richiedono uno schema a tratteggio incrociato o un giunto cardanico angolato poiché l'angolo di riposo dei materiali delle scorte consente alla fotocamera di catturare l'intero lato della scorta. Solo alcuni casi speciali in cui l'erosione o le operazioni dei macchinari provocano angoli ripidi sulle facce del cumulo trarrebbero vantaggio dal modello di volo a tratteggio incrociato e dal gimbal angolato della fotocamera, ma si consideri che queste caratteristiche aggiuntive riconosciute hanno un costo (in termini di lavoro sul campo e tempo di lavorazione) e i miglioramenti risultanti sono talvolta trascurabili.

Nella maggior parte dei casi il modello di volo di un tosaerba è in grado di produrre modelli di scorte altamente accurati.

![Schema di volo del rasaerba](/images/lawnmower_pattern.webp)

La sovrapposizione consigliata sarebbe compresa tra il 75% e l'80% con una sovrapposizione laterale nell'ordine dal 65% al ​​70%. Si consiglia inoltre di aumentare leggermente la sovrapposizione e la sovrapposizione laterale man mano che aumenta l'altezza del volo.

### Altezza del volo

L'altezza del volo può essere influenzata da diversi modelli di fotocamera, ma in generale e per garantire un equilibrio tra qualità dell'immagine e ottimizzazione del volo, si consiglia di eseguirlo ad altezze da 3 a 4 volte l'altezza della scorta più alta. Quindi, per una scorta di 10 metri, le immagini possono essere catturate ad un'altezza di 40 metri.

Man mano che l'altezza di volo aumenta, si consiglia anche di aumentare la sovrapposizione, quindi per un volo di altezza di 40 metri è possibile impostare una sovrapposizione laterale del 65% e una sovrapposizione del 75%, ma per un'altezza pianificata di 80 metri una sovrapposizione laterale del 70% e dell'80% consente di riconoscere ed elaborare correttamente le caratteristiche.

### GCP

Per ottenere livelli di precisione migliori del 3%, si consiglia l'uso di GCP. In genere 5 GCP distribuiti sono sufficienti per garantire risultati accurati. Quando si posiziona o si misura il GCP, la precisione dell'apparecchiatura deve essere maggiore del GSD. Il GNSS di livello topografico e le stazioni totali hanno lo scopo di fornire la precisione millimetrica richiesta.

Per ulteriori informazioni sull'uso dei GCP, fare riferimento alla [sezione Punti di controllo a terra](/ground-control-points/).

### Parametri di elaborazione

È possibile ottenere un modello estremamente accurato utilizzando le impostazioni predefinite ad alta risoluzione WebODM. Quindi è possibile regolare ulteriormente alcuni parametri secondo necessità.

Questi valori di riferimento possono aiutarti a configurare le impostazioni del processo:

- `--dsm`: vero
- "--dem-risoluzione": 2.0
- `--risoluzione-ortofoto`: 1.0
- "--qualità delle funzionalità": alta
- "--qualità-pc": alta

### Misurare

Poiché quasi il 50% del materiale si troverà nel primo 20% dell'altezza del cumulo, è necessario prestare particolare attenzione nel definire adeguatamente il piano di base.

![Distribuzione dell'altezza delle scorte](/images/stockpile.webp)

Nella dashboard WebODM, fai clic su "visualizza mappa" per avviare una visualizzazione 2D del tuo progetto.

Una volta nella vista della mappa 2D, fai clic sul pulsante "Misura volume, area e lunghezza".

![Pulsante Misura volume](/images/measurement1.webp)

Quindi fare clic su "Crea una nuova misurazione".

![Crea una nuova misurazione](/images/measurement2.webp)

Iniziare a posizionare i punti per definire il piano base della scorta.

![Definire il piano base della scorta](/images/measurement3.webp)

Fare clic su "Termina misurazione" per completare il processo.

![Termina la misurazione](/images/measurement4.webp)

La finestra di dialogo mostrerà il messaggio "Calcolo in corso..." per alcuni secondi e al termine del calcolo verrà visualizzato il valore di misurazione del volume.

![Risultato della misurazione del volume](/images/measurement7.webp)

Se si utilizza la riga di comando è possibile utilizzare i file dsm per misurare i volumi delle scorte utilizzando altri programmi.

Considera anche che una volta impostati i limiti della scorta in un software come [QGIS](https://www.qgis.org), scoprirai che ci sono alcuni modi per determinare il piano di base. Pertanto, per le scorte isolate i cui confini sono per lo più visibili, è possibile utilizzare un approccio lineare. Mentre per i cumuli disposti su pendii o in contenitori, il piano di base è meglio definito dal punto più basso. Per cumuli di grandi dimensioni si consiglia la creazione di una superficie 3D triangolata per definire il piano di base. Ciò vale anche per le scorte collocate su superfici irregolari.

### Precisione prevista

Per progetti attentamente pianificati ed eseguiti, e specialmente quando GSD è inferiore a 1 cm, la precisione prevista dovrebbe essere compresa tra l'1% e il 2%. La precisione risultante è paragonabile al software di fotogrammetria disponibile in commercio e a quella ottenuta utilizzando apparecchiature GNSS di livello topografico.
