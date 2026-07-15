---

titolo: Avvio rapido
modello: doc
---


## Come elaborare le immagini

In questo tutorial esploreremo come elaborare un'ortofoto da un set di immagini aeree utilizzando Python. Per fare ciò dovremo:

- Autenticarsi
- Crea un [progetto](/api/reference/operazioni/projects_create/). I progetti rappresentano un modo per raggruppare elementi [Attività](/api/task/) correlati
- Carica alcune immagini per creare un [Attività](/api/task/)
- Controlla l'avanzamento dell'[Attività](/api/task/). La fotogrammetria può richiedere molto tempo, quindi l'elaborazione dei risultati potrebbe richiedere da alcuni minuti ad alcune ore.
- Scarica l'ortofoto risultante.

<aside class="notice">La maggior parte degli esempi in questo documento utilizzano <a href="http://docs.python-requests.org/en/latest/index.html" target="_blank">richieste</a>. Assicurati che sia installato prima di eseguire qualsiasi codice:<br/><br/>

<pre class="evidenzia shell">
Richieste di installazione $ pip
</pre>
</a parte>

<aside class="avviso">
Il <a href="https://github.com/WebODM/Docs/blob/main/examples/process_images.py" target="_blank">codice sorgente</a> per questo esempio è disponibile su GitHub</a>.
</a parte>

```python
richieste di importazione
res = request.post('http://localhost:8000/api/token-auth/',
dati={'nome utente': 'amministratore',
'password': 'admin'}).json()
gettone = res['gettone']
```

Innanzitutto, <a href="/api/authentication/">autentichiamo</a> con WebODM. Un "token" viene restituito quando l'autenticazione ha esito positivo.
<div class="clear"></div>

```python
res = request.post('http://localhost:8000/api/projects/',
headers={'Autorizzazione': 'JWT {}'.format(token)},
data={'nome': 'Ciao WebODM!'}).json()
id_progetto = res['id']
```

Quindi dobbiamo creare un [Progetto](/api/reference/operazioni/projects_create/). Passiamo il nostro "token" tramite l'intestazione "Authorization". Se dimentichiamo di passare questa intestazione, il sistema non ci autenticherà e rifiuterà di elaborare la richiesta. Assegniamo anche un `nome` al nostro progetto.
<div class="clear"></div>

```python
immagini = [
('immagini', ('immagine1.jpg', open('immagine1.jpg', 'rb'), 'immagine/jpg')),
('immagini', ('immagine2.jpg', open('immagine2.jpg', 'rb'), 'immagine/jpg')),
#...
]

opzioni = json.dumps([
{'nome': "risoluzione ortofoto", 'valore': 24}
])


res = request.post('http://localhost:8000/api/projects/{}/tasks/'.format(project_id),
headers={'Autorizzazione': 'JWT {}'.format(token)},
file=immagini,
dati={
'opzioni': opzioni
}).json()

task_id = res['id']
```

Possiamo quindi creare un [Task](/api/task/). L'unico parametro richiesto è un elenco di "immagini" multiple codificate in più parti. L'elaborazione inizierà automaticamente
non appena un [Nodo di elaborazione](/api/reference/operazioni/processingnodes_list/) è disponibile. È possibile specificare opzioni aggiuntive passando un valore "opzioni", che è un elenco di coppie nome/valore con codifica JSON. Sono disponibili molte altre opzioni. Consulta il riferimento [Opzioni e flag](/options-flags/) per ulteriori informazioni.
<div class="clear"></div>

```python
mentre Vero:
res = request.get('http://localhost:8000/api/projects/{}/tasks/{}/'.format(project_id, task_id),
headers={'Autorizzazione': 'JWT {}'.format(token)}).json()

if res['status'] == status_codes.COMPLETED:
print("L'operazione è stata completata!")
rottura
elif res['status'] == status_codes.FAILED:
print("Operazione fallita: {}".format(res))
sys.uscita(1)
altro:
print("Elaborazione in corso, aspetta...")
tempo.sonno(3)
```

Controlliamo periodicamente lo stato [Attività](/api/task/) utilizzando un ciclo.
<div class="clear"></div>

```python
res = request.get("http://localhost:8000/api/projects/{}/tasks/{}/download/orthophoto.tif".format(project_id, task_id),
headers={'Autorizzazione': 'JWT {}'.format(token)},
flusso=Vero)
con open("orthophoto.tif", 'wb') come f:
per pezzo in res.iter_content(chunk_size=1024):
se pezzo:
f.write(pezzo)
print("Salvato ./orthophoto.tif")
```

La nostra ortofoto è pronta per essere scaricata. Sono disponibili anche una varietà di altre risorse, tra cui una densa nuvola di punti 3D e un modello strutturato (/api/task/#download-assets).

Congratulazioni! Hai appena elaborato alcune immagini.

![Successo](https://i.imgflip.com/2/ipzhf.jpg)
