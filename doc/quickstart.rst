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
