---

titolo: Multispettrale e Termico
modello: doc
---


## Supporto multispettrale

WebODM supporta la normalizzazione radiometrica, che è in grado di generare ortofoto di riflettanza da telecamere multispettrali. Le telecamere multispettrali catturano più scatti della scena utilizzando sensori di banda diversi.

### Sensori supportati

Anche se miriamo a supportare il maggior numero possibile di fotocamere, il supporto multispettrale è stato sviluppato utilizzando le seguenti fotocamere, quindi funzioneranno meglio:

- [MicaSense RedEdge-MX e Altum](https://www.micasense.com/)
- [Sentera 6X](https://sentera.com/products/fieldcapture/sensors/6x/)
- [DJI Phantom 4 Multispectral](https://www.dji.com/p4-multispectral)
- [DJI Mavic 3 Multispettrale](https://ag.dji.com/mavic-3-m)

Potrebbero funzionare anche altre fotocamere. Puoi aiutarci ad espandere questo elenco [condividendo](https://webodm.org/community) set di dati acquisiti con altre fotocamere.

### Creazione di ortofoto da dati multispettrali

Per i sensori supportati elencati sopra (e probabilmente altri sensori), gli utenti possono elaborare i dati multispettrali allo stesso modo delle immagini a luce visibile. Le immagini provenienti da tutte le bande del sensore devono essere elaborate contemporaneamente (non separare le bande in più cartelle). Gli utenti hanno la possibilità di passare il parametro "--radiometric-calibration" con le opzioni "camera" o "camera+sun" per abilitare la normalizzazione radiometrica. Se le immagini fanno parte di una configurazione multi-camera, l'ortofoto risultante avrà N bande, una per ciascuna fotocamera (+ alfa).

L'NDVI e altri indici di vegetazione possono essere calcolati da queste ortofoto cucite utilizzando software come [QGIS](https://www.qgis.org/).


## Supporto termico

WebODM supporta la calibrazione radiometrica dei dati termici, che è in grado di generare ortofoto di temperatura da telecamere a infrarossi a onda lunga (LWIR). Le immagini LWIR possono essere elaborate da sole o come parte di un set di dati multispettrali.

![Immagini termiche in WebODM](/images/thermal.webp)

### Ferramenta

Anche se miriamo a supportare il maggior numero possibile di fotocamere, il supporto termico è stato sviluppato utilizzando le seguenti fotocamere, quindi funzioneranno meglio:

- [MicaSense Altum](https://www.micasense.com/)
- [DJI Zenmuse XT](https://www.dji.com/zenmuse-xt)
- [Serie DJI Zenmuse H20](https://enterprise.dji.com/zenmuse-h20-series)

Anche questi droni sono supportati, ma richiedono la pre-elaborazione con
[Strumenti termici](https://webodm.net/thermaltools):

*DJI Zenmuse H20N
* Serie DJI Matrice 30
*DJI Zenmuse XT S
* Serie DJI Zenmuse H30
*DJI Mavic 2 Enterprise Avanzato
*DJI Mavic 3 Enterprise
* Serie DJI Matrice 4

Potrebbero funzionare anche altre fotocamere. Puoi aiutarci ad espandere questo elenco [condividendo](https://webodm.org/datasets) set di dati acquisiti con altre fotocamere.

### Utilizzo

:::nota[Solo per droni DJI]

Per ottenere i valori di temperatura, preelaborare le immagini con [Thermal Tools](https://webodm.net/thermaltools) prima di elaborarle con WebODM e utilizzare le impostazioni standard (non utilizzare `--radiometric-calibration`).

:::


Elaborare le immagini utilizzando il parametro "--radiometric-calibration camera" per abilitare la calibrazione radiometrica.
