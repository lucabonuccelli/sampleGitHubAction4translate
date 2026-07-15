---

titolo: Autorizzazioni
modello: doc
---


WebODM viene fornito con un sistema di autorizzazione standard a "livello di modello". Puoi
controlla se gli utenti hanno effettuato l'accesso e dispongono dei privilegi per agire sulle cose
dal punto di vista del modello (un utente può aggiungere un progetto? un utente può visualizzare i progetti?).

Oltre a ciò, WebODM presenta un potente sistema di permessi a "livello di riga". Puoi specificare esattamente a quali cose un utente ha o non ha accesso, eliminare, modificare, ecc.

Le modifiche alle autorizzazioni degli oggetti possono essere gestite tramite la pagina "Amministrazione" di WebODM.

Stiamo pianificando di rendere più semplice per gli utenti e gli sviluppatori la gestione delle autorizzazioni tramite un'API. Questo è un lavoro in corso.


### Valori dei permessi

Autorizzazione | Descrizione
----- | -----------

elimina | L'oggetto può essere eliminato
cambiare | L'oggetto può essere modificato
aggiungi | È possibile aggiungere un oggetto correlato all'oggetto (è possibile aggiungere un'attività al progetto)
vista | L'oggetto può essere visualizzato (sola lettura)