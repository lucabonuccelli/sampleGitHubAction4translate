---

titolo: Utilizzo di Podman
---


In alternativa a Docker, è possibile scegliere di eseguire WebODM utilizzando [Podman](https://podman.io). Per fare ciò, installa semplicemente il pacchetto podman della tua distribuzione e il suo livello di compatibilità per docker. Ad esempio, su Alpine Linux:

```bash
apk aggiungi podman podman-docker
```

La riga di comando di Podman ha una forte somiglianza con quella di Docker, quindi fare riferimento alla sezione precedente e sostituire ogni invocazione del comando "docker" con "podman" è probabilmente sufficiente per insegnarne l'uso di base.

### Migrazione da Docker a Podman

Sfortunatamente, dato il numero di opzioni che `webodm.sh` fornisce per la distribuzione, la migrazione tra i due potrebbe richiedere del lavoro manuale prima di cambiare piattaforma. Se le informazioni di WebODM sono state archiviate in directory utilizzando i flag `--media-dir` e `--db-dir`, i dati al loro interno devono essere di proprietà dell'utente che esegue i contenitori Podman. Se esegui senza root, assicurati di impostarlo sul tuo utente corrente. Dovresti essere sicuro di chownare ricorsivamente l'intero repository git come tale se il tuo `media-dir` e `db-dir` risiedono al suo interno:

```bash
sudo chown -R $(whoami) WebODM
```

Se `webodm.sh` è stato utilizzato senza flag, è necessario un intervento diverso per migrare i propri dati.

```bash
esportazione volume docker webodm-dbdata > webodm-dbdata.tar
esportazione del volume docker webodm-appmedia > webodm-appmedia.tar
```

Indipendentemente dalla posizione dei dati, ora dovrai disinstallare completamente Docker dal tuo sistema in base alla documentazione del tuo sistema operativo. Tieni presente che, per impostazione predefinita, lo script `webodm.sh` potrebbe essersi preso la libertà di installare docker-compose per te. Per ripulirlo, esegui quanto segue:

```bash
rm ~/.docker/cni-plugins-docker-compose
```

Ora installa Podman secondo la documentazione del tuo sistema operativo. Se prima avevi bisogno di esportare i file multimediali e le directory db da Docker, ora puoi utilizzarlo per importare i volumi.

```bash
podman volume importa webodm-dbdata webodm-dbdata.tar
podman volume import webodm-appmedia webodm-appmedia.tar
```

Si consiglia di disconnettersi e accedere nuovamente al sistema a questo punto per garantire che tutte le variabili di ambiente siano originate correttamente.

L'esecuzione di "webodm.sh" ora dovrebbe comportare la persistenza dei dati utente tra lo switch.

### Per le versioni di podman-compose < 1.5.0

Le versioni podman-compose precedenti alla 1.5.0 non supportano le variabili di ambiente nei file docker-compose. Se la tua distribuzione non fornisce una versione aggiornata nei suoi repository, puoi scegliere di fornire il tuo binario aggiornato o utilizzare [Docker Compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually) con podman stesso. In entrambi i casi, dovrai aggiornare la riga compose_provviders del file `/etc/containers/containers.conf`.

Se scegli di utilizzare Docker Compose invece di podman-compose, potresti dover configurare alcune variabili di ambiente aggiuntive per indicare a WebODM dove inviare le richieste API Docker. La seguente configurazione dell'ambiente ha comportato la generazione corretta di WebODM in Alpine Linux 3.22, sebbene dovrebbe essere abbastanza agnostico tra le distribuzioni.

```bash
esporta WEBODM_PODMAN_SOCKET=$(informazioni podman --format '{{.Host.RemoteSocket.Path}}')
mkdir -p $(nomedir WEBODM_PODMAN_SOCKET)
esporta DOCKER_HOST=unix://$WEBODM_PODMAN_SOCKET
```

Infine, avvia WebODM come tale:

```bash
servizio di sistema podman --time=0 unix://$WEBODM_PODMAN_SOCKET & ./webodm.sh avvio
```

### Configurazione di Podman per l'esecuzione senza root

Uno dei principali vantaggi derivanti dall'utilizzo di Podman anziché Docker è dovuto alla sua capacità di funzionare senza root. Il tuo sistema operativo specifico potrebbe o meno configurarlo manualmente, ma puoi trovare istruzioni generiche su come farlo [nella documentazione ufficiale di Podman](https://docs.podman.io/en/latest/markdown/podman.1.html#rootless-mode). Per supporre, l'esecuzione dei seguenti comandi è probabilmente ciò che dovrai fare:

```bash
sudo usermod --add-subuids 10000-75535 $(whoami)
sudo usermod --add-subgids 10000-75535 $(whoami)
```

###macOS

In teoria, [installare](https://podman-desktop.io/docs/installation/macos-install) ed eseguire Podman Desktop dal sito Web ufficiale dovrebbe essere tutto ciò che serve per utilizzare lo script `webodm.sh`. Installalo e configuralo sia per la [compatibilità Docker](https://podman-desktop.io/docs/migrating-from-docker/customizing-docker-compatibility#enable-docker-compatibility) che per la [funzionalità Compose](https://podman-desktop.io/docs/compose/setting-up-compose).
