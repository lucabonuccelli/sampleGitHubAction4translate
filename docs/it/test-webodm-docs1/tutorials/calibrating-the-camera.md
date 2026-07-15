---

titolo: Calibrazione della fotocamera
---


La calibrazione della fotocamera è una sfida speciale con le fotocamere commerciali. Cambiamenti di temperatura, vibrazioni, messa a fuoco e altri fattori possono influenzare i parametri derivati ​​con effetti sostanziali sui dati risultanti. La calibrazione automatica o automatica è possibile e auspicabile con i voli dei droni, ma a seconda del modello di volo, la calibrazione automatica potrebbe non rimuovere tutte le distorsioni dai prodotti risultanti. James e Robson (2014) nel loro articolo [Mitigating systemic error in topoographic models derive from UAV and ground‐based image network](https://onlinelibrary.wiley.com/doi/full/10.1002/esp.3609) affrontano come ridurre al minimo la distorsione derivante dall'autocalibrazione.

![Effetto bowling sulla nuvola di punti](/images/msimbasi_bowling.webp)

*Effetto bowling sulla nuvola di punti di oltre 13.000 set di dati di immagini raccolti dalla Banca Mondiale in Tanzania sul bacino di Msimbasi, soggetto a inondazioni, Dar es Salaam, Tanzania.*

Per mitigare questo effetto, ci sono alcune opzioni, ma le più semplici sono le seguenti: volare due schemi separati di 20° e invece di avere una telecamera nadir (puntata verso il basso), utilizzarne una inclinata in avanti di 5°.

![Pianificazione ottimale del volo](/images/flightplanning.webp)

Poiché questo approccio richiede più tempo rispetto all’imaging tradizionale, i piloti e i team possono applicare questa tecnica a un’area più piccola e utilizzare i dati raccolti per ottimizzare i voli futuri. WebODM può generare un file di calibrazione chiamato cameras.json da un piccolo volo di esempio. Il file di calibrazione può essere utilizzato per voli futuri, mitigando l'effetto bowling senza sacrificare l'efficienza.

In alternativa, è possibile applicare il seguente metodo sperimentale: volo con una sovrapposizione molto inferiore, ma due voli *crossgrid* (a volte chiamati crosshatch) separati di 20° con una telecamera rivolta in avanti di 5°.

- Le percentuali di sovrapposizione della griglia trasversale possono essere inferiori rispetto ai voli paralleli. Per ottenere buoni risultati 3D, sarà necessaria una sovrapposizione e una sovrapposizione laterale del 68% per una sovrapposizione e una sovrapposizione laterale equivalente all'83%.
- Per ottenere buoni risultati 2D e 2,5D (modello digitale di elevazione), saranno necessari il 42% di sovrapposizione e sidelap per una sovrapposizione e sidelap equivalente al 70%.

![Metodo di rotazione sperimentale](/images/rotation.webp)

Anche le linee di volo separate verticalmente migliorano la precisione, ma meno di una fotocamera rivolta in avanti di 5°.

![Effetto delle linee di volo separate verticalmente](/images/forward_facing.webp)

*Da James e Robson (2014), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)*
