# geno-sugar
Utility functions to read bed and bgen files and facilitate genome-wide analyses.

# Install

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

# Quick start

.. _quickstart:

*********************
Quick Start in Python
*********************

We here show how to run geno-wide analysis using plink and bgen files
using geno-sugar.

Plink file example
^^^^^^^^^^^^^^^^^^

Before getting started, let's get some data::

    wget http://www.ebi.ac.uk/~casale/data_structlmm.zip
    unzip data_structlmm.zip

Now we are ready to go.

.. literalinclude:: quickstart_plink.py
   :encoding: latin-1

The following script can be downloader :download:`here <quickstart_plink.py>`.

Bgen file example
^^^^^^^^^^^^^^^^^

Before getting started, let's get some data::

    mkdir data
    wget https://github.com/limix/bgen-reader-py/blob/master/example/example.bgen data/.

Now we are ready to go.

.. literalinclude:: quickstart_bgen.py
   :encoding: latin-1

The following script can be downloader :download:`here <quickstart_bgen.py>`.

# Developer

Francesco Paolo Casale
