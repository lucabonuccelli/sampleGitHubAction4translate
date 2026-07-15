---

titolo: Guida alla selezione delle opzioni
modello: doc
---


Questa guida ti aiuta a scegliere i parametri di elaborazione WebODM più appropriati in base al tuo drone, alle caratteristiche del sondaggio e ai risultati attesi.
Nota: questa guida non è perfetta; trovare i parametri giusti non è sempre un processo deterministico: il più delle volte è un’arte che trascende gli algoritmi.

---

# Passaggio 1: analisi dell'hardware

## Il tuo drone utilizza un Global Shutter o un Rolling Shutter?

### Se utilizzi un drone consumer (DJI Mini, DJI Air, Mavic, ecc.)

**Impostazione consigliata**
- `tapparella: vero`
**Perché?**
I sensori rolling shutter introducono una distorsione geometrica quando le immagini vengono catturate mentre il drone è in movimento.
**Best practice**
Per sondaggi futuri, se possibile:
- ridurre la velocità di volo;
- usa la modalità **Stop-and-Hover** quando scatti fotografie.

---


# Fase 2 - Caratteristiche del sondaggio

## Le immagini includono il cielo o l'orizzonte?
### Se sì
**Impostazione consigliata**
```text
rimozione del cielo: vero
```
### Vantaggi
- Meno rumore di ricostruzione
- Nuvola di punti più pulita
- Migliore qualità della maglia

## Per la ricostruzione di oggetti a distanza ravvicinata
Utilizzo:
```text
bg-rimozione
```
---

# Passaggio 3: scena esaminata
## L'area contiene vegetazione o superfici a bassa consistenza?
Esempi:
- foreste
- praterie
- campi agricoli
- sabbia
- nevicare

**Impostazione consigliata**
```text
numero minimo di funzioni: 20000
```

### Effetto
- aumenta il numero di punti caratteristici rilevabili;
- migliora la robustezza della ricostruzione;
- aumenta il tempo di elaborazione.

---


## Il progetto prevede edifici o strutture verticali?
**Impostazioni consigliate**
```text
qualità PC: alta
```

### Vantaggi
- Ortofoto più accurate
- Migliore ricostruzione delle pareti verticali
- Bordi dell'edificio più nitidi

---


# Passo 4 - Distanza di campionamento del suolo (GSD)
## Hai bisogno di preservare la piena risoluzione nativa della fotocamera?
Quando si vola molto basso (GSD inferiore a circa 2 cm), WebODM può ridurre automaticamente la risoluzione di elaborazione.
Per disattivare questa ottimizzazione:

```text
ignora-gsd: vero
```

### Avvertimento
Ciò aumenta notevolmente:
- Utilizzo della RAM
- Spazio su disco
- Tempo di elaborazione

---


# Passaggio 5: risultato desiderato
## Priorità: mesh 3D dettagliata
Parametro principale:
```text
mesh-octree-profondità
```
Valori consigliati:
| Scenario | Valore |
|----------|------:|

| Terreno pianeggiante | 6–8 |
| Scopo generale | 11|
| Architettura complessa | 12|

Se si aumenta questo valore, aumentare anche:
```text
dimensione della maglia
```
per evitare un’eccessiva semplificazione della mesh.
---


## Priorità: modello digitale del terreno (DTM)

Abilitare:
```text
dtm: vero
```
Regola questi parametri:
| Parametro | Raccomandazione |
|-----------|----------------|

| `smrf-pendenza` | 0,1 per terreno pianeggiante, fino a 1,2 per terreno montuoso |
| `soglia-smrf` | Altezza minima dell'oggetto da rimuovere |

---


## Priorità: elaborazione rapida
Abilitare:
```text
ortofoto veloce: vero
```

### Effetto

Salta la ricostruzione MVS densa e genera l'ortofoto direttamente dalla nuvola di punti sparsa.

---


## Priorità: elaborazione molto veloce

Quando l'obiettivo principale è ottenere un risultato il più rapidamente possibile (ad esempio durante la risposta alle emergenze, una valutazione rapida, una verifica sul campo o un'analisi preliminare), applicare le seguenti ottimizzazioni.

### Consigli per la pianificazione del volo

L'elaborazione più rapida inizia con una strategia di acquisizione ottimizzata:

- Esegui un **volo nadir planare** quando possibile.
- Mantenere un'altitudine costante dal suolo.
- Utilizza una spaziatura regolare delle immagini e una sovrapposizione coerente.
- Evitare immagini oblique non necessarie se l'obiettivo primario è un'ortofoto 2D.
- Evitare di catturare ampie aree al di fuori del confine del rilevamento.
- Utilizzare una traiettoria di volo più lenta e più stabile quando si utilizzano telecamere con tapparella.

