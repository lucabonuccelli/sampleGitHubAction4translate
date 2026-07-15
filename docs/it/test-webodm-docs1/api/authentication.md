---

titolo: Autenticazione
modello: doc
---


### Nozioni di base sull'autenticazione

> Ottieni token di autenticazione:

```bash
curl -X POST -d "nomeutente=utentetest&password=testpass" http://localhost:8000/api/token-auth/

{"token":"eyJ0eXAiO..."}
```

> Utilizza token di autenticazione:

```bash
curl -H "Autorizzazione: JWT <your_token>" http://localhost:8000/api/projects/

{"contare":13, ...}
```

> Utilizza token di autenticazione tramite querystring (meno sicuro):

```bash
curl http://localhost:8000/api/projects/?jwt=<tuo_token>

{"contare":13, ...}
```


`POST /api/token-auth/`

Campo | Digitare | Descrizione
----- | ---- | -----------

nome utente | stringa | Nome utente
password | stringa | Password

Per accedere all'API, è necessario fornire un nome utente e una password validi. Puoi creare utenti dalla pagina di amministrazione di WebODM.

Se l'autenticazione ha esito positivo, ti verrà rilasciato un token. Tutte le chiamate API dovrebbero includere la seguente intestazione:

Intestazione |
------ |

Autorizzazione: JWT `your_token` |

Il token scade dopo un determinato periodo di tempo. Per ulteriori informazioni, vedere [Scadenza token](#scadenza token).

Poiché le applicazioni a volte non consentono la modifica delle intestazioni, puoi anche autenticarti aggiungendo il parametro querystring `jwt` a un URL protetto. Questo è meno sicuro, quindi passa il token tramite l'intestazione, se possibile.


### Scadenza del token

Per impostazione predefinita, il token scade dopo sei ore. Il tempo di scadenza è definito nel modulo delle impostazioni di Django in WebODM. Se si crea WebODM dai sorgenti o lo si esegue in modo nativo, il tempo di scadenza può essere modificato nella variabile `JWT_AUTH['JWT_EXPIRATION_DELTA']`. Altrimenti, ad es. utilizzando le immagini docker, dovrai richiedere un altro token alla scadenza del token.

Sai che un token è scaduto se una qualsiasi chiamata API restituisce un codice di stato "403" con il corpo JSON "{'detail": "La firma è scaduta.'}".
