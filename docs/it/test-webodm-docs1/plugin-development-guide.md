---

titolo: Guida allo sviluppo dei plugin
modello: doc
---


WebODM ti consente di scrivere plugin, che puoi distribuire come file .zip o condividerli con il mondo aggiungendoli alla cartella "coreplugins" di WebODM (e aprendo una richiesta pull). Questa è un'opzione flessibile per coloro che non vogliono mantenere un fork separato, ma desiderano comunque aggiungere nuove funzionalità a WebODM.

Puoi attivare/disattivare i plugin dalla Dashboard tramite il menu **Amministrazione** --> **Plugins**.

I plugin ti consentono di definire sia la logica lato server (Python) che quella lato client (Javascript). Eseguono in un ambiente condiviso. Esistono hook/gestori di eventi/segnali a cui puoi iscriverti per ricevere notifiche, ad esempio quando un'attività viene creata/eliminata o quando la visualizzazione della mappa sta per essere renderizzata. Il numero di questi è limitato, ma tieni presente che è possibile aggiungerne altri.

Vengono forniti alcuni aiutanti di base, ad esempio per l'esecuzione di lunghe attività asincrone, per l'archiviazione di base dei dati chiave-valore, per l'installazione di dipendenze Python isolate (tramite pip) e dipendenze Javascript (tramite npm). Un sistema di compilazione lato client (tramite webpack) ti consente inoltre di utilizzare React/SCSS nel codice del plug-in e accedere a tutti i componenti lato client di WebODM (JSX).

Puoi rendere disponibili le risorse (immagini, stili, modelli, ...) semplicemente inserendole in una cartella "pubblica".

Il sistema dei plugin non tenta di imporre standard rigorosi. Ciò che costruisci dipende da te e tutto è possibile.

## Avvio rapido

