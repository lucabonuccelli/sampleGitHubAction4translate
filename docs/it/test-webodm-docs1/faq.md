---

titolo: Domande frequenti
modello: doc
---


## Qual è la relazione tra WebODM e OpenDroneMap?

WebODM faceva parte del progetto OpenDroneMap. Dal 2026, WebODM non è più affiliato o connesso a OpenDroneMap. Sono due progetti separati.

## Il software non utilizza sempre tutti i core/memoria/GPU della CPU. È normale?

SÌ. Il software cerca di utilizzare tutte le risorse disponibili, quando possibile, ma non sempre. È normale vedere un utilizzo della CPU del 10-15% in diversi momenti durante l'elaborazione e un utilizzo della GPU dello 0% per molte volte.

## Come posso ottenere le mappe con la risoluzione più alta?

Imposta [ortofoto-risoluzione](/options-flags/#orthophoto-risoluzioni) e [dem-risoluzione](/options-flags/#dem-risoluzione) su un valore basso come "0.01".

## Dove sono archiviati i miei file?

Quando si utilizza Docker, tutti i risultati dell'elaborazione vengono archiviati in un volume docker e non sono disponibili sul file system host. Esistono due volumi docker specifici di interesse:
1. Media (chiamato webodm_appmedia): qui sono archiviati tutti i file relativi a un progetto e un'attività.
2. Postgres DB (chiamato webodm_dbdata): questo è ciò che il database Postgres utilizza per archiviare i suoi dati.

Per ulteriori informazioni su come vengono utilizzati questi due volumi e in quali contenitori, fare riferimento al file [docker-compose.yml](https://github.com/WebODM/WebODM/blob/master/docker-compose.yml).

Per vari motivi, come la facilità di backup/ripristino, se desideri archiviare i tuoi file sul file system host anziché su un volume docker, devi passare un percorso tramite le opzioni `--media-dir` e/o `--db-dir`:

```bash
./webodm.sh riavvio --media-dir /home/utente/webodm_data --db-dir /home/utente/webodm_db
```

Tieni presente che i risultati delle attività esistenti non saranno disponibili dopo la modifica. Fare riferimento alla sezione [Migrazione dei volumi di dati](https://docs.docker.com/engine/tutorials/dockervolumes/#backup-restore-or-migrate-data-volumes) della documentazione di Docker per informazioni sulla migrazione dei risultati delle attività esistenti.

## Posso elaborare due o più GeoTIFF di ortofoto per unirli insieme?

No. WebODM è un software fotogrammetrico e le ortofoto non hanno le informazioni necessarie sulla fotocamera poiché le immagini sono già state ortorettificate. Puoi usare questo [plug-in QGIS](https://github.com/uav4geo/QRasterMerge) per farlo.

## Se utilizzo la versione nativa del software, come posso allocare più risorse per l'elaborazione?

Non c'è bisogno; la versione nativa (non docker) del software utilizza già tutte le risorse disponibili.

## Voglio creare un'applicazione commerciale che includa WebODM. Ho bisogno di una licenza commerciale?

WebODM è un software gratuito e open source, rilasciato sotto [AGPLv3](https://github.com/WebODM/WebODM/blob/master/LICENSE.md). Sei libero di creare e vendere applicazioni con esso, assicurati solo di rispettare i requisiti della licenza, in particolare il requisito di divulgazione della fonte e di seguire le nostre [linee guida sui marchi](https://github.com/WebODM/WebODM/blob/master/TRADEMARK.md).

## Esistono altre opzioni di licenza oltre a AGPLv3?

No, mi spiace!

## La memoria del tuo computer sta esaurendo. Cosa puoi fare?

1. Per prima cosa puoi acquistare più RAM, questa è la soluzione definitiva e definitiva.
2. In alternativa puoi ridimensionare le immagini durante il caricamento e/o modificare le impostazioni di qualità.
3. Configurare un file di scambio. Sia in Windows che in Linux avrai bisogno preferibilmente di un SSD veloce o di un'unità NVME, e il processo di calcolo sarà ancora MOLTO più lento.

- Se utilizzi Windows con [Docker+WSL2](https://docs.docker.com/desktop/windows/wsl/) puoi aggiungere due righe nel file .wslconfig in modo che Docker utilizzi un file di scambio. Consulta anche la documentazione Microsoft completa su [Configurazione delle impostazioni avanzate in WSL](https://docs.microsoft.com/en-us/windows/wsl/wsl-config).

```
scambio=128GB
file di scambio=C:\temp\wsl-swap.vhdx
```

- In Linux è possibile aggiungere un file di swap o una partizione dedicata allo swap. Per ulteriori informazioni, consulta il tuo motore di ricerca preferito poiché esistono molte distribuzioni e metodi diversi per aggiungere lo swap.

