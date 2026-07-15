---

titolo: Installazione
modello: doc
---


:::suggerimento[Lo sapevi?]

Puoi saltare l'installazione ed eseguire WebODM da [webodm.net](https://webodm.net), che supporta lo sviluppo del software ❤ Provalo [gratuitamente](https://webodm.net).

:::


## Installazione sul tuo computer

Se utilizzi Windows o macOS, il modo più semplice è [scaricare](https://webodm.org/download) il programma di installazione per la tua piattaforma da [webodm.org](https://webodm.org).

Se utilizzi Linux, devi utilizzare la finestra mobile (vedi sotto).

:::nota

OpenDroneMap, a cui [non siamo più affiliati](https://webodm.org/blog/announcement/), vende programmi di installazione per un fork di WebODM. Tieni presente che i programmi di installazione WebODM ufficiali possono essere scaricati e utilizzati gratuitamente e che l'acquisto da OpenDroneMap non supporta WebODM.

:::


### Finestra mobile

Per installare WebODM sul tuo computer con docker, installa prima:

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/)

Gli utenti Windows e macOS devono installare Docker Desktop. Poi:

1. Fornisci a Docker abbastanza CPU (default 2) e RAM (>4 Gb, meglio 16 Gb ma lasciane un po' per il sistema operativo) andando su "Impostazioni - Risorse"
2. Seleziona la posizione del disco rigido in cui desideri che risiedano i dischi rigidi virtuali (`Impostazioni -- Risorse -- Avanzate`).

Poi:

* Apri Git Bash (Windows), oppure dalla riga di comando (Mac/Linux/WSL), digita:

```bash
git clone https://github.com/WebODM/WebODM --config core.autocrlf=input -- Depth 1
cd WebODM
./webodm.sh avviare
```

* Se riscontri problemi nell'ultimo passaggio su Linux, assicurati che il tuo utente faccia parte del gruppo docker:

```bash
sudo usermod -aG docker $USER
Uscita
(riavviare la shell disconnettendosi e quindi rientrando)
./webodm.sh avviare
```

🎉 **Congratulazioni!** Dovresti essere attivo e funzionante. Aprire un browser su http://localhost:8000

Per interrompere WebODM premi CTRL+C o esegui:

```
./webodm.sh fermati
```

Per aggiornare WebODM all'ultima versione utilizzare:

```
./webodm.sh aggiornamento
```

:::nota[Archiviazione su disco]

Per impostazione predefinita, i dati vengono archiviati nella finestra mobile denominata volumi. Vedi [Dove sono archiviati i miei file?](/faq/#where-are-my-files-stored)

Per cambiarlo, vedi sotto.

:::



Se hai intenzione di elaborare grandi quantità di dati o stai esaurendo lo spazio su disco, configura `--media-dir` e/o `--node-dir`:

```
./webodm.sh riavvio --media-dir /storage/media --node-dir /storage/node
```

| Argomento | Descrizione |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `--dir-nodo` | Percorso in cui verranno archiviati i file temporanei durante l'elaborazione quando si utilizza il nodo predefinito. Sicuro da cambiare.                                                                 |
| `--media-dir` | Dove tutti i file relativi a un progetto e un'attività vengono archiviati in modo permanente. Cerca di non modificare questa cartella dopo il primo avvio, a meno che non sia parte di una [migrazione](#backup-and-restore). |

## Installazione su altre macchine

### Google Compute, Amazon AWS

Questi passaggi sono per Google Cloud, ma possono essere utilizzati anche per Amazon AWS e altre piattaforme cloud con piccole modifiche:

1. Avvia un'istanza Google Cloud di Ubuntu LTS.
2. Apri il terminale SSH: Google offre SSH tramite il sito web.
3. Esegui "sudo apt-get update".
4. Eseguire "sudo apt-get upgrade".
5. Installa [docker-compose](https://docs.docker.com/compose/install/). Non installare tramite apt dal 24.04 in poi.
6. Eseguire `sudo apt-get install python-pip`
7. Esegui `git clone https://github.com/WebODM/WebODM --config core.autocrlf=input -- Depth 1`
8. cd WebODM (Linux fa distinzione tra maiuscole e minuscole)
9. "sudo ./webodm.sh start".
10. Ora puoi accedere a WebODM tramite l'indirizzo IP pubblico della tua istanza di Google. Ricorda la porta predefinita 8000.
11. Verifica che il firewall della tua istanza consenta connessioni TCP in entrata sulla porta 8000! Se dimentichi questo passaggio non sarai in grado di connetterti a WebODM.
12. Apri http://publicip:8000

Per configurare il firewall su Google Cloud, apri l'istanza, al centro della pagina delle impostazioni dell'istanza trova NIC0. Aprilo, quindi aggiungi la porta TCP 8000 per l'ingresso e l'uscita sul firewall.


### NAS (Qnap)

Se utilizzi [Lightning](https://webodm.net) o un altro nodo processore, i requisiti per WebODM sono sufficientemente bassi da consentirne l'esecuzione su un dispositivo a basso consumo come un NAS. Il test è stato eseguito su un Qnap-TS264 con 32 GB di RAM (processore Celeron N5095)
Per installare WebODM su un Qnap NAS:

1. Abilitare l'accesso ssh al NAS nel pannello di controllo
2. Installa Git. Ciò potrebbe essere facilmente ottenuto utilizzando [qgit qkpg](https://www.myqnap.org/product/qgit/)
3. Seguire le istruzioni "Installazione con Docker" sopra.
4. Una nuova applicazione "webodm" dovrebbe apparire nella stazione container insieme a quattro contenitori individuali per l'app.
5. WebODM dovrebbe essere disponibile sulla porta 8000 del NAS.
6. Imposta un account Lightning online e configuralo all'interno dei "nodi di elaborazione". È anche possibile configurare un computer più potente per eseguire attività di elaborazione anziché Lightning.


## Configurazioni avanzate

### Gestisci i nodi di elaborazione

WebODM può essere collegato a uno o più nodi di elaborazione che parlano l'[API NodeODX](https://github.com/WebODM/NodeODX/blob/master/docs/index.adoc), come [NodeODX](https://github.com/WebODM/NodeODX), [NodeMICMAC](https://github.com/OpenDroneMap/NodeMICMAC/), [ClusterODX](https://github.com/WebODM/ClusterODX) e [Lightning](https://webodm.net). La configurazione predefinita include un nodo di elaborazione "node-odx-1" che viene eseguito sulla stessa macchina di WebODM, solo per aiutarti a iniziare. Man mano che acquisisci maggiore familiarità con WebODM, potresti voler installare nodi di elaborazione su macchine separate.

L'aggiunta di più nodi di elaborazione ti consentirà di eseguire più lavori in parallelo.

Puoi anche configurare un nodo [ClusterODX](https://github.com/WebODM/ClusterODX) per eseguire una singola attività su più macchine con [distributed split-merge](https://docs.opendronemap.org/large/?highlight=distributed#getting-started-with-distributed-split-merge) ed elaborare decine di migliaia di immagini più rapidamente, con meno memoria.

Se non hai bisogno del nodo predefinito "node-odx-1", passa semplicemente il flag `--default-nodes 0` all'avvio di WebODM:

`./webodm.sh riavvio --default-nodes 0`.

Quindi dall'interfaccia web è sufficiente rimuovere manualmente il nodo "node-odx-1".


### Abilita SSL

WebODM ha la capacità di richiedere e installare automaticamente un certificato SSL tramite [Let's Encrypt](https://letsencrypt.org/), oppure puoi specificare manualmente la tua coppia chiave/certificato.

- Imposta il tuo record DNS (webodm.myorg.com --> IP del server).
- Assicurati che le porte 80 e 443 siano aperte.
- Esegui quanto segue:

```bash
./webodm.sh restart --ssl --hostname webodm.myorg.com
```

Questo è tutto! Il certificato si rinnoverà automaticamente quando necessario.

Se vuoi specificare la tua coppia chiave/certificato, passa semplicemente l'opzione `--ssl-key` e `--ssl-cert` a `./webodm.sh`. Per ulteriori informazioni vedere `./webodm.sh --help`.

Nota! Non puoi passare un indirizzo IP al parametro hostname! È necessaria una configurazione del record DNS.

### Abilita l'autenticazione OIDC

WebODM supporta l'autenticazione [OIDC](https://openid.net/) (OpenID Connect), il che significa che puoi fornire un'esperienza Single Sign On (SSO) utilizzando un provider di autenticazione come Google. Per abilitare uno o più provider, crea un file `local_settings.py` con quanto segue:

```python
OIDC_AUTH_PROVIDERS = [
    {

"nome": "Google",
'icona': 'fab fa-google', # icona Font-Awesome valida o lasciare vuoto
'id_client': '<OAUTH2_CLIENT_ID>',
'client_secret': '<OAUTH2_CLIENT_SECRET>',
"auth_endpoint": "https://accounts.google.com/o/oauth2/v2/auth",
"token_endpoint": "https://oauth2.googleapis.com/token",
'userinfo_endpoint': 'https://openidconnect.googleapis.com/v1/userinfo'
    },

# Aggiungi altri fornitori di seguito
]


# Opzionale, imposta restrizioni su chi può accedere
# se non impostato, chiunque abbia un indirizzo email Google può accedere
OIDC_AUTH_EMAILS = ["@myorg.com", "utente@gmail.com"]
```

I valori "client_id" e "client_secret" vengono forniti dal provider di autenticazione. Dovrai registrare un'applicazione. Con Google, puoi farlo da [Google Cloud Console](https://console.cloud.google.com).

Durante la registrazione dell'applicazione, impostare gli **URI di reindirizzamento autorizzati** con:

* `https://webodm.myorg.com/oidc/callback/`

Gli URL degli endpoint sono spesso pubblicati su un URL ".well-known/openid-configuration". Ad esempio, Google pubblica i propri su https://accounts.google.com/.well-known/openid-configuration.

Quindi riavvia WebODM con:

```
./webodm.sh restart --settings /path/to/local_settings.py
```

### Abilita IPv6

L'installazione deve innanzitutto avere un indirizzo IPv6 pubblico.
Per abilitare IPv6 sulla tua installazione, devi attivare IPv6 in Docker aggiungendo quanto segue a un file situato in /etc/docker/daemon.json:

```bash
{

"ipv6": vero,
"fixed-cidr-v6": "fdb4:4d19:7eb5::/64"
}

```
Riavvia la finestra mobile:
"systemctl riavvia la finestra mobile".

Per aggiungere IPv6, esegui semplicemente:

`./webodm.sh riavviare --ipv6`

Nota: quando si utilizza la modalità `--ssl`, non è possibile passare un indirizzo IP al parametro hostname; è necessario impostare un record DNS AAAA. Senza la modalità `--ssl` abilitata, accedi al sito all'indirizzo (ad esempio, http://[2001:0db8:3c4d:0015::1]:8000). Le parentesi attorno all'indirizzo IPv6 sono essenziali!
Puoi aggiungere un nuovo nodo NodeODX in WebODM specificando un indirizzo IPv6. Non dimenticare di includere parentesi attorno all'indirizzo! ad esempio, [2001:0db8:fd8a:ae80::1]

### Abilita MicMac

WebODM può utilizzare [MicMac](https://github.com/OpenDroneMap/micmac) come motore di elaborazione tramite [NodeMICMAC](https://github.com/OpenDroneMap/NodeMICMAC/). Per aggiungere MicMac, esegui semplicemente:

`./webodm.sh riavviare --with-micmac`

Ciò creerà un nodo di elaborazione "node-micmac-1" sulla stessa macchina che esegue WebODM. Tieni presente che NodeMICMAC è in fase di sviluppo attivo ed è attualmente sperimentale. Se riscontri problemi, [segnalali](https://github.com/OpenDroneMap/NodeMICMAC/issues) nel repository NodeMICMAC.

## Risoluzione dei problemi comuni

| Sintomi | Possibili soluzioni |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Memoria esaurita | Assicurati che il tuo ambiente Docker disponga di RAM sufficiente allocata: [Istruzioni MacOS](http://stackoverflow.com/a/39720010), [Istruzioni Windows](https://docs.docker.com/desktop/settings/windows/#advanced) |
| Su Windows, docker-compose fallisce con il messaggio "Impossibile eseguire lo script docker-compose" | Assicurati di aver abilitato la virtualizzazione VT-x nel BIOS |
| Impossibile accedere a WebODM utilizzando Microsoft Edge su Windows 10 | Prova a modificare le tue proprietà Internet seguendo [queste istruzioni](http://www.hanselman.com/blog/FixedMicrosoftEdgeCantSeeOrOpenVirtualBoxhostedLocalWebSites.aspx) |
| Viene visualizzato l'errore "Spazio esaurito sul dispositivo", ma sul disco rigido è rimasto spazio sufficiente | Docker su Windows per impostazione predefinita assegnerà solo 20 GB di spazio alla macchina docker predefinita. È necessario aumentare tale importo. Vedi [questo collegamento](http://support.divio.com/local-development/docker/managing-disk-space-in-your-docker-vm) e [questo collegamento](https://www.howtogeek.com/124622/how-to-enlarge-a-virtual-machines-disk-in-virtualbox-or-vmware/) |
| Impossibile avviare WebODM tramite `./webodm.sh start`, i messaggi di errore sono diversi ad ogni nuovo tentativo | Potresti essere a corto di memoria. Assicurati di avere abbastanza RAM disponibile. 2 GB dovrebbero essere il minimo consigliato, a meno che tu non sappia cosa stai facendo |
| Su Windows, lo spazio di archiviazione mostrato nella pagina di diagnostica WebODM non è lo stesso di quello effettivamente impostato nelle impostazioni di Docker.                                                   | Da Hyper-V Manager, fare clic con il pulsante destro del mouse su "DockerDesktopVM", andare su Modifica disco, quindi scegliere di espandere il disco e abbinare la dimensione massima alle impostazioni specificate nelle impostazioni della finestra mobile. Dopo aver apportato le modifiche, riavviare la finestra mobile.                                                                                                                                                                                                                                                     |
| Su Linux o WSL, avviso: `È stato richiesto l'uso della GPU, ma non è stata trovata alcuna GPU` | Esegui `nvidia-smi` (nativamente) o `docker run --rm --gpus all nvidia/cuda:11.2.2-devel-ubuntu20.04 nvidia-smi` (docker) per verificare con [driver NVIDIA](https://www.nvidia.com/drivers/unix/) e [contenitore NVIDIA Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).                                                                                                                                                          |
| Ricevo un "Errore di connessione: HTTPSConnectionPool(host='spark1.webodm.net', port=443): numero massimo di tentativi superato [Errno 11002] Errore di ricerca scaduta" durante l'invio di immagini a Lightning | Per qualche motivo il sistema DNS sul tuo computer non è configurato correttamente o è filtrato dal software AV/VPN/di rete installato sul computer. Puoi provare a modificare il tuo file "hosts" per mappare manualmente l'indirizzo IP di "spark1.webodm.net". Vedi [come modificare il file host su Windows](https://www.howtogeek.com/784196/how-to-edit-the-hosts-file-on-windows-10-or-11/) e [usa questo indirizzo IP](https://mxtoolbox.com/SuperTool.aspx?action=a%3aspark1.webodm.net&run=toolpage) |


## Attività amministrative comuni

È abbastanza semplice gestire un'installazione di WebODM. Ecco un elenco di operazioni comuni che potresti dover eseguire:

### Reimposta la password dell'amministratore

Se hai dimenticato la password che hai scelto la prima volta che hai effettuato l'accesso a WebODM, per reimpostarla basta digitare:

```bash
./webodm.sh start && ./webodm.sh resetadminpassword newpass
```

La password verrà reimpostata su "newpass". Il comando ti dirà anche quale nome utente hai scelto.

### Backup e ripristino

Se desideri spostare WebODM su un altro sistema, devi solo trasferire i volumi della finestra mobile (a meno che tu non stia archiviando i tuoi file sul file system).

Sul vecchio sistema:

```bash
mkdir -v backup
docker esegui --rm --volume webodm_dbdata:/temp --volume `pwd`/backup:/backup ubuntu tar cvf /backup/dbdata.tar /temp
docker esegui --rm --volume webodm_appmedia:/temp --volume `pwd`/backup:/backup ubuntu tar cvf /backup/appmedia.tar /temp
```

I tuoi file di backup verranno archiviati nella directory "backup" appena creata. Trasferisci la directory `backup` sul nuovo sistema, quindi sul nuovo sistema:

```bash
ls backup # --> appmedia.tar dbdata.tar
./webodm.sh down # Assicurati che WebODM sia inattivo
docker esegui --rm --volume webodm_dbdata:/temp --volume `pwd`/backup:/backup ubuntu bash -c "rm -fr /temp/* && tar xvf /backup/dbdata.tar"
docker esegui --rm --volume webodm_appmedia:/temp --volume `pwd`/backup:/backup ubuntu bash -c "rm -fr /temp/* && tar xvf /backup/appmedia.tar"
./webodm.sh avviare
```

### Aggiornamento

Se usi la finestra mobile, l'aggiornamento è semplice come eseguire:

```bash
./webodm.sh aggiornamento
```

### Personalizzazione ed estensione

Piccole personalizzazioni come la modifica dei colori, del nome, del logo dell'applicazione o l'aggiunta di CSS/HTML/Javascript personalizzati possono essere eseguite direttamente dai pannelli Personalizza - Marchio/Tema all'interno di WebODM. Non è necessario eseguire il fork o modificare il codice.

È possibile ottenere personalizzazioni più avanzate [scrivendo plugin](/plugin-development-guide/). Questo è il modo preferito per aggiungere nuove funzionalità a WebODM poiché richiede meno sforzo rispetto al mantenimento di un fork separato. Il sistema di plug-in presenta segnali lato server che possono essere utilizzati per essere avvisati di vari eventi, un sistema di compilazione ES6/React, un'API dinamica lato client per aggiungere elementi all'interfaccia utente, un archivio dati integrato, un task runner asincrono, hook per aggiungere voci di menu e funzioni per inserire rapidamente visualizzazioni CSS, Javascript e Django.

Per saperne di più, inizia dalla [guida allo sviluppo dei plugin](https://docs.webodm.org/plugin-development-guide/). È anche utile studiare il codice sorgente dei [plugin esistenti](https://github.com/WebODM/WebODM/tree/master/coreplugins).

Se un particolare hook/segnale per il tuo plugin non esiste ancora, [richiedilo](https://github.com/WebODM/WebODM/issues). Aggiungiamo ganci e segnali man mano che procediamo.


## Requisiti hardware

Per eseguire un'installazione autonoma di WebODM (l'interfaccia utente), incluso il componente di elaborazione ([NodeODX](https://github.com/WebODM/NodeODX)), consigliamo come minimo:

* 100 GB di spazio libero su disco
*16 GB di RAM

Non aspettarti di elaborare più di qualche centinaio di immagini con queste specifiche. Per elaborare set di dati più grandi, aggiungi più RAM in modo lineare al numero di immagini che desideri elaborare:

| Numero di immagini | RAM o RAM + Swap (GB) |
| ---------------- | ---------------------- |

| 40| 4|
| 250| 16|
| 500| 32|
| 1500| 64|
| 2500| 128|
| 3500| 192|
| 5000| 256|

:::nota

Queste sono stime prudenti. Molti fattori influenzano l'utilizzo della memoria, come le dimensioni dell'immagine, l'altitudine di volo e le impostazioni di elaborazione. Quindi potresti essere in grado di elaborare più immagini con meno memoria di quanto riportato sopra.

:::


Una CPU con più core accelera l'elaborazione, ma può aumentare l'utilizzo della memoria. L'accelerazione GPU è supportata anche su Linux e WSL. Per utilizzare la tua scheda grafica compatibile con CUDA, assicurati di passare `--gpu` all'avvio di WebODM. In questo caso è necessario che nvidia-docker sia installato, vedere https://github.com/NVIDIA/nvidia-docker e https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker per informazioni sulla configurazione docker/NVIDIA.

WebODM funziona meglio su Linux, ma funziona bene anche su Windows e Mac.

WebODM di per sé è solo un'interfaccia utente e non richiede molte risorse. WebODM può essere caricato su una macchina con solo 1 o 2 GB di RAM e funziona perfettamente senza [NodeODX](https://github.com/WebODM/NodeODX). Puoi utilizzare un servizio di elaborazione come [webodm.net](https://webodm.net) o eseguire NodeODX su un computer separato e più potente.