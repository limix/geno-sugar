.. _quickstart:

*********************
Quick Start in Python
*********************

We here show how to run geno-wide analysis using plink and bgen files
using geno-sugar.


Plink file example
^^^^^^^^^^^^^^^^^^

We need to first download and extract BED files, and then proceed with the example
of reading them.

.. testcleanup::

    import os
    import shutil

    if os.path.exists("data_structlmm.zip"):
        os.remove("data_structlmm.zip")

    if os.path.exists("data_structlmm"):
        shutil.rmtree("data_structlmm")

.. testcode::

    import numpy as np
    from pandas_plink import read_plink
    from sklearn.impute import SimpleImputer
    
    import geno_sugar as gs
    import geno_sugar.preprocess as prep

    
    gs.download("http://www.ebi.ac.uk/~casale/data_structlmm.zip")
    gs.unzip("data_structlmm.zip")
    
    # define random state
    random = np.random.RandomState(1)
    
    # import genotype file
    bedfile = "data_structlmm/chrom22_subsample20_maf0.10"
    (bim, fam, G) = read_plink(bedfile, verbose=False)
    
    # subsample snps
    Isnp = gs.is_in(bim, ("22", 17500000, 28500000))
    G, bim = gs.snp_query(G, bim, Isnp)
    
    # define geno preprocessing function
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    preprocess = prep.compose(
        [
            prep.filter_by_missing(max_miss=0.10),
            prep.impute(imputer),
            prep.filter_by_maf(min_maf=0.10),
            prep.standardize(),
        ]
    )
    
    # define filtering function
    filter = gs.unique_variants
    
    # loop on geno
    queue = gs.GenoQueue(G, bim, batch_size=200, preprocess=preprocess)
    for _G, _bim in queue:
        # run genetic analysis
        print("Result:", np.einsum("is,is->", random.rand(*_G.shape), _G))

.. testoutput::

    .. read 200 / 15929 variants (1.26%)
    Result: 39.31615841973354
    .. read 400 / 15929 variants (2.51%)
    Result: 60.14859050496203
    .. read 600 / 15929 variants (3.77%)
    Result: 55.331152201803974
    .. read 800 / 15929 variants (5.02%)
    Result: -6.754660482524052
    .. read 1000 / 15929 variants (6.28%)
    Result: -53.0330138600346
    .. read 1200 / 15929 variants (7.53%)
    Result: -28.67740460227282
    .. read 1400 / 15929 variants (8.79%)
    Result: -52.79766992650515
    .. read 1600 / 15929 variants (10.04%)
    Result: 79.23948191402047
    .. read 1800 / 15929 variants (11.30%)
    Result: -31.970194355365024
    .. read 2000 / 15929 variants (12.56%)
    Result: 24.525441851113786
    .. read 2200 / 15929 variants (13.81%)
    Result: -48.154400096220584
    .. read 2400 / 15929 variants (15.07%)
    Result: -62.707711729788215
    .. read 2600 / 15929 variants (16.32%)
    Result: 136.40189146745564
    .. read 2800 / 15929 variants (17.58%)
    Result: 98.58366080355582
    .. read 3000 / 15929 variants (18.83%)
    Result: -17.91015348468791
    .. read 3200 / 15929 variants (20.09%)
    Result: 36.21731334424119
    .. read 3400 / 15929 variants (21.34%)
    Result: 76.66526289877936
    .. read 3600 / 15929 variants (22.60%)
    Result: 2.2764654983047485
    .. read 3800 / 15929 variants (23.86%)
    Result: 72.3204050130708
    .. read 4000 / 15929 variants (25.11%)
    Result: 41.708157458158894
    .. read 4200 / 15929 variants (26.37%)
    Result: 4.48703122701581
    .. read 4400 / 15929 variants (27.62%)
    Result: -75.69136000949241
    .. read 4600 / 15929 variants (28.88%)
    Result: 48.13702616216051
    .. read 4800 / 15929 variants (30.13%)
    Result: 40.69527425370762
    .. read 5000 / 15929 variants (31.39%)
    Result: 41.55059257637385
    .. read 5200 / 15929 variants (32.64%)
    Result: 29.746125051086196
    .. read 5400 / 15929 variants (33.90%)
    Result: -146.22678609888834
    .. read 5600 / 15929 variants (35.16%)
    Result: 85.3328467745588
    .. read 5800 / 15929 variants (36.41%)
    Result: 60.41791541164633
    .. read 6000 / 15929 variants (37.67%)
    Result: -124.87024172520883
    .. read 6200 / 15929 variants (38.92%)
    Result: -36.578181837560756
    .. read 6400 / 15929 variants (40.18%)
    Result: -38.469877156502115
    .. read 6600 / 15929 variants (41.43%)
    Result: -138.4592756656873
    .. read 6800 / 15929 variants (42.69%)
    Result: 56.577704329353125
    .. read 7000 / 15929 variants (43.95%)
    Result: -80.6127449445221
    .. read 7200 / 15929 variants (45.20%)
    Result: -11.449427386001588
    .. read 7400 / 15929 variants (46.46%)
    Result: -93.54900003659337
    .. read 7600 / 15929 variants (47.71%)
    Result: -6.744703955747619
    .. read 7800 / 15929 variants (48.97%)
    Result: -44.129987933106094
    .. read 8000 / 15929 variants (50.22%)
    Result: -32.74345970500676
    .. read 8200 / 15929 variants (51.48%)
    Result: -64.23327234685601
    .. read 8400 / 15929 variants (52.73%)
    Result: 108.2817141901817
    .. read 8600 / 15929 variants (53.99%)
    Result: -41.89605216445146
    .. read 8800 / 15929 variants (55.25%)
    Result: -155.60904006432918
    .. read 9000 / 15929 variants (56.50%)
    Result: -42.593669143248114
    .. read 9200 / 15929 variants (57.76%)
    Result: 70.25528000060257
    .. read 9400 / 15929 variants (59.01%)
    Result: 3.0340936971777346
    .. read 9600 / 15929 variants (60.27%)
    Result: 89.61512757137238
    .. read 9800 / 15929 variants (61.52%)
    Result: 72.34002346267535
    .. read 10000 / 15929 variants (62.78%)
    Result: 117.11832615272706
    .. read 10200 / 15929 variants (64.03%)
    Result: -14.743982350445938
    .. read 10400 / 15929 variants (65.29%)
    Result: 11.98705299203688
    .. read 10600 / 15929 variants (66.55%)
    Result: 111.43049301844309
    .. read 10800 / 15929 variants (67.80%)
    Result: -14.315709132899778
    .. read 11000 / 15929 variants (69.06%)
    Result: 48.617625544156496
    .. read 11200 / 15929 variants (70.31%)
    Result: -20.00727644211451
    .. read 11400 / 15929 variants (71.57%)
    Result: -59.300078720370834
    .. read 11600 / 15929 variants (72.82%)
    Result: 46.00359413870454
    .. read 11800 / 15929 variants (74.08%)
    Result: 72.30226579174433
    .. read 12000 / 15929 variants (75.33%)
    Result: -61.685905978762975
    .. read 12200 / 15929 variants (76.59%)
    Result: 29.078820766788667
    .. read 12400 / 15929 variants (77.85%)
    Result: -42.94694959575352
    .. read 12600 / 15929 variants (79.10%)
    Result: -71.69481829181149
    .. read 12800 / 15929 variants (80.36%)
    Result: -19.13047845855384
    .. read 13000 / 15929 variants (81.61%)
    Result: -78.25805157473718
    .. read 13200 / 15929 variants (82.87%)
    Result: -134.4075742710578
    .. read 13400 / 15929 variants (84.12%)
    Result: 106.09895668041852
    .. read 13600 / 15929 variants (85.38%)
    Result: -127.45465981769064
    .. read 13800 / 15929 variants (86.63%)
    Result: -18.335427508625894
    .. read 14000 / 15929 variants (87.89%)
    Result: 98.20454314478086
    .. read 14200 / 15929 variants (89.15%)
    Result: 18.86291543490482
    .. read 14400 / 15929 variants (90.40%)
    Result: 83.5512500268531
    .. read 14600 / 15929 variants (91.66%)
    Result: 67.78377400714238
    .. read 14800 / 15929 variants (92.91%)
    Result: -12.928835500603215
    .. read 15000 / 15929 variants (94.17%)
    Result: -64.7657284402363
    .. read 15200 / 15929 variants (95.42%)
    Result: -29.27809775283688
    .. read 15400 / 15929 variants (96.68%)
    Result: -25.711359348095776
    .. read 15600 / 15929 variants (97.93%)
    Result: 36.17358874299279
    .. read 15800 / 15929 variants (99.19%)
    Result: -106.72796041500679
    .. read 15929 / 15929 variants (100.00%)
    Result: -87.96227721980513


