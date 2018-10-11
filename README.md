# geno-sugar

[![Travis](https://img.shields.io/travis/com/limix/geno-sugar.svg?style=flat-square&label=linux%20%2F%20macos%20build)](https://travis-ci.com/limix/geno-sugar)

Utility functions to read bed and bgen files and facilitate genome-wide analyses.

## Install

Geno-sugar requires scipy, numpy, matplotlib, pandas, scikit-learn, pandas_plink and bgen_reader among other Python packages.

* Create a new conda environment:

    ```bash
    conda create -n geno-sugar python=3.6
    source activate geno-sugar
    ```

* Install dependencies::

    ```bash
    conda install -c conda-forge scipy numpy matplotlib pandas sphinx sphinx_rtd_theme scikit-learn pandas-plink bgen-reader
    ```

* Install geno-sugar::

    ```bash
    git clone https://github.com/limix/geno-sugar.git
    cd geno-sugar
    python setup.py install
    ```

* Build the documentation::

    ```bash
    cd doc
    make html
    ```

The documentation is in HTML and will be available at
``_build/html/index.html``.

## Quick start

We here show how to run geno-wide analysis using plink and bgen files using geno-sugar.

## Plink file example

Before getting started, let's get some data::

```bash
wget http://www.ebi.ac.uk/~casale/data_structlmm.zip
unzip data_structlmm.zip
```

Now we are ready to go.

```python
import numpy as np
from pandas_plink import read_plink
import geno_sugar as gs
from sklearn.preprocessing import Imputer

# import genotype file
bedfile = 'data_structlmm/chrom22_subsample20_maf0.10'
(bim, fam, G) = read_plink(bedfile)

# subsample snps
Isnp = gs.is_in(bim, ('22', 17500000, 18500000))
G, bim = gs.snp_query(G, bim, Isnp)

# define geno preprocessing function
impute = gs.preprocess.impute(Imputer(missing_values=np.nan, strategy='mean', axis=1))
standardize = gs.preprocess.standardize()
preprocess = gs.preprocess.compose([impute, standardize])

# define filtering function
filter = gs.unique_variants

# loop on geno
queue = gs.GenoQueue(G, bim, batch_size=200, preprocess=preprocess, filter=filter)
for _G, _bim in queue:
    print('.. loaded %d/%d variants' % (_G.shape[0], G.shape[0]))
```

## Bgen file example

TODO
