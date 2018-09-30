*******
Install
*******

Conda
^^^^^

TODO


Manual
^^^^^^

Geno-sugar requires scipy, numpy, matplotlib, pandas, scikit-learn, pandas_plink and bgen_reader among other Python packages.

* Create a new environment in conda_::

    conda create -n geno-sugar python=3.6
    source activate geno-sugar

* Install dependencies::

    conda install -c conda-forge scipy numpy matplotlib pandas sphinx sphinx_rtd_theme scikit-learn pandas-plink bgen-reader

* Install geno-sugar::

    git clone https://github.com/limix/geno-sugar.git
    cd geno-sugar
    python setup.py install

* Build the documentation::

    cd doc
    make html

The documentation is in HTML and will be available at
``_build/html/index.html``.

.. _conda: https://conda.io
