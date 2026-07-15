---

titolo: Gestione degli errori
modello: doc
---


Tutte le chiamate API utilizzano i codici di stato descritti nella [Guida ai codici di stato di Django REST Framework](http://www.django-rest-framework.org/api-guide/status-codes/), ma in genere è sufficiente verificare solo i codici di stato di successo (`200` o `204`), gestire il caso speciale di [Scadenza token](/api/authentication/#token-expiration) (`403`) e segnalare un errore altrimenti.

### Codici di stato di errore

Questo non è un elenco esaustivo, ma i codici di errore comuni sono elencati di seguito.

Codice di stato | Descrizione
----------- | -----------

401| Non autenticato
403| Proibito (token scaduto?)
400| Richiesta non valida
404| Non trovato

Per ragioni di sicurezza, a volte un'operazione che dovrebbe restituire "403" restituisce "404" per evitare di rivelare ID e altre informazioni agli aggressori.
