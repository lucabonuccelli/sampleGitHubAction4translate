---

titolo: Creazione di modelli digitali di elevazione
---


Per impostazione predefinita, WebODM non crea modelli di elevazione digitale (DEM). Per creare un modello digitale del terreno, assicurati di passare il flag `--dtm`. Per creare un modello di superficie digitale, assicurati di passare il flag `--dsm`.

![Modello di superficie digitale](/images/digitalsurfacemodel.webp)

Per la generazione del DTM, viene utilizzato un filtro morfologico semplice (smrf) per classificare i punti a terra e non a terra e vengono utilizzati solo i punti a terra. Il filtro `smrf` può essere controllato tramite diversi parametri:

- Valore di ridimensionamento `--smrf-scalar`. Aumentare questo parametro per terreni con molte variazioni di altezza.
- Parametro di pendenza `--smrf-slope`, che è una misura della "tolleranza della pendenza". Aumentare questo parametro per terreni con molte variazioni di altezza. Dovrebbe essere impostato su un valore superiore a 0,1 e non superiore a 1,2.
- Soglia di elevazione `--smrf-threshold`. Imposta questo parametro sull'altezza minima (in metri) che prevedi che siano gli oggetti non a terra.
- Parametro del raggio della finestra `--smrf-window` (in metri) che corrisponde alla dimensione dell'elemento più grande (edificio, alberi, ecc.) da rimuovere. Dovrebbe essere impostato su un valore superiore a 10.

La modifica di queste opzioni può influire in modo significativo sul risultato dei DTM. La migliore fonte da leggere per capire come i parametri influenzano l'output è leggere il documento originale [Un filtro morfologico semplice migliorato per la classificazione del terreno dei dati LIDAR aerotrasportati](https://www.researchgate.net/publication/258333806_An_Improved_Simple_Morphological_Filter_for_the_Terrain_Classification_of_Airborne_LIDAR_Data).

Nel complesso l'opzione `--smrf-threshold` ha il maggiore impatto sui risultati.

SMRF è efficace nell'evitare errori di Tipo I (un piccolo numero di punti a terra erroneamente classificati come non a terra) ma è solo "accettabile" nell'evitare errori di Tipo II (un gran numero di punti non a terra erroneamente classificati come a terra). Questo deve essere preso in considerazione quando si generano DTM destinati ad essere utilizzati visivamente, poiché gli oggetti scambiati per terreno sembrano artefatti nel DTM finale.

![Filtro SMRF](/images/smrf.webp)

Altri due importanti parametri influenzano la generazione del DEM:

- `--dem-length` che imposta la risoluzione di output del raster DEM (cm/pixel)
- `--dem-gapfill-steps` che determina il numero di livelli DEM progressivi da utilizzare. Per le scene urbane, aumentare questo valore a "4-5" può aiutare a produrre migliori risultati di interpolazione nelle aree lasciate vuote dal filtro SMRF.

Esempio di come generare un DTM:

```bash
docker run -ti --rm -v /mio/progetto:/datasets/code <mia_immagine_odm> --project-path /datasets --dtm --dem-release 2 --smrf-threshold 0.4 --smrf-window 24
```
