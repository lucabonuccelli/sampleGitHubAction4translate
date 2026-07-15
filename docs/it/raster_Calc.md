# Calcolatore raster QGIS

Il **Calcolatore Raster** è uno strumento di QGIS che ti consente di creare nuovi set di dati raster applicando espressioni matematiche e logiche a uno o più layer raster esistenti.

Ogni pixel del raster di output viene calcolato in modo indipendente utilizzando i valori dei pixel corrispondenti dei raster di input. Ciò rende il calcolatore raster uno strumento potente per eseguire analisi spaziali, derivare nuovi set di dati e automatizzare attività complesse di elaborazione raster.

## Usi comuni

Il calcolatore raster può essere utilizzato per:

* Eseguire operazioni aritmetiche come addizione, sottrazione, moltiplicazione e divisione.
* Combina più livelli raster in un unico output.
* Calcola gli indici di vegetazione come l'NDVI.
* Riclassificare i valori raster.
* Crea maschere binarie utilizzando espressioni condizionali.
* Converti unità o applica fattori di scala.
* Genera pendenza, aspetto o altri set di dati derivati ​​da prodotti raster intermedi.
* Applicare soglie e condizioni logiche per identificare aree di interesse specifiche.

## Operazioni supportate

Le espressioni possono includere:

* Operatori aritmetici: `+`, `-`, `*`, `/`, `^`
* Operatori di confronto: `>`, `<`, `>=`, `<=`, `=`, `!=`
* Operatori logici: `AND`, `OR`, `NOT`
* Funzioni matematiche come `sin()`, `cos()`, `sqrt()`, `log()`, `exp()`, `abs()` e molte altre.

Per esempio:

```text
("DEM@1" > 1000) * "LandCover@1"
```

Questa espressione mantiene i valori del raster **LandCover** solo dove la quota è maggiore di 1000 metri, assegnando zero altrove.

Un altro esempio:

```text
("NIR@1" - "Rosso@1") / ("NIR@1" + "Rosso@1")
```

Questo calcola l'**Indice di differenza di vegetazione normalizzata (NDVI)** dalle bande spettrali del vicino infrarosso e del rosso.

## Produzione

Il Calcolatore Raster genera un nuovo layer raster il cui:

* estensione,
* risoluzione,
* sistema di riferimento delle coordinate (CRS), e
* valori dei pixel

sono determinati dai layer di input selezionati e dai parametri di calcolo scelti.

## Flusso di lavoro tipico

1. Carica i layer raster richiesti in QGIS.
2. Aprire **Raster → Calcolatrice raster**.
3. Costruisci l'espressione desiderata utilizzando bande e funzioni raster.
4. Specificare il file di output e le opzioni di elaborazione.
5. Eseguire il calcolo per generare il nuovo raster.

Il raster risultante può quindi essere visualizzato, analizzato o utilizzato come input per ulteriori flussi di lavoro di elaborazione geospaziale.