* Assicurati di aver avviato WebODM in modalità sviluppo (tramite `--dev`). Vedi [contributing](/contributing/#setup-a-development-environment) per istruzioni.
* Vai su **Amministrazione** --> **Plugin** e attiva il plugin **Hello World**.
* Nota che nel menu a sinistra è apparso il menu "Hello World".
* Crea una copia della cartella `coreplugins/hello-world`. Chiamatelo "coreplugins/mio-plugin".
* Modifica `coreplugins/my-plugin/manifest.json`:

```json
 {

"nome": "Il mio plugin",
"webodmMinVersion": "2.9.4",
"description": "Il mio primo plugin",
"versione": "1.0.0",
"autore": "Il tuo nome",
"email": "tua@email.qui",
"repository": "https://github.com/WebODM/WebODM",
"tags": ["descrittivo", "tags"],
"homepage": "https://github.com/WebODM/WebODM",
"sperimentale": falso,
"deprecato": falso
}

```

* Modifica `coreplugins/my-plugin/plugin.py`:

```python
da app.plugins importa PluginBase, Menu, MountPoint
dal rendering di importazione di django.shortcuts
da django.contrib.auth.decorators importa login_required
da django.utils.translation importa gettext come _

plugin di classe(PluginBase):
def menu_principale(self):
return [Menu(_("Il mio plugin"), self.public_url(""), "fa fa-cog fa-fw")]

def punti_montaggio_app(self):
@login_required
def ciao_vista(richiesta):
return render(request, self.template_path("ciao.html"), {'messaggio': "Ciao!"})

ritorno [
Punto di montaggio('$', ciao_view),
# altri punti di montaggio qui...
        ]


def include_js_files(self):
ritorno ['main.js']

def build_jsx_components(self):
ritorno ['app.jsx']

# vedi anche plugin_base.py per altri metodi
```

* Salva le modifiche e apri `app/boot.py`, aggiungi una riga vuota, salva `boot.py`, quindi rimuovi la riga vuota, quindi salva nuovamente `boot.py`. Questo è un trucco per forzare il ricaricamento di WebODM senza riavviare il processo docker. Devi farlo solo una volta.
* Il tuo plugin ora dovrebbe essere visibile in **Amministrazione** --> **Plugin**.
* Attivalo per vedere se funziona.

Congratulazioni! 🎉 Ora sei uno sviluppatore di plugin.

Il tuo plugin dovrebbe avere questa struttura di file di base:

```
├── disabilitato
├── __init__.py
├── manifest.json
├── plugin.py
├── pubblico
│   ├── app.jsx
│   ├── app.scss
│   ├── main.js
│   └── webpack.config.js
└── modelli
└── ciao.html
```

Un file `disabled` vuoto nella root indica che il plugin non dovrebbe essere abilitato per impostazione predefinita.

## Modelli Django

Puoi eseguire il rendering dei [modelli Django](https://docs.djangoproject.com/en/2.2/topics/templates/) inserendo i file modello nella cartella "templates". Quindi esegui il rendering dei modelli creando *punti di montaggio* (proprio come [URL Django](https://docs.djangoproject.com/en/2.2/topics/http/urls/)).

## File Javascript

È possibile eseguire codice JavaScript arbitrario. Quando il tuo plugin è abilitato, qualsiasi file restituito da `include_js_files` verrà incluso in ogni pagina WebODM (nell'intestazione). Puoi usarlo come punto di ingresso per caricare codice Javascript più complesso (ad esempio una build React) o per registrare un hook.

## File CSS

Come per Javascript, puoi includere file CSS arbitrari tramite:


```python
def include_css_files(self):
ritorno ['style.css']
```

## Componenti di reazione

Se prevedi di utilizzare React (facoltativo) e desideri utilizzare il sistema integrato per creare il componente (anch'esso facoltativo), dovrai dichiarare quali file `.jsx` vuoi creare tramite:

```python
def build_jsx_components(self):
ritorno ['app.jsx']
```

I file compilati verranno inseriti in `coreplugins/my-plugin/public/build/*` e saranno accessibili tramite `http://localhost:8000/plugins/my-plugin/build/*`.

Se utilizzi componenti JSX, ti consigliamo di riavviare il tuo ambiente di sviluppo con:

```bash
./webodm.sh riavvio --dev --dev-watch-plugins
```

Altrimenti dovrai eseguire manualmente `webpack --watch` dalla cartella `coreplugins/my-plugin/public` (all'interno del contenitore WebODM).

Dal lato client, puoi importare i tuoi componenti React, così come qualsiasi altro modulo Javascript, utilizzando vari hook. Uno di questi hook è `PluginsAPI.App.Ready`, che viene attivato al caricamento della pagina:

```javascript
PluginAPI.App.ready([
'/plugins/mio-plugin/build/app.js',
'/plugins/mio-plugin/build/app.css'
], funzione(argomenti, App){

ReactDOM.render(React.createElement(App, {saluto: "Ciao"}), $("#ciao-component").get(0));
});

```

## Ganci lato cliente

Puoi essere informato di vari eventi lato client tramite hook. Alcuni di questi hook ti consentono di restituire un elemento DOM, che può essere utile per aggiungere pulsanti o altri componenti in momenti diversi del processo di rendering dell'interfaccia utente:

```javascript
PluginAPI.hook([
// elenco facoltativo delle dipendenze da caricare
], funzione(argomenti, dipendenze facoltative]){
// Il tuo codice qui

// args contiene parametri specifici per ciascun hook.

console.log(argomenti);

var domEl = /* ... */;
restituire domEl;
});


```

| <div style="width:260px">Gancio</div> | Innescato |
| ----------------------------------- | ----------------------------------------------------------------------------------------------- |
| `App.pronta` | Al caricamento del DOM |
| `Dashboard.addTaskActionButton` | Quando i pulsanti sono stati aggiunti a un'attività (accanto a Visualizza mappa, Visualizza modello 3D, ..) |
| `Dashboard.addNewTaskPanelItem` | Quando si apre il pannello dopo aver selezionato immagini e GCP |
| `Dashboard.addNewTaskButton` | Quando i pulsanti sono stati aggiunti al pannello di un progetto (accanto a Seleziona immagini e GCP, Importa) |
| `Map.willAddControls` | Quando stanno per essere aggiunti i controlli del volantino |
| `Map.didAddControls` | Quando sono stati aggiunti i controlli del volantino |
| `Map.addActionButton` | Quando stanno per essere aggiunti i pulsanti di azione (in basso a destra dello schermo) |
| `ModelView.addActionButton` | Quando i pulsanti di azione (in basso a destra dello schermo) stanno per essere aggiunti (nel modello 3D) |
| `SharePopup.addLinkControl` | Durante il rendering della finestra di dialogo Condividi nella vista mappa |

## Richiamate lato client

Similmente agli hook, i callback possono avvisarti degli eventi che accadono intorno all'applicazione, ma a differenza degli hook, non consentono il caricamento delle dipendenze. È possibile registrare e annullare la registrazione delle richiamate:

```javascript
var miaFunzione = funzione(){
restituire un valore;
};


PluginsAPI.[ns].onCallback(miaFunzione); // per registrarsi
PluginsAPI.[ns].offCallback(miaFunzione); // per annullare la registrazione
```

Per esempio:

```javascript
PluginsAPI.Map.onHandleClick(funzione(){
console.log("Mappa cliccata!");
});

```

| Spazio dei nomi | <div style="width:260px">Richiamata</div> | Attivato quando |
| --------- | --------------------------------------- | ----------------------------------------------------------------------------- |

| `Mappa` | `handleClick` | Si fa clic sulla mappa del volantino |
| `Mappa` | `aggiungiannotazione` | L'annotazione sta per essere aggiunta |
| `Mappa` | "aggiornamentoAnnotazione" | L'annotazione sta per essere modificata |
| `Mappa` | `cancellaAnnotazione` | L'annotazione sta per essere eliminata |
| `Mappa` | `toggleAnnotazione` | L'annotazione sta per essere attivata/disattivata |
| `Mappa` | `annotazioneEliminata` | L'annotazione è stata eliminata |
| `Mappa` | `scaricaAnnotazioni` | Viene avviata una richiesta per scaricare le annotazioni |
| `Mappa` | `mapTypeChanged` | Il tipo di mappa (da Ortofoto a Modello di superficie, a Salute delle piante, ecc.) è cambiata |
| `Mappa` | `sideBySideChanged` | L'utente ha sovrapposto due livelli affiancati |

## Segnali lato server

Puoi registrarti a vari [segnali Django](https://docs.djangoproject.com/en/2.2/topics/signals/) per ricevere notifiche sugli eventi che accadono attorno all'applicazione.

```python
dal ricevitore di importazione django.dispatch
da app.plugins.signals import task_completed
da app.plugins.functions importa get_current_plugin

@destinatario(attività_completata)
def on_complete(mittente, task_id, **kwargs):
# Non eseguirlo se il plugin non è attivo
se get_current_plugin(only_active=True) è Nessuno:
ritorno

print("L'attività %s è stata completata" % task_id)
```

| <div style="width:260px">Segnale</div> | Attivato quando |
| ------------------------------------- | ---------------------------------- |

| `attività_completata` | Un'attività è stata completata con successo |
| `rimozione_attività` | Un'attività sta per essere eliminata |
| `attività_rimossa` | Un'attività è stata eliminata |
| `attività_non riuscita` | Un'attività non è riuscita |
| `task_resizing_images` | Un compito è ridimensionare le immagini |
| `attività_duplicata` | Un'attività è stata duplicata |
| `nodo_di_elaborazione_rimosso` | Un nodo di elaborazione è stato eliminato |

## Dipendenze NPM

Puoi utilizzare dipendenze esterne definendo un `package.json` nella cartella `public` del tuo plugin e fare riferimento a tali dipendenze nei tuoi componenti JSX (o caricarli nel browser). Questo può essere creato tramite `npm init`. Le dipendenze vengono scaricate e installate automaticamente durante la fase di compilazione.

## Dipendenze PIP

Sul lato server, puoi installare pacchetti Python aggiuntivi definendo un file `requirements.txt` nella cartella principale del tuo plugin (ad esempio `coreplugins/my-plugin/requirements.txt`).

Quando il plugin è abilitato, il sistema controllerà prima se è necessario scaricare qualche dipendenza e, se necessario, eseguirà "pip install".

Per evitare collisioni tra versioni e spazi dei nomi con WebODM, così come con altri plugin, per utilizzare una dipendenza del plugin è necessario racchiudere l'importazione in un contesto `python_imports`:

```python
da app.plugins.functions importa get_current_plugin

con get_current_plugin().python_imports():
importa Numpy come np
#...
```

## Attività a lunga esecuzione

Il sistema di plug-in offre funzioni per eseguire attività lato server di lunga durata, nonché funzioni lato client per tenere traccia dello stato di tali attività. Le attività a lunga esecuzione vengono eseguite dai processi di lavoro anziché dall'applicazione del server Web.

Sul server:

```python
da app.plugins.worker importa run_function_async
dallo stato di importazione di rest_framework
da rest_framework.response import Risposta

# Dal punto di montaggio "greet".

def long_greet(saluto, progress_callback=None):
import time # DEVI posizionare le importazioni all'interno della funzione async e non all'inizio del file
tempo.sonno(30)
progress_callback("Quasi finito!", 50) # opzionale (stato del testo, [0-100]%)
tempo.sonno(10)
return {'output': saluto + " ecco!"} # qualsiasi output serializzabile JSON

# - oppure - puoi anche restituire file restituendo a
# miofile = 'percorso/del/file.txt'
# return {'file': miofile}

# - oppure - un errore
# return {'errore': 'oh no'}

Tentativo:
celery_task_id = run_function_async(long_greet, saluto="Ciao").task_id
restituisce risposta({'celery_task_id': celery_task_id}, status=status.HTTP_200_OK)
tranne Eccezione come e:
restituisce Risposta({'errore': str(e)}, status=status.HTTP_200_OK)
```

Sul cliente:

```javascript
importare lavoratori da 'webodm/classes/Workers';

$.ajax({
tipo: 'OTTIENI',
url: `/api/plugins/mio-plugin/saluto/`,
contentType: "applicazione/json"
}).done(res => {
Workers.waitForCompletion(res.celery_task_id, errore => {
se (errore){
console.error("oh no!");
}altro{
Workers.getOutput(result.celery_task_id, (errore, saluto) => {
console.log(saluto);
            });

// - o - vengono scaricati anche file
// Workers.downloadFile(res.celery_task_id, res.filename);
        }

}, (stato, avanzamento) => {
console.log(stato, avanzamento)
    });

});

```

:::Attenzione
**Devi** dichiarare tutte le istruzioni import all'interno delle funzioni asincrone (e non all'inizio del file). Puoi anche passare solo argomenti serializzabili JSON alle funzioni asincrone. Ad esempio, non puoi passare oggetti Python complessi.
:::


## Archivio dati integrato

La memorizzazione dei dati è un requisito frequente per tutti i tipi di applicazioni, quindi il sistema di plug-in offre un semplice archivio di valori-chiave per la memorizzazione di stringhe, numeri interi, float, booleani e JSON che possono essere globali (condivisi tra tutti gli utenti) o basati sull'utente (specifici per un utente).

```python
da app.plugins importa GlobalDataStore, UserDataStore

# da un punto di montaggio

ds = GlobalDataStore('il mio-plug-in')
uds = UserDataStore('mio-plugin', request.utente)

ds.set_string("chiave1", "stringa")
ds.set_int("chiave2", 42)
ds.set_float("chiave3", 3.14)
ds.set_bool("chiave4", Vero)
ds.set_json("key5", {'piero_is': ['cool', 'silly', 'entrambi']})

ds.get_string("chiave1")
ds.get_int("chiave2")

#...
```

I dati salvati in questo modo vengono archiviati **non crittografati** nella tabella *PluginDatum*. Puoi visualizzare/modificare questi dati visitando **Amministrazione** --> **Applicazione** --> **Plugin Datum**.

## Pubblicazione del tuo plugin

Il modo più semplice per condividere il tuo lavoro è aprire una richiesta pull nel repository WebODM. Ad un certo punto in futuro potremmo creare una sorta di repository di plugin in cui le persone possano sfogliare e scaricare plugin, ma non siamo ancora a quel punto.

Puoi anche creare un file zip dell'intera cartella del plugin (ad esempio `my-plugin`) con la cartella come voce di primo livello nell'archivio zip e distribuire manualmente il file zip. Gli utenti possono quindi installare il plug-in premendo il pulsante **Carica plug-in (.zip)** quando visitano **Amministrazione** --> **Plugin**.

## Suggerimenti finali

* Impara da altri plugin! Questa documentazione fornisce le nozioni di base, ma aiuta davvero a studiare come funzionano gli altri plugin osservando il loro codice sorgente.
* Se hai bisogno di un nuovo hook, callback o segnale, apri una richiesta pull e aggiungiamolo al sistema.
* Con il tempo, questa documentazione potrebbe non essere aggiornata. Se qualcosa non sembra corrispondere a ciò che vedi in questa pagina o non sembra funzionare, controlla il codice! Il sistema di plugin non è complicato e può essere letto dall'inizio alla fine in meno di poche ore. Leggi `app/plugins` e `app/static/app/js/classes/plugins`.
* Divertiti :)
