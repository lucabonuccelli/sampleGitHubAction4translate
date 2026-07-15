---

titolo: Utilizzo del visualizzatore 3D
---


### Fotocamere

Attivare questa funzione per visualizzare le posizioni della telecamera.

Puoi anche fare clic sull'icona della fotocamera per visualizzare le singole immagini in una cornice nell'angolo in alto a destra. Un clic sulla cornice dell'immagine attiva la modalità a schermo intero.

All'interno della cornice dell'immagine sono presenti collegamenti per scaricare l'immagine e il file della fotocamera GeoJSON.

![Posizioni delle telecamere](/images/cameras.webp)

### Modello strutturato

Attiva questa funzione per mostrare il caricamento del modello con texture. A seconda delle dimensioni del file e della velocità di connessione, il caricamento potrebbe richiedere diversi secondi.

![Modello con texture](/images/texturingmodel.webp)

### Aspetto

#### Budget in punti

Sia per scopi di aspetto che di performance, è possibile gestire il budget dei punti sulla scena. Alcune macchine vecchie e meno capaci trarrebbero vantaggio da un budget di 500.000 punti, mentre la maggior parte delle macchine con specifiche di fascia media sono in grado di gestire un budget da 1 a 2 milioni di punti.

Un budget compreso tra 5 e 7 milioni di punti produce un modello 3D della nuvola di punti uniforme, ma può comportare un processo ad alto dispendio di risorse.

Il valore del budget punti predefinito è impostato su 1.000.000.

#### Campo visivo

Per controllare gli elementi del modello da includere nella scena è possibile regolare il campo visivo. Il valore predefinito è impostato su 60 gradi.

![Regolazione del campo visivo](/images/FOV_animation.webp)

#### Illuminazione Eye Dome

Il modulo visualizzatore 3D Potree Point Cloud può implementare l'illuminazione a cupola degli occhi, un modello di illuminazione che accentua le forme degli oggetti.

L'illuminazione Eye Dome raggruppa gli oggetti, ne ombreggia i contorni e migliora la percezione della profondità nelle immagini di visualizzazione scientifica. È utile per il riconoscimento e la misurazione delle strutture all'interno di un modello. Può essere modificato regolando Raggio, Intensità e Opacità.

Per impostazione predefinita, Eye Dome-Lighting è abilitato sul visualizzatore Potree 3D, ma può essere disabilitato facendo clic sull'opzione abilita.

![Regolazione illuminazione cupola oculare](/images/EDL_animation.webp)

#### Sfondo

Lo sfondo del visualizzatore 3D di Potree può essere modificato. Le opzioni disponibili sono **Skybox** / **Gradiente** / **Nero** / **Bianco** / **Nessuno**

![Selezione sfondo](/images/Background_animation.webp)

#### Altro

**Qualità simbolo**: la qualità simbolo può essere regolata su standard o alta, per migliorare l'aspetto del modello.

**Dimensione minima del nodo**: l'opzione relativa alla dimensione minima del nodo influirà sulla densità dei punti dei nodi rappresentati.

**Box** — Visualizza i box dei nodi.

**Blocca vista**: blocca la vista della nuvola di punti, impedendo di caricare o scaricare punti nel modello.

### Utensili

#### Misurazione

Il modulo visualizzatore 3D Potree fornisce diversi strumenti per la misurazione. Questo set di strumenti è composto da 12 elementi. Dispone inoltre di controlli per mostrare o nascondere le etichette di misurazione risultanti.

Le misurazioni vengono eseguite facendo clic con il pulsante sinistro del mouse sui punti desiderati e per alcuni strumenti è necessario fare clic con il pulsante destro del mouse per terminare il processo.

![Strumenti di misurazione](/images/measurement.webp)

