# practical project

author: Norman Bauersfeld, Von-Garßen-Str. 12, 38640 Goslar, u37724

**preamble**

main topics to begin with a low budget solution evaluation testing water characteristics

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

**files**

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

**conclusion**

* ideas of the framework adapted can be found by different sources of publications, e.g. given by references (Zeit, 2017), (IISA, 2019) or (IFF, 2019)
* a first prototype of the mobile mount or chassis was build with a specific fiber channel
* reagences where selected to identify the target molecules
* an understanding was evolved, how a reagence indicate a concentration of a target and how could it be possible to evaluate in color space and by sample images
* labeled test and train data was provided by a local water supplier to build models to identify target molecules within an appropriate model in machine learning
* different kinds of models (with a comparable machine learning algorithm) where developed
  * a model to compare and setup data of different target molecules to setup and select the model to predict a concentration of the target
  * a model to compare and predict data of the same target molecule
* a mobile app was developed to store images from the fiber channel aperture by the mobile flash light and camera, evaluate them and extract the actual value of concentration of the prefered target molecules by a pre-defined model on site
* sample image collections where transfered to a cloud store or online folder to post train the models to identify the target molecules
* interation steps where planed to improve models, app handling and mount construction
* field tests where applied to test the first models, mount and mobile app handling
* the on site data samples where fit with OLS models; statistical tests where applied

**challenges**

* the chassis construction has to be accurate to mount to a mobile of a special type without loss of measurement information
* the fiber channel begin and end has to be plane enough to avoid shadowing or even fringing
* the reagences has to be well prepared in a vessel and easy to handle on site
* the machine learning model (implemented by ZMeans; (Ng, A., 2012) and (Jan et. al., 1988)) has to be appropriate to the evaluation case in the sample color space, easy to implement for on site analysis and embedded devices, fast to execute to give results, post trainable and transferable
* a 1st model has to identifiy the target working space
* a 2nd model hast to predict the concentration of the target molecule
* the mobile app has always be up to date and understandable in its one page design
* the mobile app has pre-trained models to evaluate the the image samples and detect target molecules in an appropriate way just in time and on site (depends on the reagence behaviour)
* the mobile app can restore all on site measurements to an online folder; if the mobile is online and in a special network area, data should be transfered over secure channels
* the transfered samples has to be used to retrain the reagence models to keep the mobile app models up to date;
  evaluation is necessary whether a preview by an engineer or automatic application is possible
* the inclusion of local water suppliers improve the created results and gives an evaluation by experts
  (but can be time consuming and annoying)
* a common system description of the system should be applied to make it usable
* the OLS models fits to coefficients with the assumption that the residuals are independent to each other; statistical test do not support this actually by showing assumption violations (Durbin-Watson-Test, (Zach, 2023))

**references**

- Zeit (2017, 02). Dies App macht das Smartphone zum Spektrometer. https://www.zeit.de/digital/mobil/2017-02/hawkspex-mobile-app-fraunhofer-institut-gemuese-pestizide-erkennung
- IISA (2019, 07). Spektralanalysen mit dem Smartphone. https://www.investieren-in-sachsen-anhalt.de/presse/nachrichten-iisa/2019/07/spektralanalysen-mit-dem-smartphone
- IFF (2019, 07). Presseinformation. https://www.iff.fraunhofer.de/content/dam/iff/de/dokumente/pressemappe/pm20190702-spektralanalysen-mit-smartphone-iq-innovationspreis-mitteldeutschland-fuer-scantechnologie-des-fraunhofer-iff.pdf
- Zach (2023, August 27). Durbin-Watson-Test. http://www.stratology.org/durbin-watson-test
- Ng, A. (2012). Clustering with the k-means algorithm. Machine Learning, 1-2.
- Jain, A. K., & Dubes, R. C. (1988). Algorithms for clustering data. Prentice-Hall, Inc.

**notes**

- a first approach description (german) is given by doc/sma_review.pdf,
  that shows the data understanding, preparation, modelling and evaluation chain;
  the coresponding quantity/quality report and a schematic view of sample preparation,
  sample merge and a (small) conclusion
- html prints of the jupyther notebooks are given in the html folder
- raw sample data ist given in the raw folder
- evaluation, training and test data is given in the data folder
- python implementation of ZMeans and Utilities are given in the _ZMeans.py script

version 2023-08-27