---


### Impostazioni WebODM consigliate

#### Utilizza la generazione rapida di ortofoto

```text
ortofoto veloce: vero
```

Genera l'ortofoto senza eseguire la fase completa di ricostruzione densa.

---


#### Ridurre la risoluzione dell'immagine durante l'elaborazione

```text
ridimensiona a: 2048
```

o un valore inferiore a seconda della qualità di output richiesta.

Vantaggi:

- tempi di elaborazione notevolmente ridotti;
- minor consumo di RAM;
- corrispondenza delle funzionalità più rapida.

---


#### Disabilita gli output non necessari

Genera solo i prodotti necessari per l'attività.

Evitare di produrre:
- nuvola di punti densa (la più importante!)
```text
ortofoto veloce: vero
```

- mesh 3D strutturato;
```text
skip-3dmodel: vero
```
- (se non necessari) prodotti DEM.
```text
dsm: falso
dtm: falso
```

- rapporto
```text
skip-report: vero
```


Esempio:

- Mappatura di emergenza → Solo ortofoto
- Ispezione preliminare → Ortofoto + DSM a bassa risoluzione
- Rilievo finale → Flusso di lavoro di elaborazione completo

---


#### Ridurre la densità della nuvola di punti
(solo se ti serve la nuvola di punti)
Utilizzo:

```text
qualità PC: bassa
```

O

```text
qualità PC: media
```

quando non è richiesto un modello 3D dettagliato.

Vantaggi:

- ricostruzione più rapida;
- minore utilizzo del disco.

---


#### Limita la generazione della mesh

Se non è necessaria una mesh:

```text
maglia: falso
```

Evitare la generazione della mesh può far risparmiare una notevole quantità di tempo di elaborazione.

---


### Ulteriori raccomandazioni operative

Per la massima velocità:

1. Carica solo le immagini richieste.
2. Rimuovere le immagini sfocate o duplicate prima dell'elaborazione.
3. Evita immagini con grandi quantità di cielo o sfondi irrilevanti.
4. Utilizzare un flusso di lavoro basato su aree invece di elaborare set di dati molto grandi in una sola volta.
5. Quando possibile, suddividere indagini molto grandi in blocchi indipendenti più piccoli.
6. Utilizzare l'hardware di elaborazione locale con accelerazione GPU quando disponibile.

---

# Passaggio 6: software di destinazione

##QGIS

Abilitare:

```text
panoramiche della build: vero
```

### Nota

Le versioni recenti di ODX generano già GeoTIFF ottimizzati per il cloud (COG) se si utilizza l'opzione `--cog`, che include già panoramiche interne.

---


## Miscelatore

Abilitare:

```text
testurizzazione-monomateriale: vero
gltf: vero
```

### Vantaggi

- Importazione più semplice
- Materiale a trama singola
- Formato 3D compresso moderno

---


## Cesio o visualizzazione Web

Abilitare:

```text
Piastrelle 3D: vero
```

Questo genera tessere 3D ottimizzate adatte allo streaming web.

---


# Passaggio 7: verifica della precisione

## Sono disponibili punti di controllo a terra (GCP)?

Per ottenere una valutazione indipendente dell'accuratezza:

1. Seleziona alcuni punti di controllo come checkpoint.
2. Prefiggi i loro nomi con:

```text
CHK-
```

Osservazioni del punto di controllo:

- non influenzano l'aggiustamento del bundle;
- sono utilizzati esclusivamente per calcolare statistiche di accuratezza indipendenti nel **Rapporto sulla qualità**.



---


# Riferimento rapido

| Situazione | Parametro consigliato |
|------------|-------------|
| Drone di consumo | `tapparella: vero` |
| Drone RTK | `precisione GPS` |
| RTK+GCP | `force-gps: vero` |
| Le immagini includono il cielo | `rimozione del cielo: vero` |
| Vegetazione fitta | `numero-minimo-caratteristiche: 20000` |
| Bordi dell'edificio migliori | `qualità PC: alta` |
| GSD molto basso | `ignore-gsd: vero` |
| Genera DTM | `dtm: vero` |
| Ortofoto veloce | `ortofoto veloce: vero` |
| Esportazione del frullatore | `gltf: vero` |
| Esportazione di cesio | `piastrelle 3d: vero` |
| Convalida della precisione | Punti di controllo `CHK-` |

---

modifica 12 luglio 2026
