---

titolo: Set di dati di grandi dimensioni
modello: doc
---


È possibile suddividere set di dati molto grandi in blocchi gestibili (chiamati sottomodelli), eseguendo il software su ciascun blocco e quindi producendo DEM, ortofoto e nuvole di punti uniti. Il processo è denominato "split-merge".

Perché potresti utilizzare la pipeline split-merge? Se nel set di dati è presente un numero molto elevato di immagini, la suddivisione e l'unione contribuiranno a rendere l'elaborazione più gestibile su una macchina di grandi dimensioni (richiederà meno memoria). Se hai molte macchine tutte connesse alla stessa rete puoi anche elaborare i sottomodelli in parallelo, consentendo così il ridimensionamento orizzontale e l'elaborazione di migliaia di immagini più rapidamente.

L'unione divisa funziona immediatamente in WebODM purché i nodi di elaborazione supportino l'unione divisa, abilitando l'opzione `--split` durante la creazione di una nuova attività.

## Divisione-unione locale

Dividere un set di dati in sottomodelli più gestibili ed elaborare in sequenza tutti i sottomodelli sulla stessa macchina è facile! Basta usare `--split` e `--split-overlap` per decidere rispettivamente il numero medio di immagini per sottomodello e la sovrapposizione (in metri) tra i sottomodelli:

```bash
docker run -ti --rm -v /mio/progetto:/datasets/code webodm/odx --project-path /datasets --split 400 --split-overlap 100
```

Se sai già come suddividere il set di dati, puoi fornire tali informazioni e verranno utilizzate al posto dell'algoritmo di clustering.

Il raggruppamento può essere fornito aggiungendo un file denominato "image_groups.txt" nella cartella principale del set di dati. Il file dovrebbe avere una riga per immagine. Ogni riga dovrebbe contenere due parole: prima il nome dell'immagine e poi il nome del gruppo a cui appartiene. Per esempio:

```
01.jpgA
02.jpgA
03.jpgB
04.jpgB
05.jpg C
```

creerà 3 sottomodelli. Assicurati di passare `--split-overlap 0` se fornisci manualmente un file `image_groups.txt`.

## Divisione-unione distribuita

WebODM può anche distribuire automaticamente l'elaborazione di ciascun sottomodello su più macchine tramite nodi [NodeODX](https://github.com/WebODM/NodeODX), orchestrati tramite [ClusterODX](https://github.com/WebODM/ClusterODX).

![ClusterODX](/images/ClusterODX.webp)

### Iniziare con la suddivisione e l'unione distribuita

Il primo passo è avviare ClusterODX:

```bash
docker esegui -ti -p 3001:3000 -p 8080:8080 webodm/clusterodx
```

Quindi su ogni macchina che desideri utilizzare per l'elaborazione, avvia un'istanza NodeODX tramite:

```bash
docker run -ti -p 3000:3000 webodm/nodeodx
```

Connettiti tramite telnet a ClusterODX e aggiungi gli indirizzi IP/porta delle macchine che eseguono NodeODX:

```bash
$telnet <cluster-odm-ip> 8080
Connesso a <cluster-odm-ip>.
Il carattere di escape è '^]'.
[...]

# nodo aggiungi <nodo-odx-ip-1> 3000
# nodo aggiungi <nodo-odx-ip-2> 3000
[...]

# elenco dei nodi
1) <node-odx-ip-1>:3000 [online] [0/2] <versione 1.5.1>
2) <node-odx-ip-2>:3000 [online] [0/2] <versione 1.5.1>
```

A questo punto, usa semplicemente l'opzione `--sm-cluster` per abilitare l'unione divisa distribuita.

### Comprendere il cluster

Quando si è connessi via telnet, è possibile interrogare cosa sta succedendo sul cluster. Ad esempio, possiamo usare il comando HELP per scoprire i comandi disponibili:

```
# AIUTO
NODE ADD <nome host> <porta> [token] - Aggiungi nuovo nodo
NODE DEL <numero nodo> - Rimuove un nodo
INFO NODO <numero nodo>: visualizza le informazioni sul nodo
ELENCO NODI - Elenca i nodi
NODE LOCK <numero nodo>: interrompe l'inoltro delle attività a questo nodo
NODE UNLOCK <numero nodo>: riprende l'inoltro delle attività a questo nodo
AGGIORNAMENTO NODO: aggiorna le informazioni di tutti i nodi
NODE BEST <numero di immagini> - Mostra il nodo migliore per il numero di immagini
ROUTE INFO <taskId>: trova informazioni sul percorso per l'attività
ELENCO PERCORSI [numero nodo] - Elenca i percorsi
ELENCO ATTIVITA' [numero nodo] - Elenca le attività
TASK INFO <taskId>: visualizza le informazioni sull'attività
TASK OUTPUT <taskId> [linee]: visualizza l'output dell'attività
TASK CANCEL <taskId>: annulla l'attività
TASK REMOVE <taskId>: rimuove l'attività
ASR VIEWCMD <numero di immagini> - Comando di visualizzazione utilizzato per creare una macchina
!! - Ripetere l'ultimo comando
```

Se l'istanza di NodeODX non era attiva all'avvio di ClusterODX, puoi eseguire un `NODE UPDATE`:

