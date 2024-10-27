<div align="center">

# SARS-CoV-2 Variants Clustering

<div align="left">

<h2 id="first-section">What is this repo about?</h2>

This repo contains Python implementations for clustering spike protein sequences into recognized variants, aiding study on the spread and dynamics of rapidly emerging variants.

The spike sequences were retrieved from a publicly available dataset of SARS-CoV-2 spike sequences, which were then stored in a NumPy binary file (`filtered_protein_seq.npy`) for efficient data storage and read time.

To begin with, a $k$-mers-based approach is used to generate frequency vector representations of the spike sequences. Following that, feature selection process is applied on these feature vectors to mitigate the curse of dimensionality during clustering.

Finally, both hard and soft clustering methods are then used on these feature vectors, achieving high $F_1$ scores that allow for accurate, precise, yet efficient clustering of spike sequences by variant.

## Before using this repo...

First, clone this repo to your local machine. Then, create a new conda environment with its dependencies by executing the following syntax in terminal or console.

> Note: This repo is accelerated with Intel(R) Extension for Scikit-learn. So, make sure to clone this repo on Intel-powered local machine.

```
conda env create --file requirements.yml
```

After a new conda environment created, activate the environment by

```
conda activate sars-cov-2_clustering
```

Fuzzy C-Means clustering method is still not available in conda package manager. While in the activated `sars-cov-2_clustering` environment, install fuzzy-c-means package with `pip`.

```
pip install fuzzy-c-means
```

## How to use this repo?

First, as stated in [What is this repo about?](#first-section), a $k$-mers-based approach is performed by executing the following syntax on terminal/console.

> Ensure that your current working directory is set to the cloned repo.

```
python featureVec_Generator.py
```

After generating the feature vectors and saving them in a NumPy binary files, clustering can be performed using the methods in each respective folder.

In each respective clustering methods folder, you will find folders as follows.
- org/
  - Clustering is done without applying any feature selection method on the feature vectors.
  - Longer runtime and low $F_1$ score.
- Boruta/
  - Clustering is done after applying 
