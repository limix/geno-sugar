.. _public:

****************
Public Interface
****************

- :ref:`utils_ref`

  - :func:`.snp_query`
  - :func:`.is_in`
  - :func:`.standardize_snps`
  - :func:`.unique_variants`

- :ref:`genoqueue_ref`

  - :class:`.GenoQueue`

- :ref:`preprocess_ref`

  - :func:`.preprocess.standardize`
  - :func:`.preprocess.inpute`
  - :func:`.preprocess.compose`



.. _utils_ref:

Utils
^^^^^
.. automodule:: geno_sugar.utils
  :members:

  
.. _genoqueue_ref:

Geno Queue
^^^^^^^^^^

Iterator class facilitating genome-wide analyses by
(i) loading the genetic data in batches of snps, and
(ii) applying user-specified functions for preprocessing and filtering.

.. autoclass:: geno_sugar.geno_queue.GenoQueue
  :members:


.. _preprocess_ref:

Preprocess
^^^^^^^^^^

Preprocess functions return functions that take
as only argument the array-like genetic matrix

.. automodule:: geno_sugar.preprocess
  :members:
