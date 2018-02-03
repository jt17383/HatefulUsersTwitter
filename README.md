# Like Sheep Among Wolves

This folder contains the data and the analysis done in the papers:

    "Like Sheep Among Wolves":  Characterizing Hateful Users on Twitter
    Manoel Horta Ribeiro, Pedro H Calais, Yuri A Santos,  Virgílio AF Almeida, Wagner Meira Jr
    to be presented @ MIS2 workshop at WSDM'18
    
    Characterizing and Detecting Hateful Users on Twitter
    Manoel Horta Ribeiro, Pedro H Calais, Yuri A Santos,  Virgílio AF Almeida, Wagner Meira Jr
    under review :)
    
The experiments with the *GraphSage* algorithm are in [another repository](colocar aqui).

The dataset can be downloaded [here on Kaggle](colocar aqui).

## Folder Structure

These are the main folders, reproducible with the dataset downloaded from **Kaggle**:

- `./analysis/` contains scripts exploring the dataset collected.

- `./classification/` contains scripts with the classifiers (duh).

These folders are not reproducible, but they are present just in for completeness:

- `./crawler/` contains the code used to extract the dataset. You need to set neo4j to run it.

- `./prepreprocessing/` contains scripts to select the users to be annotated, and extract their tweets.

- `./features/` contains scripts to get the features to be analyzed and that will be fed into the classifier.

Auxiliary folders:

- `./data/` data generated by data wrangling.

- `./secrets/` for the API/DB authentication stuff.

- `./tmp/` auxiliary scripts.

- `./img/` images generated by analyses.
    
# Reproducibility

Some of the files used are not shared because sharing them violates Twitter's guidelines. 
However, we do our best to ensure reproducibility:

- all the data analysis process is throughoutly explained with jupyter notebooks :)

- you can download the following files here (to be added):

    -   `bad_words.txt`
    -   `lexicon.txt`
