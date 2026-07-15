---

titolo: Usare la singolarità
---


[Singularity](https://sylabs.io/) è un'altra piattaforma contenitore in grado di eseguire immagini Docker. Singularity può essere eseguito sia su macchine locali che in istanze in cui l'utente non ha accesso root. Le istanze in cui un utente potrebbe non avere privilegi root includono cluster HPC e risorse cluster cloud. Un contenitore è un singolo file senza nient'altro da installare.

### Crea un'immagine della singolarità dall'immagine Docker

Singularity può utilizzare l'immagine Docker per creare un'immagine SIF.

Per l'immagine Docker ODX più recente (consigliato):

```bash
build singolarità --disable-cache -f odx_latest.sif docker://webodm/odx:latest
```

### Utilizzo dell'immagine SIF della singolarità

Dopo aver utilizzato uno dei comandi precedenti per scaricare e creare l'immagine `odx_latest.sif`, è possibile eseguirla utilizzando la singolarità. Inserisci le tue immagini in una directory denominata "images" (ad esempio `/my/project/images`), quindi esegui semplicemente:

```bash
esecuzione della singolarità --bind /mio/progetto:/datasets/code odx_latest.sif --project-path /datasets
```

Come con la finestra mobile, è possibile aggiungere opzioni e flag aggiuntivi al comando:

```bash
esecuzione della singolarità --bind /mio/progetto:/dataset/codice \
--writable-tmpfs odx_latest.sif \
--orthophoto-png --mesh-octree-profondità 12 --dtm \
--smrf-threshold 0.4 --smrf-window 24 --dsm --pc-csv --pc-las --orthophoto-kmz \
--matcher-type flann --feature-quality ultra --max-concurrency 16 \
--use-hybrid-bundle-adjustment --build-overviews --time --min-num-features 10000 \
--percorso-progetto /dataset
```

### ClusterODX, NodeODX, SLURM, con Singularity su HPC

Puoi scrivere uno script SLURM per pianificare e configurare i nodi disponibili con NodeODX affinché ClusterODX venga collegato se ti trovi sull'HPC. L'utilizzo di SLURM ridurrà la quantità di tempo e i processi necessari per configurare ogni volta i nodi per ClusterODX.

Per configurare HPC con SLURM, è necessario assicurarsi che SLURM sia installato.

Lo script SLURM sarà diverso da cluster a cluster, a seconda dei nodi del cluster di cui disponi. Tuttavia, l'idea principale è eseguire NodeODX su ciascun nodo una volta e, per impostazione predefinita, ciascun NodeODX verrà eseguito sulla porta 3000. Successivamente, eseguire ClusterODX sul nodo principale e connettere i NodeODX in esecuzione al ClusterODX.

Ecco un esempio di uno script SLURM che assegna i nodi 48, 50, 51 per eseguire NodeODX:

```bash
#!/usr/bin/bash
#SBATCH --partizione=8core
#SBATCH --nodelist-nodo [48,50, 51]
#SBATCH --ore 20:00:00

cd $CASA
cdODX/NodeODX/

# Avvia sul nodo 48
srun --nodes-1 apptainer esegui --writable node/ &

# Avvia sul nodo 50
srun --nodes-1 apptainer esegui --writable node/ &

# Avvia sul nodo 51
srun --nodes=1 apptainer esegui --writable node/ &
Aspettare
```

Puoi controllare i nodi disponibili usando `sinfo`, eseguire lo script con `sbatch sample.slurm` e controllare i lavori in esecuzione con `squeue -u $USER`.

SLURM non gestisce l'assegnazione di lavori al nodo head, quindi esegui ClusterODX localmente. Quindi connettiti alla CLI e collega i NodeODX a ClusterODX:

```bash
telnet localhost 8080
> NODO AGGIUNGI nodo48 3000
> NODO AGGIUNGI nodo50 3000
> NODO AGGIUNGI nodo51 3000
> ELENCO NODI
```

È anche possibile prepopolare i nodi utilizzando JSON. Se si avvia ClusterODX da apptainer o docker, il relativo JSON è disponibile in `docker/data/nodes.json`:

```json
[

{"hostname":"node48","port":"3000","token":""},
{"hostname":"node50","port":"3000","token":""},
{"hostname":"node51","port":"3000","token":""}
]

```

Dopo aver ospitato ClusterODX sul nodo principale e averlo collegato a NodeODX, puoi eseguire il tunneling per vedere se ClusterODX funziona come previsto:

```bash
ssh -L localhost:10000:localhost:10000 utente@nomehost
```

Apri un browser e connettiti a "http://localhost:10000" (la porta 10000 è dove è ospitata l'interfaccia web amministrativa di ClusterODX).

Quindi tunnela la porta 3000 per l'assegnazione delle attività:

```bash
ssh -L localhost:3000:localhost:3000 utente@nomehost
```

Connettiti a "http://localhost:3000" per assegnare compiti e osservare i processi.