**Angolo** — Questo strumento misura l'angolo tridimensionale formato dalle linee che collegano 3 punti. Per avviare una misurazione, fare clic sull'icona dell'angolo, quindi fare clic con il pulsante sinistro del mouse su 3 punti e il processo verrà terminato automaticamente. Ulteriori informazioni possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Punto** — Questo strumento evidenzia un punto selezionato e ne visualizza le coordinate XYZ. Per avviare una misurazione, fare clic sull'icona del punto, quindi fare clic sul punto desiderato e il processo verrà terminato automaticamente. Ulteriori informazioni possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Distanza** — Questo strumento misura la distanza tridimensionale delle linee che collegano una serie di punti. Per avviare una misurazione, fare clic sull'icona della distanza e iniziare a fare clic sui punti desiderati (due o più). Fare clic con il tasto destro per terminare la misurazione. Ulteriori informazioni come la Lunghezza totale possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Altezza**: questo strumento misura l'altezza o la distanza verticale tra due punti. Per avviare una misurazione, fare clic sull'icona dell'altezza e quindi fare clic sui due punti desiderati. Il processo verrà terminato automaticamente. Ulteriori informazioni possono essere ottenute anche selezionando questo elemento nella sezione scena.

![Misurazione dell'altezza](/images/height_animation.webp)

**Cerchio** — Questo strumento misura il raggio di un cerchio formato da tre punti. Per avviare una misurazione, fare clic sull'icona del cerchio e quindi fare clic sui due punti desiderati. Il processo verrà terminato automaticamente. Ulteriori informazioni come la Circonferenza possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Azimut**: questo strumento misura l'angolo azimutale di una linea. Questa linea è formata da due punti selezionati dall'utente, l'angolo si misura in gradi, in senso orario da 0 a 360 e partendo dal nord geografico. Per avviare una misurazione, fare clic sull'icona dell'azimut e quindi fare clic sui due punti desiderati. Il processo verrà terminato automaticamente. Ulteriori informazioni possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Area** — Questo strumento misura l'area orizzontale formata da un poligono. Per avviare una misurazione, fare clic sull'icona dell'area e iniziare a fare clic sui punti che formano il poligono desiderato (tre o più). Fare clic con il tasto destro per terminare la misurazione. Ulteriori informazioni possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Volume (cubo)** — Questo strumento misura il volume formato da un cubo. Per avviare una misurazione, fare clic sull'icona del volume (cubo) e fare clic sul modello per posizionare il cubo. È possibile riposizionare, ridimensionare e ruotare il cubo utilizzando i gestori visualizzati. Fare clic con il tasto destro per terminare la misurazione. Ulteriori informazioni possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Volume (sfera)** — Questo strumento misura il volume formato da una sfera. Per avviare una misurazione, fare clic sull'icona del volume (sfera) e fare clic sul modello per posizionare la sfera. È possibile riposizionare, ridimensionare e ruotare la sfera utilizzando i gestori visualizzati. Fare clic con il tasto destro per terminare la misurazione. Ulteriori informazioni possono essere ottenute anche selezionando questo elemento nella sezione scena.

**Profilo altezza** — Questo strumento crea un profilo altezza formato da una linea sul modello. Per avviare una misurazione, cliccare sull'icona Profilo altezza e poi formare una linea sul modello cliccando sui punti desiderati (due o più). Fare clic con il tasto destro per terminare la misurazione. Ulteriori informazioni e opzioni, come ad esempio "Mostra profilo 2d", possono essere ottenute anche selezionando questo elemento nella sezione scena.

![Profilo altezza](/images/height_profile.webp)

**Annotazione**: questo strumento crea un'etichetta di annotazione su un punto evidenziato sul modello. Per avviare una misurazione, fare clic sull'icona dell'annotazione e quindi fare clic sul punto desiderato. Il processo verrà terminato automaticamente. Per modificare l'annotazione, seleziona questo elemento nella sezione scena, quindi modifica Titolo e Descrizione.

**Rimuovi misurazioni**: questo strumento rimuove tutte le misurazioni sul modello. Per rimuovere tutte le misurazioni, fare clic sull'icona "Rimuovi misurazioni".

#### Ritaglio

![Strumenti di ritaglio](/images/clipping.webp)

La nuvola di punti può essere ritagliata selezionando un'area. Le opzioni di ritaglio includono **Nessuno** / **Evidenzia** / **Interno** / **Esterno**

Per ritagliare una nuvola di punti, fare clic sull'icona di clip del volume, posizionare il cubo sul modello e riposizionare, ridimensionare e ruotare per contenere l'area desiderata. L'evidenziazione è impostata per impostazione predefinita come metodo di ritaglio. Se vengono visualizzati solo i punti contenuti all'interno del cubo cliccare su "Interno", altrimenti cliccare su "Esterno".

Per rimuovere il volume di ritaglio o i poligoni, fare clic sull'icona "Rimuovi tutte le misurazioni".

![Ritaglio](/images/clipping_animation.webp)

#### Navigazione

![Controlli di navigazione](/images/navigation.webp)

Il visualizzatore 3D Potree dispone di 4 controlli di navigazione che ne definiscono il comportamento.

**Controllo della Terra**: il controllo della Terra naviga come se fosse ancorato al suolo. Il pulsante sinistro del mouse sposta il modello orizzontalmente, la rotellina del mouse controlla lo zoom e il pulsante destro ruota attorno al modello.

**Controllo del volo**: il controllo del volo sposta la telecamera come a volo d'uccello utilizzando la tastiera. I tasti "W" e "S" si muovono rispettivamente avanti e indietro e nella direzione della telecamera, mentre "A" e "D" si muovono rispettivamente a sinistra e a destra. Inoltre, i tasti "R" e "F" muovono la telecamera su e giù. Il pulsante sinistro del mouse cambia la direzione della telecamera, la rotellina del mouse controlla lo zoom e il pulsante destro sposta la telecamera sull'asse XYZ. La velocità di questi movimenti può essere controllata utilizzando il controllo scorrevole.

**Controllo dell'elicottero**: il controllo dell'elicottero sposta la telecamera come su un aereo utilizzando la tastiera. I tasti "W" e "S" si muovono avanti e indietro, rispettivamente vincolati su un piano orizzontale, mentre "A" e "D" si muovono rispettivamente a sinistra e a destra. Inoltre, i tasti "R" e "F" muovono la telecamera su e giù. Il pulsante sinistro del mouse cambia la direzione della telecamera, la rotellina del mouse controlla lo zoom e il pulsante destro sposta il modello sull'asse XY. La velocità di questi movimenti può essere controllata utilizzando il controllo scorrevole.

**Controllo dell'orbita**: il controllo dell'orbita è il comportamento di navigazione predefinito. Il pulsante sinistro del mouse ruota attorno al modello, la rotella controlla lo zoom e il pulsante destro sposta il modello sull'asse XYZ.

**Estensione completa**: il pulsante Estensione completa ripristina la vista del modello.

**Cubo di navigazione**: il cubo di navigazione visualizza un cubo wireframe contenente il modello.

**Bussola**: il pulsante Bussola visualizza una bussola nell'angolo in alto a destra.

**Animazione della fotocamera**: il pulsante di animazione della fotocamera crea un percorso di animazione della fotocamera. La posizione della telecamera è definita dai punti sulla linea verde mentre i punti sulla linea blu indicano la posizione verso cui si intende guardare la telecamera. Per creare un'animazione, regola i punti per le posizioni e la direzione della telecamera, quindi seleziona l'elemento della telecamera nella sezione Scena per creare più punti, modificare la velocità dell'animazione o riprodurre l'animazione.

![Animazione fotocamera](/images/camera_animation.webp)

### Scena

La sezione Scena visualizza un albero di file contenente tutti gli elementi della scena. Gli elementi sono organizzati in sei gruppi, ovvero **Nuvole di punti** / **Misurazioni** / **Annotazioni** / **Altro** / **Vettore** / **Immagini**

Ciascun elemento di questi gruppi può essere selezionato per ottenere ulteriori informazioni o per controllarne le proprietà.

Ad esempio, le proprietà delle nuvole di punti possono essere modificate per mostrare l'elevazione e anche la scala di colori può essere personalizzata.

![Elevazione della nuvola di punti](/images/pointcloud_elevation.webp)