Bgen file example
^^^^^^^^^^^^^^^^^

.. testcleanup::

    import os

    if os.path.exists("example.bgen"):
        os.remove("example.bgen")

.. testcode::

    import numpy as np
    from numpy.random import RandomState
    from bgen_reader import read_bgen, compute_dosage, allele_expectation
    from sklearn.impute import SimpleImputer
    
    import geno_sugar as gs
    import geno_sugar.preprocess as prep
    
    gs.download("https://github.com/limix/bgen-reader-py/blob/master/example/example.bgen?raw=true")
    
    # define random state
    random = RandomState(1)
    
    # import genotype file
    bgen_file = "example.bgen"
    bgen = read_bgen(bgen_file, verbose=False)
    bim = bgen["variants"]
    G = compute_dosage(allele_expectation(bgen["genotype"], nalleles=2, ploidy=2))
    print(bim)
    print(G)
    # TODO: We need to fix this error:
    # Traceback (most recent call last):
    #   File "ex.py", line 25, in <module>
    #     G, bim = gs.snp_query(G, bim, Isnp)
    #   File "/Users/horta/code/horta/geno-sugar/geno_sugar/utils.py", line 25, in snp_query
    #     G_out = G[bim_out.i.values]
    #   File "/usr/local/anaconda3/envs/default/lib/python3.7/site-packages/pandas/core/generic.py", line 4376, in __getattr__
    #     return object.__getattribute__(self, name)
    # AttributeError: 'DataFrame' object has no attribute 'i'
    
    # subsample snps
    Isnp = gs.is_in(bim, ("22", 17500000, 28500000))
    G, bim = gs.snp_query(G, bim, Isnp)
    
    # define geno preprocessing function
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    preprocess = prep.compose([
                    prep.filter_by_missing(max_miss=0.10),
                    prep.impute(imputer),
                    prep.filter_by_maf(min_maf=0.10),
                    prep.standardize()
                    ])
    
    # define filtering function
    filter = gs.unique_variants
    
    # loop on geno
    queue = gs.GenoQueue(G, bim, batch_size=200, preprocess=preprocess)
    for _G, _bim in queue:
        # run genetic analysis
        print('Result:', np.einsum('is,is->', random.rand(*_G.shape), _G))


