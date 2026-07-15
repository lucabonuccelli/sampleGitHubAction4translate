# QGIS Raster Calculator

The **Raster Calculator** is one of the most important tools in QGIS that allows you to create new raster datasets by applying mathematical and logical expressions to one or more existing raster layers.

Each pixel of the output raster is calculated independently using the values of the corresponding pixels from the input rasters. This makes the Raster Calculator a powerful tool for performing spatial analysis, deriving new datasets, and automating complex raster processing tasks.

## note 
If You need something like "min/max value in a area" you hen to use other tools (Eg TODO)

## Common Uses

The Raster Calculator can be used to:

* Perform arithmetic operations such as addition, subtraction, multiplication, and division.
* Combine multiple raster layers into a single output.
* Calculate vegetation indices such as NDVI.
* Reclassify raster values.
* Create binary masks using conditional expressions.
* Convert units or apply scaling factors.
* Generate slope, aspect, or other derived datasets from intermediate raster products.
* Apply thresholds and logical conditions to identify specific areas of interest.

## Supported Operations

Expressions may include:

* Arithmetic operators: `+`, `-`, `*`, `/`, `^`
* Comparison operators: `>`, `<`, `>=`, `<=`, `=`, `!=`
* Logical operators: `AND`, `OR`, `NOT`
* Mathematical functions such as `sin()`, `cos()`, `sqrt()`, `log()`, `exp()`, `abs()`, and many others.

For example:

```text
("DEM@1" > 1000) * "LandCover@1"
```

This expression keeps the values from the **LandCover** raster only where the elevation is greater than 1000 meters, assigning zero elsewhere.

Another example:

```text
("NIR@1" - "Red@1") / ("NIR@1" + "Red@1")
```

This computes the **Normalized Difference Vegetation Index (NDVI)** from near-infrared and red spectral bands.

## Output

The Raster Calculator generates a new raster layer whose:

* resolution,
* coordinate reference system (CRS), and
* pixel values

are determined by the selected input layers and the chosen calculation parameters.

## Typical Workflow

1. Load the required raster layers into QGIS.
2. Open **Raster → Raster Calculator**.
3. Build the desired expression using raster bands and functions.
4. Specify the output file and processing options.
5. Run the calculation to generate the new raster.

The resulting raster can then be visualized, analyzed, or used as input for further geospatial processing workflows.