```
# AGGIORNAMENTO NODO
OK
# ELENCO NODI
1) localhost:3000 [online] [0/2] <versione 1.5.3> [L]
```

### Accesso ai registri

Mentre un processo è in esecuzione, è anche possibile elencare le attività e visualizzare l'output dell'attività:

```
# ELENCO ATTIVITA'
# TASK OUTPUT <taskId> [righe]
```

### ClusterODX con scalabilità automatica

ClusterODX include anche l'opzione di scalabilità automatica su più piattaforme, tra cui Amazon e Digital Ocean. Ciò consente agli utenti di ridurre i costi associati alle istanze sempre attive e di scalare l'elaborazione in base alla domanda.

Per impostare la scalabilità automatica è necessario:

- Avere installato una versione funzionante di NodeJS e quindi installare ClusterODX:

```bash
git clone https://github.com/WebODM/ClusterODX
cdClusterODX
installazione npm
```

- Assicurati che la docker-machine sia installata.
- Configura un bucket compatibile con S3 per l'archiviazione dei risultati.
- Creare un file di configurazione per [DigitalOcean](https://github.com/WebODM/ClusterODX/blob/master/docs/digitalocean.md) o [Amazon Web Services](https://github.com/WebODM/ClusterODX/blob/master/docs/aws.md).

È quindi possibile avviare ClusterODX con:

```bash
nodo indice.js --asr configurazione.json
```

Dovresti vedere qualcosa di simile ai seguenti messaggi nella console:

```
informazioni: ASR: DigitalOceanAsrProvider
informazioni: può scrivere su S3
informazioni: trovato eseguibile docker-machine
```

Dovresti sempre avere almeno un nodo NodeODX statico collegato a ClusterODX, anche se prevedi di utilizzare il gestore della scalabilità automatica per tutta l'elaborazione. Se imposti la scalabilità automatica, non puoi avere zero nodi e fare affidamento al 100% sulla scalabilità automatica. È necessario collegare un nodo NodeODX che funga da "nodo di riferimento", altrimenti ClusterODX non saprà come gestire determinate richieste. A questo scopo, dovresti aggiungere un nodo NodeODX "fittizio" e bloccarlo:

```bash
telnet localhost 8080
> NODO AGGIUNGI localhost 3001
> BLOCCO NODO 1
> ELENCO NODI
1) localhost:3001 [online] [0/2] <versione 1.5.1> [L]
```

In questo modo tutte le attività verranno automaticamente inoltrate all'autoscaler.

## Limitazioni

Le mesh con texture 3D attualmente non vengono unite come parte del flusso di lavoro (lo sono solo nuvole di punti, DEM e ortofoto).

I GCP sono completamente supportati, tuttavia, affinché venga eseguita la georeferenziazione, è necessario che siano presenti almeno 3 punti GCP su ciascun sottomodello. Se un sottomodello ha meno di 3 GCP, verrà utilizzata invece una combinazione dei GCP rimanenti + dati EXIF ​​(che sarà meno precisa). Ti consigliamo di utilizzare il file "image_groups.txt" per controllare con precisione la suddivisione del sottomodello quando utilizzi GCP.

## Stima dello sforzo di raccolta dati

Set di dati più grandi possono essere raccolti con UAV specializzati ad ala fissa, UAV a decollo e atterraggio verticale (VTOL) e raccolti in modo abbastanza efficiente in determinate condizioni. In molti casi, tuttavia, siamo costretti a svolgere attività di raccolta dati con quadricotteri commerciali. In questi casi, una domanda comune è il tempo di raccolta dei dati in condizioni ideali con apparecchiature di base.

### Sforzo di raccolta dati, 3D completo

Per ottenere i migliori risultati con ricostruzione 3D completa e risoluzione di 5 cm, è possibile raccogliere 1–2 km² per persona, al giorno. Ciò richiede il seguente insieme di voli:

- 60% di sovrapposizione del volo nadir
- Griglia incrociata con angolo gimbal di sovrapposizione del 70-80%.

Il volo a griglia incrociata a 45 gradi fornisce la base per un modello completamente collegato, mentre i voli al nadir forniscono la texture necessaria per la texturizzazione delle ortofoto. La sovrapposizione inferiore soddisfa i requisiti minimi per i prodotti ortofoto, come facilitato dalla corrispondenza delle caratteristiche della griglia incrociata con sovrapposizione molto più alta.

### Sforzo di raccolta dati, prodotti 2D e 2.5D

Per ottenere i migliori risultati della categoria per prodotti 2D e 2,5D e una risoluzione di 5 cm, è possibile raccogliere 2–4 km² per persona, al giorno. Ciò richiede il seguente insieme di voli:

- Il 70-80% si sovrappone leggermente fuori dal nadir (5-10 gradi fuori dal nadir)

Per edifici e vegetazione più complessi, puntare a una sovrapposizione più vicina all'80%. Se gli edifici, la vegetazione e i cambiamenti del terreno non sono complessi, è abbastanza fattibile utilizzare una sovrapposizione più vicina al 70%.

*(credito: derivato dalle conversazioni in corso con Ivan Gayton, Humanitarian OpenStreetMap Team)*

## Ringraziamenti

Enormi complimenti a Pau, Yann e ai ragazzi di Mapillary per il loro straordinario contributo a OpenSfM, che è un componente chiave del processo di split-merge.
