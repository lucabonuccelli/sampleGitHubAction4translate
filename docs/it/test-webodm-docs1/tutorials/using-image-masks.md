---

titolo: Utilizzo delle maschere immagine
---


Le persone possono fornire maschere di immagine per informare il software di saltare la ricostruzione su determinate aree. Ciò è utile nei casi in cui il cielo è stato accidentalmente incluso nelle foto di input provenienti da scatti obliqui, o semplicemente per limitare la ricostruzione di un singolo soggetto.

Per aggiungere una maschera, crea semplicemente una nuova immagine in bianco e nero della stessa dimensione dell'immagine di destinazione che desideri mascherare (puoi utilizzare un programma come GIMP per farlo). Colorare in nero le aree da escludere dalla ricostruzione.

![Immagine di destinazione](/images/target_image.webp)

![Maschera immagine](/images/target_image_mask.webp)

![Risultato 3D con maschera applicata](/images/3D_result.webp)

Dai un nome al tuo file:

`<nomefile>_maschera.JPG`

Ad esempio, "DJI_0018.JPG" può avere una maschera creando un file "DJI_0018_mask.JPG" e includendolo nell'elenco delle immagini. È possibile utilizzare i formati `.JPG`, `.PNG`, `.BMP` e `.TIF` per le maschere immagine.
