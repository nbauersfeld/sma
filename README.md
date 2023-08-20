# practical project

author: Norman Bauersfeld, Von-Garßen-Str. 12, 38640 Goslar, u37724

preamble

main topics to begin with a low budget solution evaluation testing water characteristics:

- sustainable water supply
- long-term securing of the water cycle and
- protection of water importance

reasons to ensure supply of clean water

- climate change, pollution, and a growing urban population
- simple but effective on-site analysis of relevant parameters is required
- identify contaminations
- search for causes
- initiate countermeasures

achievements

- with aim of a project of the development of a simple and inexpensive smartphone-based measurement system for in situ water analysis
- quantitative proof of relevant parameter realization and validation with a simple means and with a reduced need for chemicals (reagences)
- use of a common mobile camera and flash light, in combination with a mount (from the 3D printer and with a functionalized polymer film), should enable qualitative and quantitative detection of the target molecules (NO2, PH4 or NH4)

01.data
collects raw data from a project folder, that contains time based images and meta data from a mobile
with a special fiber mount for the analysis of NO2, NH4, PH4 concentrations in a reagence

to get an idea, how sample images are recorded, a schematic image description supports by
![](doc/media/aperture.png)

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

notes

- a first approach description (german) is given by doc/sma_review.pdf,
  that shows the data understanding, preparation, modelling and evaluation chain;
  the coresponding quantity/quality report and a schematic view of sample preparation,
  sample merge and a (small) conclusion
- html prints of the jupyther notebooks are given in the html folder
- raw sample data ist given in the raw folder
- evaluation, training and test data is given in the data folder
- python implementation of ZMeans and Utilities are given in the _ZMeans.py script
