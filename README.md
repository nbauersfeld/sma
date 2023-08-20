# Praxisprojekt

01.data
collects raw data from a project folder, that contains time based images and meta data from a mobile
with a special fiber mount for the analysis of NO2, NH4, PH4 concentrations in a reagence

to get an idea, how sample images are recorded, a schematic image description supports by
 ![](doc/media/aperture.png =300x)

1) camera chassis
2) mount to hold
3) the fiber channel and
4) reagence vessel with a given
5) reagent and sample, that is
6) enlighted by cameras flash light and
7) recorded with cameras foto diode

02.sample
samples projects and puts relevant cluster results into project specific data stores

03.merge
merges the samples from different data stores into a data container to evaluate

04.evaluate
contains first evaluation results of two NO2 projects and a training for a OLS model with test
conclusions are given at the end of this file
