---

titolo: Diagramma di flusso di opzioni e flag
modello: doc
---

```mermaid

diagramma di flusso della tubercolosi

Immagini@{ shape: docs, label: "Immagini"}

sottografo DatasetGroup[" "]
direzione RL
Set di dati["Set di dati"]
ds_bg["rimozione-bg"]
ds_camera_lens["obiettivo-fotocamera"]
ds_cameras["fotocamere"]
ds_gcp["gcp"]
ds_geo["geo"]
ds_gps_accuracy["precisione-gps"]
ds_primary_band["banda-primaria"]
ds_sky_removal["rimozione del cielo"]
ds_use_exif["usa-exif"]
ds_video_limit["limite video"]
ds_video_solving["risoluzione video"]

ds_bg ~~~ ds_camera_lens
ds_cameras ~~~ ds_gcp
ds_geo ~~~ ds_gps_accuracy
ds_primary_band ~~~ ds_sky_removal
ds_use_exif ~~~ ds_video_limit
ds_video_risoluzione

fai clic su ds_bg "../options-flags/#bg-removal"
fai clic su ds_camera_lens "../options-flags/#camera-lens"
fai clic su ds_cameras "../options-flags/#cameras"
fare clic su ds_gcp "../options-flags/#gcp"
fare clic su ds_geo "../options-flags/#geo"
fai clic su ds_gps_accuracy "../options-flags/#gps-accuracy"
fai clic su ds_primary_band "../options-flags/#primary-band"
fai clic su ds_sky_removal "../options-flags/#sky-removal"
fare clic su ds_use_exif "../options-flags/#use-exif"
fai clic su ds_video_limit "../options-flags/#video-limit"
fai clic su ds_video_length "../options-flags/#video-release"
FINE


sottografo GruppoDiviso[" "]
direzione RL
Dividi["Dividi"]
split_sm_cluster["sm-cluster"]
split_sm_no_align["sm-no-align"]
diviso_diviso["diviso"]
gruppi_immagine_divisi["gruppi-immagine-divisi"]
split_overlap["split-sovrapposizione"]
Diviso
split_sm_cluster ~~~ split_sm_no_align
split_split ~~~ split_image_groups
split_overlap

fai clic su split_sm_cluster "../options-flags/#sm-cluster"
fai clic su split_sm_no_align "../options-flags/#sm-no-align"
fai clic su split_split "../options-flags/#split"
fai clic su split_image_groups "../options-flags/#split-image-groups"
fai clic su split_overlap "../options-flags/#split-overlap"
FINE

Divisione["`**Divisione**`"]


sottografo OpenSFMGroup[" "]
direzione RL
ApriSFM["ApriSFM"]
sfm_feature_quality["funzionalità-qualità"]
sfm_feature_type["tipo-funzione"]
sfm_force_gps["forza-gps"]
sfm_ignore_gsd["ignore-gsd"]
sfm_matcher_neighbors["matcher-vicini"]
sfm_matcher_order["ordine-matcher"]
sfm_matcher_type["tipo di matcher"]
sfm_min_num_features["min-num-features"]
sfm_pc_quality["qualità-pc"]
sfm_radiometric_calibration["calibrazione-radiometrica"]
sfm_rolling_shutter["avvolgibile"]
sfm_rolling_shutter_readout["lettura-otturatore-rolling"]
algoritmo_sfm["algoritmo-sfm"]
sfm_no_partial["sfm-no-parziale"]
sfm_skip_band_alignment["salta-allineamento-banda"]
sfm_use_fixed_camera_params["usa-parametri-fotocamera-fissi"]
sfm_use_hybrid_bundle_adjustment["usa-hybrid-bundle-adjustment"]

OpenSFM
sfm_feature_quality ~~~ sfm_feature_type
sfm_force_gps ~~~ sfm_ignore_gsd
sfm_matcher_neighbors ~~~ sfm_matcher_order
sfm_matcher_type ~~~ sfm_min_num_features
sfm_pc_quality ~~~ sfm_radiometric_calibration
sfm_rolling_shutter ~~~ sfm_rolling_shutter_readout
sfm_algoritmo ~~~ sfm_no_partial
sfm_skip_band_alignment ~~~ sfm_use_fixed_camera_params
sfm_use_hybrid_bundle_adjustment

fare clic su sfm_feature_quality "../options-flags/#feature-quality"
fai clic su sfm_feature_type "../options-flags/#feature-type"
fai clic su sfm_force_gps "../options-flags/#force-gps"
fare clic su sfm_ignore_gsd "../options-flags/#ignore-gsd"
fai clic su sfm_matcher_neighbors "../options-flags/#matcher-neighbors"
fai clic su sfm_matcher_order "../options-flags/#matcher-order"
fai clic su sfm_matcher_type "../options-flags/#matcher-type"
fai clic su sfm_min_num_features "../options-flags/#min-num-features"
fare clic su sfm_pc_quality "../options-flags/#pc-quality"
fare clic su sfm_radiometric_calibration "../options-flags/#radiometric-calibration"
fare clic su sfm_rolling_shutter "../options-flags/#rolling-shutter"
fare clic su sfm_rolling_shutter_readout "../options-flags/#rolling-shutter-readout"
fare clic su sfm_algorithm "../options-flags/#sfm-algorithm"
fare clic su sfm_no_partial "../options-flags/#sfm-no-partial"
fai clic su sfm_skip_band_alignment "../options-flags/#skip-band-alignment"
fai clic su sfm_use_fixed_camera_params "../options-flags/#use-fixed-camera-params"
fai clic su sfm_use_hybrid_bundle_adjustment "../options-flags/#use-hybrid-bundle-adjustment"
FINE

sottografo OpenMVSGroup[" "]
direzione RL
OpenMVS["OpenMVS"]
openmvs_pc_filter["filtro-pc"]
openmvs_pc_skip_geometric["pc-skip-geometric"]

OpenMVS
openmvs_pc_filter ~~~ openmvs_pc_skip_geometric

fai clic su openmvs_pc_filter "../options-flags/#pc-filter"
fai clic su openmvs_pc_skip_geometric "../options-flags/#pc-skip-geometric"
FINE

sottografo FilterpointsGroup[" "]
direzione RL
Punti filtro["Punti filtro"]
filter_auto_boundary["confine automatico"]
filter_auto_boundary_distance["distanza-limite-auto"]
filtro_confine["confine"]
filter_fast_ortofoto["ortofotoveloce"]
filter_pc_sample["pc-campione"]

Punti filtro
filter_auto_boundary ~~~ filter_auto_boundary_distance
filter_boundary ~~~ filter_fast_orthophoto
filtro_pc_campione

fai clic su filter_auto_boundary "../options-flags/#auto-boundary"
fai clic su filter_auto_boundary_distance "../options-flags/#auto-boundary-distance"
fai clic su filter_boundary "../options-flags/#boundary"
fai clic su filter_fast_orthophoto "../options-flags/#fast-orthophoto"
fai clic su filter_pc_sample "../options-flags/#pc-sample"
FINE

sottografo MeshingGroup[" "]
direzione RL
Mesh["Mesh"]
mesh_octree_profondità["mesh-octree-profondità"]
dimensione_maglia["dimensione-maglia"]
mesh_skip_3dmodel["salta-3dmodel"]
Meshing
mesh_octree_ Depth ~~~ mesh_size ~~~ mesh_skip_3dmodel

fai clic su mesh_octree_length "../options-flags/#mesh-octree-length"
fare clic su mesh_size "../options-flags/#mesh-size"
fai clic su mesh_skip_3dmodel "../options-flags/#skip-3dmodel"
FINE

sottografo MvsTexturingGroup[" "]
direzione RL

MvsTexturing["MvsTexturing"]
texturing_keep_unseen_faces["texturing-keep-unseen-faces"]
texturing_monomateriale["texturing-monomateriale"]
texturing_skip_global_seam_leveling["texturing-skip-global-seam-leveling"]
texturing_use_3dmesh["usa-3dmesh"]
MvsTexturing

texturing_keep_unseen_faces
texturing_single_material ~~~ texturing_skip_global_seam_leveling
texturing_use_3dmesh

fai clic su texturing_keep_unseen_faces "../options-flags/#texturing-keep-unseen-faces"
fai clic su texturing_single_material "../options-flags/#texturing-single-material"
fai clic su texturing_skip_global_seam_leveling "../options-flags/#texturing-skip-global-seam-leveling"
fai clic su texturing_use_3dmesh "../options-flags/#use-3dmesh"
FINE

sottografoGeoreferencingGroup[" "]
direzione RL
Georeferenziazione["Georeferenziazione"]
georef_align["allineare"]
georef_crop["ritaglia"]
georef_pc_classifica["classifica-pc"]
georef_pc_copc["pc-copc"]
georef_pc_csv["pc-csv"]
georef_pc_ept["pc-ept"]
georef_pc_las["pc-las"]
Georeferenziazione
georef_align ~~~ georef_crop
georef_pc_classify ~~~ georef_pc_copc
georef_pc_csv ~~~ georef_pc_ept
georef_pc_las

fai clic su georef_align "../options-flags/#align"
fare clic su georef_crop "../options-flags/#crop"
fai clic su georef_pc_classify "../options-flags/#pc-classify"
fare clic su georef_pc_copc "../options-flags/#pc-copc"
fare clic su georef_pc_csv "../options-flags/#pc-csv"
fai clic su georef_pc_ept "../options-flags/#pc-ept"
fare clic su georef_pc_las "../options-flags/#pc-las"
FINE

sottografo DEMGroup[" "]
direzione RL
DEM["DEM"]
dem_cog["ingranaggio"]
dem_decimazione["dem-decimazione"]
dem_euclidea_mappa["dem-euclidea-mappa"]
dem_gapfill_steps["dem-gapfill-steps"]
risoluzione_dem["risoluzione-dem"]
dem_dsm["dsm"]
dem_dtm["dtm"]
dem_smrf_scalare["smrf-scalare"]
dem_smrf_slope["smrf-pendenza"]
dem_smrf_threshold["smrf-soglia"]
dem_smrf_window["finestra smrf"]
dem_tiles["piastrelle"]
DEM

dem_cog ~~~ dem_decimazione
dem_euclidean_map ~~~ dem_gapfill_steps
dem_risoluzione ~~~ dem_dsm
dem_dtm ~~~ dem_smrf_scalar
dem_smrf_slope ~~~ dem_smrf_threshold
dem_smrf_window ~~~ dem_tiles

fare clic su dem_cog "../options-flags/#cog"
fai clic su dem_decimation "../options-flags/#dem-decimation"
fare clic su dem_euclidean_map "../options-flags/#dem-euclidean-map"
fai clic su dem_gapfill_steps "../options-flags/#dem-gapfill-steps"
fai clic su dem_length "../options-flags/#dem-release"
fare clic su dem_dsm "../options-flags/#dsm"
fare clic su dem_dtm "../options-flags/#dtm"
fare clic su dem_smrf_scalar "../options-flags/#smrf-scalar"
fare clic su dem_smrf_slope "../options-flags/#smrf-slope"
fai clic su dem_smrf_threshold "../options-flags/#smrf-threshold"
fai clic su dem_smrf_window "../options-flags/#smrf-window"
fai clic su dem_tiles "../options-flags/#tiles"
FINE

sottografoOrtofotoGruppo[" "]
direzione RL
Ortofoto["Ortofoto"]
ortho_build_overviews["build-overviews"]
ortho_compression["ortofoto-compressione"]
ortho_cutline["ortofoto-cutline"]
ortho_kmz["ortofoto-kmz"]
ortho_no_tiled["ortofoto-no-piastrellata"]
ortho_png["ortofoto-png"]
risoluzione_orto["risoluzione-ortofoto"]
ortho_skip["salta-ortofoto"]
Ortofoto
ortho_build_overviews ~~~ ortho_compression
ortho_cutline ~~~ ortho_kmz
ortho_no_tiled ~~~ ortho_png
risoluzione_orto ~~~ salto_orto

fai clic su ortho_build_overviews "../options-flags/#build-overviews"
fai clic su ortho_compression "../options-flags/#orthophoto-compression"
fai clic su ortho_cutline "../options-flags/#orthophoto-cutline"
fai clic su ortho_kmz "../options-flags/#orthophoto-kmz"
fai clic su ortho_no_tiled "../options-flags/#orthophoto-no-tiled"
fai clic su ortho_png "../options-flags/#orthophoto-png"
fai clic su ortho_length "../options-flags/#orthophoto-release"
fai clic su ortho_skip "../options-flags/#skip-orthophoto"
FINE

sottografo ReportGroup[" "]
direzione TBC
Rapporto["Rapporto"]
report_skip["salta-rapporto"]
Segnala ~~~ report_skip
report_skip

fai clic su report_skip "../options-flags/#skip-report"
FINE

sottografo PostprocessGroup[" "]
direzione RL
Postelaborazione["Postelaborazione"]
post_3d_tiles["piastrelle 3d"]
post_copia_in["copia-in"]
post_gltf["gltf"]
Postelaborazione
post_3d_tiles ~~~ post_copy_to ~~~ post_gltf

fai clic su post_3d_tiles "../options-flags/#3d-tiles"
fai clic su post_copy_to "../options-flags/#copy-to"
fai clic su post_gltf "../options-flags/#gltf"
FINE

Immagini e01@==> DatasetGroup
DatasetGroup e02@--> Gruppo diviso

SplitGroup == Sì ==> Divisione ==> OpenSFMGroup
Gruppo diviso == No ==> OpenSFMGroup

OpenSFMGroup e02@--> OpenMVSGroup
OpenMVSGroup e03@--> FilterpointsGroup
FilterpointsGroup e04@--> MeshingGroup
MeshingGroup e05@--> MvsTexturingGroup
MvsTexturingGroup e06@--> GeoreferencingGroup
GeoreferenziazioneGruppo e07@--> DEMGroup
DEMGroup e08@--> OrtofotoGruppo
OrthophotoGroup e09@--> ReportGroup
ReportGroup e10@--> PostprocessGroup



sottografo classDefRiempimento titolo:#1f2937,tratto:#94a3b8,larghezza tratto:1.5px,colore:#fff,peso carattere:grassetto;
classDef verdeRiempimento nodo:#90EE90,tratto:#2d5016,larghezza tratto:1px,colore:#000;
classDef blueRiempimento nodo: #87CEEB, tratto: # 1e3a5f, larghezza tratto: 1px, colore: #000;
classDef rosaRiempimento nodo:#FFB6C1, tratto:#8b3a3a, larghezza tratto: 1px, colore:#000;
classDef violaRiempimento nodo:#DDA0DD,tratto:#5d3a5d,larghezza tratto:1px,colore:#000;
classDef gialloRiempimento nodo:#F0E68C,tratto:#8b8b00,larghezza tratto:1px,colore:#000;
classDef arancioneRiempimento nodo:#FFA07A, tratto:#8b4513, larghezza tratto: 1px, colore:#000;
classDef mintRiempimento nodo:#98FB98,tratto:#3a5f3a,larghezza tratto:1px,colore:#000;
classDef goldRiempimento nodo:#FFD700, tratto:#8b7500, larghezza tratto: 1px, colore:#000;
classDef skyNode fill:#87CEFA,stroke:#1e3a8a,stroke-width:1px,color:#000;
classDef sabbiaRiempimento nodo:#DEB887, tratto:#5d4e37, larghezza tratto: 1px, colore:#000;
classDef redRiempimento nodo:#F08080, tratto:#8b3a3a, larghezza tratto: 1px, colore:#000;
classDef verde acquaRiempimento nodo:#20B2AA, tratto:#0d5d5d, larghezza tratto: 1px, colore:#000;
classDef animatoEdge tratto-dasharray: 9,5,tratto-dashoffset: 900,animazione: trattino 25s lineare infinito;

classe e01,e02,e03,e04,e05,e06,e07,e08,e09,e10 bordo animato;


classe Dataset,Split,OpenSFM,OpenMVS,Filterpoints,Meshing,MvsTexturing,Georeferenziazione,DEM,Ortofoto,Report,Postprocess subgraphTitle;
class ds_bg,ds_camera_lens,ds_cameras,ds_gcp,ds_geo,ds_gps_accuracy,ds_primary_band,ds_sky_removal,ds_use_exif,ds_video_limit,ds_video_release greenNode;
class Immagini,split_sm_cluster,split_sm_no_align,split_split,split_image_groups,split_overlap blueNode;
classe sfm_feature_quality,sfm_feature_type,sfm_force_gps,sfm_ignore_gsd,sfm_matcher_neighbors,sfm_matcher_order,sfm_matcher_type,sfm_min_num_features,sfm_pc_quality,sfm_radiometric _calibrazione,sfm_rolling_shutter,sfm_rolling_shutter_readout,sfm_algorithm,sfm_no_partial,sfm_skip_band_alignment,sfm_use_fixed_camera_params,sfm_use_hybrid_bundle_adjustment pinkNodo;
class openmvs_pc_filter,openmvs_pc_skip_geometric purpleNode;
class filter_auto_boundary,filter_auto_boundary_distance,filter_boundary,filter_fast_orthophoto,filter_pc_sample yellowNode;
class mesh_octree_ Depth, mesh_size, mesh_skip_3dmodel orangeNode;
class texturing_keep_unseen_faces,texturing_single_material,texturing_skip_global_seam_leveling,texturing_use_3dmesh mintNode;
class georef_align,georef_crop,georef_pc_classify,georef_pc_copc,georef_pc_csv,georef_pc_ept,georef_pc_las goldNode;
classe dem_cog,dem_decimation,dem_euclidean_map,dem_gapfill_steps,dem_solving,dem_dsm,dem_dtm,dem_smrf_scalar,dem_smrf_slope,dem_smrf_threshold,dem_smrf_window,dem_tiles skyNode;
divisione della classe,ortho_build_overviews,ortho_compression,ortho_cutline,ortho_kmz,ortho_no_tiled,ortho_png,ortho_solving,ortho_skip sandNode;
classe report_skip redNode;
class post_3d_tiles,post_copy_to,post_gltf tealNode;

```