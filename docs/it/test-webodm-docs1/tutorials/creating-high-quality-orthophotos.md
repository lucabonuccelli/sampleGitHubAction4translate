---

titolo: Creazione di ortofoto di alta qualità
---


![Ortofoto](/images/ortofoto.webp)

Senza alcuna modifica dei parametri, WebODM sceglie un buon compromesso tra qualità, velocità e utilizzo della memoria. Se desideri ottenere risultati di qualità superiore, devi modificare alcuni parametri:

- `--ortofoto-risoluzione` è la risoluzione dell'ortofoto in cm/pixel. Diminuire questo valore per ottenere un risultato con una risoluzione più elevata.

- "--mesh-size" dovrebbe essere aumentato a "300000-600000" e "--mesh-octree- Depth" dovrebbe essere aumentato a "10-11" nelle aree urbane per ricreare edifici/tetti migliori.
